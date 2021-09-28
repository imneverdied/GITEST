import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DataTable2excel2 import DataTable2excel
import tkinter.messagebox
import webbrowser


def callback(url):
    webbrowser.open_new(url)


def PopMessage(msg):
    window = tkinter.Tk()
    window.title('錯誤')
    window.geometry('+300+350')  # 訊息內容
    Label1 = tkinter.Label(window, text="缺少chromedriver",
                           fg="black", cursor="hand2")
    Label1.pack()
    link1 = tkinter.Label(window, text="點擊下載",
                          fg="blue", cursor="hand2")
    link1.pack()

    link1.bind(
        "<Button-1>", lambda e: callback("https://chromedriver.chromium.org/"))
    window.mainloop()


options = Options()

prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
# options.binary_location = '/usr/bin/chromium-browser'
options.add_argument("--headless")  # 不開啟實體瀏覽器背景執行
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')


base_url = "https://mis.twse.com.tw/stock/etf_nav.jsp?ex=tse"

try:
    browser = webdriver.Chrome(options=options,
                               executable_path='chromedriver')
except:
    print("缺少chromedriver")
    PopMessage("缺少chromedriver")

browser.get(base_url)
print('網頁讀取中..')
time.sleep(3)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
div = soup.select_one("div#content")
table = pd.read_html(str(div))
frames = [table[0], table[1], table[3], table[5]]
result = pd.concat(frames, ignore_index=True)


print('資料處理中..')

df = result[['ETF代號/名稱', '成交價',
             '投信或總代理人預估淨值(註2)', '預估折溢價幅度(註3)']]


df.columns = ['名稱', '市價', '估淨值', '估折溢價幅度']


# excel欄位設定
excel_columns = ''
for i in range(len(df.columns)):
    excel_columns = excel_columns + df.columns[i] + ','
excel_columns = excel_columns[:-1]  # 移除最後一個','
# print(excel_columns) # 欄位名稱
# excel欄位設定

# TEMP_values = frames[0].values[00][0]  # 名稱
# TEMP_values = frames[0].values[00][3]  # 市價
# TEMP_values = frames[0].values[00][4]  # 估淨值
# TEMP_values = frames[0].values[00][5]  # 估折溢價幅度

DataTable2excel.createTable(excel_columns)

for S in range(3):
    for i in range(len(frames[0].values)):
        DataTable2excel.insert2Table(
            frames[S].values[i][0], frames[S].values[i][3], frames[S].values[i][4], frames[S].values[i][5])


DataTable2excel.OutExcel('ETF')


browser.quit()

print('完成...3秒後自動關閉')
time.sleep(3)
