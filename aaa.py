import yfinance as yf

# 設定股票代碼
ticker = "APY"

# 設定時間範圍
start_date = "2020-01-01"
end_date = "2025-04-25"

# 下載數據
df = yf.download(ticker, start=start_date, end=end_date)

# 存為 CSV 文件
csv_filename = f"{ticker}_stock_data.csv"
df.to_csv(csv_filename)

print(f"{ticker} 的數據已保存到 {csv_filename}")

