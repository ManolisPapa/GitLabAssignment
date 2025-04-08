## YFinance:
- yfinance.Ticker.history(start, end): Returns stock price history from start date to end date, both non-inclusive.  
    Dates should be formatted as YYYY-MM-DD
- yfinance.Ticker.history(period): Returns stock price history for specified period starting from today
- yfinance.Ticker.info: A dictionary containing detailed information about the company behind the ticker
- yfinance.Ticker.fast-info: A dictionary containing important information about a stock
- yfinance.Ticker.news: A dictionary containing some recent new around the stock

## Streamlit:
- For anything related to Streamlit you can find documentation and examples around all of the components you'll need [here](https://docs.streamlit.io/develop/api-reference)

## Pandas: 
- pandas.read_csv(url): Returns a dataframe with the contents of a .csv file

## Plotly: 
- plotly.graph_objects.Figure(data=[go.Pie(labels, values, hole, marker=dict(colors=colors))]): Creates a donut chart with specified labels, values, a size for the hole (0, 1) and colors.

## Useful links:
- [S&P500 Tickers csv](https://gist.githubusercontent.com/ZeccaLehn/f6a2613b24c393821f81c0c1d23d4192/raw/fe4638cc5561b9b261225fd8d2a9463a04e77d19/SP500.csv)