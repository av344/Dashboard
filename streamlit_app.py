# Import Libraries
import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# Define the tickers and number of shares
portfolio = {
    'QQQ': 7,
    'TTWO': 2
}

# Updated purchase prices
purchase_prices = {
    'QQQ': 428.35,
    'TTWO': 156.0683
}

# Portfolio start date
portfolio_start_date = '2024-01-25'

# Fetch latest prices
def fetch_latest_prices(tickers):
    data = yf.download(tickers, period='1d', interval='1m')
    return data['Adj Close'].iloc[-1]

# Calculate returns and ROI%
def calculate_returns(latest_prices, purchase_prices, portfolio):
    returns = {}
    roi_percentages = {}
    for ticker, shares in portfolio.items():
        purchase_price = purchase_prices[ticker]
        current_price = latest_prices[ticker]
        return_value = (current_price - purchase_price) * shares
        roi_percentage = ((current_price - purchase_price) / purchase_price) * 100
        returns[ticker] = return_value
        roi_percentages[ticker] = roi_percentage
    return returns, roi_percentages

# Calculate the difference in months since the portfolio start date
def calculate_months_difference(start_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    current_date = datetime.today()
    months_difference = (current_date.year - start_date.year) * 12 + current_date.month - start_date.month
    return months_difference

# Main function to run the app
def main():
    st.title('Portfolio Dashboard')

    # Fetch latest prices
    latest_prices = fetch_latest_prices(list(portfolio.keys()))
    
    # Calculate returns and ROI%
    returns, roi_percentages = calculate_returns(latest_prices, purchase_prices, portfolio)

    # Calculate months since portfolio started
    months_difference = calculate_months_difference(portfolio_start_date)

    # Display latest prices
    st.write("## Latest Prices")
    st.write(latest_prices)

    # Display portfolio returns and ROI%
    st.write("## Portfolio Returns")
    for ticker, return_value in returns.items():
        st.write(f"{ticker}: ${return_value:.2f} ({roi_percentages[ticker]:.2f}%)")

    # Display months since start of portfolio
    st.write(f"## Months Since Portfolio Start: {months_difference} months")

if __name__ == '__main__':
    main()
