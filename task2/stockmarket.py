import streamlit as st
import plotly.graph_objects as go
import yfinance as yf
from st_click_detector import click_detector

# Ideas for improvement:
# 1. Add more stock tickers to the list.
# 2. Allow users to input a custom date range for the stock data.
# 3. Allow users to select different types of charts (e.g., line chart, bar chart).
# 4. Allow users to provide their own tickers, with error handling for invalid tickers.
# 5. Show information about the stock (e.g., market cap, P/E ratio) alongside the chart.
# 6. Add a download button for the stock data in CSV format. 
# 7. Investment portfolio tracker: Allow users to input multiple stocks and track their performance over time.
# 8. Add a news section to show the latest news related to the selected stock.


def show_tickers():
    content = """
        <a href='#' id='MSFT'><img height='60px' width='60px' src='https://banner2.cleanpng.com/20180609/jq/aa8dbj2or.webp'></a>
        <a href='#' id='AAPL'><img height='60px' width='60px' src='https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg'></a>
    """
    return content

def get_ticker():
    content = show_tickers()
    clicked = click_detector(content)
    return clicked

def show_plot(fig):
    # Display the candlestick chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

def get_dataframe(ticker):
    # Get the stock data for the given ticker
    stock_data = yf.Ticker(ticker)
    df = stock_data.history(period="1y")
    df.reset_index(inplace=True)  # This moves the date from index to a column
    return df

def plot_candlestick(df, ticker):
    # Create a candlestick chart using Plotly
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.update_layout(title=f'{ticker} Stock Price', xaxis_title='Date', yaxis_title='Price (USD)')
    return fig

ticker = get_ticker()
if ticker != "":
    df = get_dataframe(ticker)
    fig = plot_candlestick(df, ticker)
    show_plot(fig)
