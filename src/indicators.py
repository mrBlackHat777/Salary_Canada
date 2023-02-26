from datetime import datetime, timedelta, date
from enum import Enum, IntEnum
import math

class Resolution(Enum):
    DAILY = "1day"
    HALF_DAY = "12hour"
    EIGHT_HOURS = "8hour"
    FOUR_HOURS = "4hour"
    HOURLY = "1hour"
    MINUTE = "1min"


Weekday = IntEnum('Weekday', 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday', start=0)
NthWeek = IntEnum('NthWeek', 'First Second Third Fourth Last', start=1)


def nth_day_of_nth_week(date: datetime, nth_week: int, week_day: int) -> datetime:
    temp_date = date.replace(day=1)
    adj = (week_day - temp_date.weekday()) % 7
    temp_date += timedelta(days=adj)
    temp_date += timedelta(weeks=nth_week - 1)
    return temp_date


def calc_good_friday(year: int) -> datetime:
    a = year % 19
    b, c = divmod(year, 100)
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    return datetime(year, month, day) + timedelta(days=-2)


def us_holiday_list(_year: int) -> list:
    holidays = [datetime(year=_year, month=1, day=1)]

    # Birthday of Martin Luther King, Jr., the third Monday in January.
    holidays.append(nth_day_of_nth_week(datetime(year=_year, month=1, day=1), NthWeek.Third, Weekday.Monday))

    # Washington’s Birthday, the third Monday in February.
    holidays.append(nth_day_of_nth_week(datetime(year=_year, month=2, day=1), NthWeek.Third, Weekday.Monday))

    # Good Friday, the Friday before Easter
    holidays.append(calc_good_friday(year=_year))

    # Memorial Day, the last Monday in May.
    holidays.append(nth_day_of_nth_week(datetime(year=_year, month=5, day=1), NthWeek.Last, Weekday.Monday))

    # Juneteenth National Independence Day, June 19.
    holidays.append(datetime(year=_year, month=6, day=19))

    # Independence Day, July 4.
    holidays.append(datetime(year=_year, month=7, day=4))

    # Labor Day, the first Monday in September.
    holidays.append(nth_day_of_nth_week(datetime(year=_year, month=9, day=1), NthWeek.First, Weekday.Monday))

    # Thanksgiving Day, the fourth Thursday in November.
    holidays.append(nth_day_of_nth_week(datetime(year=_year, month=11, day=1), NthWeek.Fourth, Weekday.Thursday))

    # Christmas Day, December 25.
    holidays.append(datetime(year=_year, month=12, day=25))

    # Adjust Saturday holidays to Friday and Sunday holidays to Monday
    for holiday in holidays:
        if holiday.weekday() == Weekday.Saturday:
            holiday += timedelta(days=-1)
        if holiday.weekday() == Weekday.Sunday:
            holiday += timedelta(days=1)

    return holidays


@staticmethod
def is_market_open(date: datetime, resolution: Resolution) -> bool:
    if date.weekday() >= 5:
        return False

    if resolution != Resolution.DAILY:
        if date.hour < 9 or date.hour > 16:
            return False
        elif date.hour == 16 and date.minute > 0:
            return False
        elif date.hour == 9 and date.minute < 30:
            return False

    return date not in us_holiday_list(date.year)

def get_date_in_x_market_days_away(lapse: int, start_date: datetime = datetime.now()) -> date:
    """
    Gets the date that is x amount of market day(s) away
    Args:
        lapse: Number of days wanted
        start_date: date at which the function starts, default: present day
    Returns: The date that is the amount of market days away in date format
    """
    countdown = lapse
    today = start_date
    while countdown > 0:
        today = today + timedelta(days=+1)
        if is_market_open(today):
            countdown -= 1
    return today

def sma(data_source, symbol: str, period: int, date: datetime = None):
    """
    Calculates the Simple Moving Average
    Args:
        data_source: DataSource object
        symbol: Stock symbol
        period: number of days for the average
        date: Date of average / start date. If no value is given the function will use the date of the backtest
    Returns:
        sma: Average stock price for the given range
    """

    date = data_source.timestamp if date is None else date
    values = []

    for _ in range(period):
        # Go back one day
        date -= timedelta(days=1)

        # Make sure market is open
        while not is_market_open(date, Resolution.DAILY):
            date -= timedelta(days=1)

    for _ in range(period):
        # Go forward one day
        date += timedelta(days=1)

        # Make sure market is open
        while not is_market_open(date, Resolution.DAILY):
            date += timedelta(days=1)

        # Fetch stock value
        price = data_source.get_price(symbol=symbol, timestamp=date)
        if price is not None:
            values.append(price)

    return sum(values) / len(values)

def wma(data_source, symbol: str, period: int, date: datetime = None):
    """
        Calculates the Weight Moving Average
        Args:
            symbol: Stock symbol
            period: number of days for the average
            date: Date of average / start date
        Returns:
            wma: Average stock price weight for the given range
        """
    date = data_source.timestamp if date is None else date
    wma = 0

    weight_total = sum(x + 1 for x in range(period))
    for _ in range(period):
        # Go back one day
        date -= timedelta(days=1)

        # Make sure market is open
        while not is_market_open(date, Resolution.DAILY):
            date -= timedelta(days=1)

    for x in range(period):
        # Go forward one day
        date += timedelta(days=1)

        # Make sure market is open
        while not is_market_open(date, Resolution.DAILY):
            date += timedelta(days=1)

        # Fetch stock value
        price = data_source.get_price(symbol=symbol, timestamp=date)

        if price is not None:
            current_weight = ((x + 1) / weight_total)
            print("Price: ", price, " Weight: ", x + 1,
                " / ", weight_total, " = ", current_weight)
            wma += price * current_weight

    return wma

def ema(data_source, symbol: str, period: int, date: datetime = None, smoothing: int = 2):
    """
        Calculates the Exponential Moving Average
        Args:
            symbol: Stock symbol
            period: number of days for the average
            date: Date of average / start date. If no value is given the function will use the date of the backtest
            smoothing: weighted importance of latest data, higher number gives more weight to more recent data
        Returns:
            ema: Exponential average stock price for the given range
        """

    date = data_source.timestamp if date is None else date
    multiplier = smoothing/(period + 1)

    for _ in range(period):
        ##Go back one day
        date -= timedelta(days=1)

        #Make sure market is open
        while not is_market_open(date, Resolution.DAILY):
            date -= timedelta(days=1)

    ema = sma(data_source, symbol, period, date)

    for _ in range(period):
        ##Go forward one day
        date += timedelta(days=1)

        # Make sure market is open
        while not is_market_open(date, Resolution.DAILY):
            date += timedelta(days=1)

        price = data_source.get_price(symbol=symbol, timestamp=date)
        if price is not None:
            ema = price*multiplier + ema*(1-multiplier)

    return ema

def macd(data_source, symbol, date: datetime = None):
    """
        Calculates the Moving Average Converging/Diverging
        Args:
            symbol: Stock symbol
            date: Date of average / start date. If no value is given the function will use the date of the backtest
        Returns:
            macd
        """

    date = data_source.timestamp if date is None else date
    return data_source.ema(symbol, 12, date) - data_source.ema(symbol, 26, date)

def rsi(data_source, symbol: str, period: int = 14, date: datetime = None):
    # sourcery skip: avoid-builtin-shadow
    """
        Calculates the Relative Strength Index
        Args:
            symbol: Stock symbol
            period: number of days for the average
            date: Date of average / start date. If no value is given the function will use the date of the backtest
        Returns:
            rsi
        """

    date = data_source.timestamp if date is None else date
    total_gain = 0
    total_loss = 0

    for _ in range(period):
        ##Go back one day
        date -= timedelta(days=1)

        # Make sure market is open
        while not is_market_open(date, Resolution.DAILY):
            date -= timedelta(days=1)

    for _ in range(period):
        ##Go forward one day
        date += timedelta(days=1)

        # Make sure market is open
        while not is_market_open(date, Resolution.DAILY):
            date += timedelta(days=1)

        # fill each value
        open = data_source.get_price(symbol=symbol, timestamp=date, value="open")
        close = data_source.get_price(symbol=symbol, timestamp=date, value="close")
        if open is not None and close is not None:
            daily_percent = (close - open) / open
            if daily_percent > 0:
                total_gain += daily_percent
            else:
                total_loss += daily_percent

    if total_gain <= 0:
        return 0
    elif total_loss >= 0:
        return 100

    return 100 - 100 / (1 - total_gain / total_loss)

def std_dev(data_source, symbol: str, period: int, date: datetime = None):
    """
        Calculates the Exponential Moving Average
        Args:
            symbol: Stock symbol
            period: number of days for the average
            date: Date of average / start date. If no value is given the function will use the date of the backtest
        Returns:
            std_dev
        """
    differences = []
    sum_squared = 0.0
    sma = sma(data_source, symbol, period, date)
    # table of market price for each day in the period
    values = []

    for _ in range(period):
        ##Go back one day
        date -= timedelta(days=1)

        # Make sure market is open
        while not is_market_open(date, Resolution.DAILY):
            date -= timedelta(days=1)

    for _ in range(period):
        ##Go forward one day
        date += timedelta(days=1)

        # Make sure market is open
        while not is_market_open(date, Resolution.DAILY):
            date += timedelta(days=1)

        # fill each value
        price = data_source.get_price(symbol=symbol, timestamp=date)
        if price is not None:
            values.append(price)

    # calculate difference between each value and ema
    for x in range(len(values)):
        differences.append(values[x] - sma)
        sum_squared += differences[x] * differences[x]

    # calculate variance
    variance = sum_squared / len(differences)

    return math.sqrt(variance)

def bollinger_bands(data_source, symbol: str, period: int = 20, mult: int = 2, date: datetime = None):
    """
        Bollinger Bands are computed based on standard deviations on the SMA.
        Args:
            symbol: Stock symbol
            period:
            date:
        Returns:
            bollingerBands: Upper Band and Lower Band
        """

    date = data_source.timestamp if date is None else date
    # Simple Moving Average
    mean = sma(data_source, symbol, period, date)
    # Standard Deviation
    std_dev = std_dev(data_source, symbol, period, date)

    # Calculates Upper Band (sma 20 + 2 std dev)
    upper_band = mean + (mult * std_dev)
    # Calculates Lower Band (sma 20 - 2 std dev)
    lower_band = mean - (mult * std_dev)

    return lower_band, upper_band