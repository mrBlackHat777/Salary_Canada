# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

FMP_API_KEY = os.getenv("FMP_API_KEY")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")

BASE_URL_FMP = "https://financialmodelingprep.com/api/v3"
BASE_URL_BINANCE = "https://fapi.binance.com/fapi/v1/"