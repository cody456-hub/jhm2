import requests
from bs4 import BeautifulSoup
import pandas as pd

# Barchart 的 APY 歷史數據頁面
url = "https://www.barchart.com/stocks/quotes/APY/historical-data"

# 發送請求
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 找到數據表（需要查看網頁結構以確保準確抓取）
table = soup.find("table")

# 如果找到表格，就轉換成 CSV（這部分需要根據網頁的 HTML 調整）
if table:
    df = pd.read_html(str(table))[0]
    df.to_csv("APY_stock_data.csv", index=False)
    print("APY 的數據已保存到 APY_stock_data.csv")
else:
    print("未找到 APY 的股票數據，請確認網站結構！")