# -*- coding: utf-8 -*-
import httpx
from code import make_api_request
from config import FMP_API_KEY, BINANCE_API_KEY, BASE_URL_BINANCE, BASE_URL_FMP


async def get_senate_disclosure():
    api_endpoint = "https://financialmodelingprep.com/api/v4/senate-disclosure"
    params = {"symbol": "AAPL", "apikey": FMP_API_KEY}

    return await make_api_request(api_endpoint, params)

async def get_revenue_product_segmentation(symbol, download=False, structure="flat"):
    api_endpoint = (
        "https://financialmodelingprep.com/api/v4/revenue-product-segmentation"
    )
    params = {
        "symbol": symbol,
        "datatype": "csv" if download else "json",
        "structure": structure,
        "apikey": FMP_API_KEY,
    }

    return await make_api_request(api_endpoint, params)


async def get_revenue_geographic_segmentation(symbol, download=False, structure="flat"):
    api_endpoint = (
        "https://financialmodelingprep.com/api/v4/revenue-geographic-segmentation"
    )
    params = {
        "symbol": symbol,
        "datatype": "csv" if download else "json",
        "structure": structure,
        "apikey": FMP_API_KEY,
    }

    return await make_api_request(api_endpoint, params)

async def get_income_statements(symbol, limit=120, download=False, period="quarter"):
    api_endpoint = f"{BASE_URL_FMP}/income-statement"
    params = {
        "symbol": symbol,
        "limit": limit,
        "datatype": "csv" if download else "json",
        "period": "quarter",
        "apikey": FMP_API_KEY,
    }

    return await make_api_request(api_endpoint, params)


async def get_balance_sheet(symbol, limit=120, download=False, period="quarter"):
    api_endpoint = f"{BASE_URL_FMP}/balance-sheet-statement"
    params = {
        "symbol": symbol,
        "limit": limit,
        "datatype": "csv" if download else "json",
        "period": "quarter",
        "apikey": FMP_API_KEY,
    }

    return await make_api_request(api_endpoint, params)


async def get_cash_flow(symbol, limit=120, download=False, period="quarter"):
    api_endpoint = f"{BASE_URL_FMP}/cash-flow-statement"
    params = {
        "symbol": symbol,
        "limit": limit,
        "datatype": "csv" if download else "json",
        "period": "quarter",
        "apikey": FMP_API_KEY,
    }

    return await make_api_request(api_endpoint, params)


async def get_historical_data(symbol, interval, limit=500):
    api_endpoint = f"{BASE_URL_BINANCE}/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}

    return await make_api_request(api_endpoint, params)


async def get_historical_price_full_crypto(symbol):
    api_endpoint = f"{BASE_URL_FMP}/v3/historical-price-full/crypto/${symbol}"
    params = {"apikey": FMP_API_KEY}

    return await make_api_request(api_endpoint, params)


async def get_historical_price_full_stock(symbol):
    api_endpoint = f"{BASE_URL_FMP}/v3/historical-price-full/stock/${symbol}"
    params = {"apikey": FMP_API_KEY}

    return await make_api_request(api_endpoint, params)
