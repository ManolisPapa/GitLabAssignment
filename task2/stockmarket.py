import streamlit as st
import plotly.graph_objects as go
import yfinance as yf
from st_click_detector import click_detector
import time

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# fig = go.Figure(data=[go.Candlestick(x=df['Date'],
#                 open=df['AAPL.Open'],
#                 high=df['AAPL.High'],
#                 low=df['AAPL.Low'],
#                 close=df['AAPL.Close'])])

# st.plotly_chart(fig, use_container_width=True)
# st.title('Stock Market Data')

# msft = yf.Ticker("MSFT")
# msft_history = msft.history(period="1y")
# msft_history.reset_index(inplace=True)  # This moves the date from index to a column
# fig = go.Figure(data=[go.Candlestick(x=msft_history['Date'],
#                 open=msft_history['Open'],
#                 high=msft_history['High'],
#                 low=msft_history['Low'],
#                 close=msft_history['Close'])])
# st.plotly_chart(fig, use_container_width=True)
# st.title('Stock Market Data')
# print(1)

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
