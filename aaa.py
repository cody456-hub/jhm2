import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

# 設定時間範圍
start = datetime(2020, 1, 1)
end = datetime(2025, 4, 25)

# 取得 SPY 的數據
spy_data = web.DataReader('SPY', 'yahoo', start, end)

# 顯示數據
print("SPY Data:")
print(spy_data.head())