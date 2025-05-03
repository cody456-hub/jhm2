import yfinance as yf

# 定义股票代码
tickers = ["AAPL", "SPY", "XLK"]

# 设置时间范围
start_date = "2020-01-01"
end_date = "2025-04-25"

# 下载数据并保存到单独的 CSV 文件
for ticker in tickers:
    df = yf.download(ticker, start=start_date, end=end_date)
    df.to_csv(f"{ticker}_stock_data.csv")
    print(f"{ticker} 的数据已保存到 {ticker}_stock_data.csv")