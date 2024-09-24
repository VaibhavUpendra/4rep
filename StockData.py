import yfinance as yf

ticker = input("Enter the Ticker: ")
from_date = input("Enter start date (YYYY-MM-DD) :")
to_date = input("Enter end date (YYYY-MM-DD) :")

stock_data = yf.download(ticker,start=from_date,end=to_date)
stock_data.to_html("Stock_Data.html")
print("Stock data written to Stock_Data.csv")
