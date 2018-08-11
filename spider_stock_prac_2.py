
# coding: utf-8

# In[1]:


import time
import csv
import requests

#使用selenium webdriver進行抓取
from selenium import webdriver
chromedriver="D:\chromedriver_win32/chromedriver"
driver=webdriver.Chrome(chromedriver)

#獲取要爬取的網頁
driver.get("http://www.tse.com.tw/zh/page/trading/fund/TWT38U.html")

#之後要儲存檔案的路徑，output.csv是要寫入的檔案名稱，若路徑上沒有檔案則會新建一個檔案。
store_destination="C:/Users/user/Desktop/python pracice/stock data/output.csv"


# In[6]:


def search_a_month():
    
    year_for_search=input("請輸入欲查詢之年份(西元):")
    month_for_search=input("請輸入欲查詢之月份:")
    place_for_store=input("請輸入儲存路徑:")
    
    # xpath路徑
    xpath_year="//select[@name='yy']/option[@value="+"'" +str(year_for_search) +"'"+ "]"
    xpath_month="//select[@name='mm']/option[@value="+"'" +str(month_for_search) +"'"+ "]"

    for i in range(1,32):
        date=str(i)
        xpath_date="//select[@name='dd']/option[@value="+"'" +str(i) +"'"+ "]"
    
        print(xpath_year)
        print(xpath_month)
        print(xpath_date)
            
        try:
                
            #使用selenium模仿點擊網頁，用以獲取爬取所需頁面    
            select_year=driver.find_element_by_xpath(xpath_year)
            select_year.click()
            select_month=driver.find_element_by_xpath(xpath_month)
            select_month.click()
            select_date=driver.find_element_by_xpath(xpath_date)
            select_date.click()

            start_search=driver.find_element_by_xpath("//a[@href='#']")
            start_search.click()
            time.sleep(5)        
            
            #獲取頁面上所需資訊的xpath路徑
            y=driver.find_elements_by_xpath("//tr/td")
            for i in range(0,10):
                
                output_list=[year_for_search+"/"+month_for_search+"/"+date, y[6+i*12].text, y[7+i*12].text, y[10+i*12].text]
                print(output_list)
                
                #建立csv檔，並將獲取的資料寫入
                with open(place_for_store,"a+",encoding="UTF-8",newline='') as csvfile:
                    w=csv.writer(csvfile)
                    w.writerow(output_list)  
                
                    
        except:
            continue
                

