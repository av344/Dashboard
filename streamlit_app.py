
pip install streamlit yfinance pandas numpy matplotlib seaborn 

# Import Libraries
import streamlit as st
import yfinance as yf
import pandas as pd

# App


# Define the tickers and number of shares
portfolio = {
    'QQQ': 7,
    'TTWO': 2
}

# Example purchase prices (adjust with your actual purchase prices)
purchase_prices = {
    'QQQ': 350.00,
    'TTWO': 150.00
}

# Fetch latest prices
def fetch_latest_prices(tickers):
    data = yf.download(tickers, period='1d', interval='1m')
    return data['Adj Close'].iloc[-1]

# Calculate returns
def calculate_returns(latest_prices, purchase_prices, portfolio):
    returns = {}
    for ticker, shares in portfolio.items():
        purchase_price = purchase_prices[ticker]
        current_price = latest_prices[ticker]
        returns[ticker] = (current_price - purchase_price) * shares
    return returns

# Main function to run the app
def main():
    st.title('Portfolio Dashboard')
    latest_prices = fetch_latest_prices(list(portfolio.keys()))
    returns = calculate_returns(latest_prices, purchase_prices, portfolio)

    # Display portfolio returns
    st.write("## Latest Prices")
    st.write(latest_prices)

    st.write("## Portfolio Returns")
    for ticker, return_value in returns.items():
        st.write(f"{ticker}: ${return_value:.2f}")

if __name__ == '__main__':
    main()
