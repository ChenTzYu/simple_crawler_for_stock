# simple_crawler_for_stock_part1

抓取單月外資買超的股票代號、股票名稱、跟買超股數
注意：本文對於股市的看法僅代表個人意見，股市投資必然需要承擔風險，請投資人自行衡量。

簡介：
  在股票的籌碼面中，外資持續買超可以視為一個先行指標，可視為先行指標的原因基本有二：
  
  第一，外資資金龐大，因此無法一次買齊所需要的部位，所以通常需要分成數次，這其中可能是好幾天，也可能持續數星期，也因此，當外資剛開始持續買入的時候便是     散戶可以跟著上車的機會。
    
  第二，外資對於投資標的的選擇必須是經過仔細研究的，需要依據股票本身的基本面以及該產業的狀況來下決定，而非極短線的炒作，因此，外資持續買入可以被視為一     個中長期的趨勢，並且在基本面及產業上是更有保障的。
    
  既然了解到外資持續買超可視為一先行指標，那下一步自然就是開始觀察哪些股票是外資持續買入的對象，而這個簡單的程式也是專門為此設計的，這個程式能夠抓取單月中每日的外資買超對象前10名，並將其股票代號、股票名稱、買超張數記錄下來。

[輸出例子](https://github.com/ChenTzYu/simple_crawler_for_stock_part1/blob/master/output_example.csv)


使用方法：

1.環境設置：程式用到幾個庫，分別是time,csv,requests,selenium

    import time
    import csv
    import requests
    from selenium import webdriver

要使用selenium的webdriver還需要使用chromedriver
[下載地址](http://chromedriver.chromium.org/downloads)

安裝完成後設定chromedriver的位置

    chromedriver="D:\chromedriver_win32/chromedriver"
    driver=webdriver.Chrome(chromedriver)

然後獲取所需要的網頁
    
    driver.get("http://www.tse.com.tw/zh/page/trading/fund/TWT38U.html")


2.執行爬取：爬取只需要使用函數search_a_month()就可以開始

    search_a_month()

函數執行後會要求輸入欲查詢之年份、欲查詢之月份、及儲存路徑

    請輸入欲查詢之年份(西元):
    請輸入欲查詢之月份:
    請輸入儲存路徑：

儲存路徑包括欲儲存的檔案名稱，若該檔案不存在則會新建一個。
以下是實際輸入的例子

    請輸入欲查詢之年份(西元):
    2018
    請輸入欲查詢之月份:
    6
    請輸入儲存路徑：
    C:/Users/user/Desktop/python pracice/stock data/output.csv
    




  
