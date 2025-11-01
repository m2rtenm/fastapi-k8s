from fastapi import FastAPI, Query
from sqlmodel import SQLModel
import yfinance as yf

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/price")
def get_price(symbol: str = Query(...), interval: str = Query("1d"), period: str = Query("1mo")):
    ticker = yf.Ticker(symbol)
    try:
        df = ticker.history(interval=interval, period=period)
        prices = df.reset_index().to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
    return {"symbol": symbol, "interval": interval, "period": period, "prices": prices}

# For future: DB models and integration
