# 멀티 프로세싱을 통한 웹 스크래핑 1 

import requests

from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool

def get_link():
    
    url = 'https://beomi.github.io/beomi.github.io_old/'
    data = requests.get(url).text
    soup = bs(data, 'html.parser')
    print(soup)
    my_title = soup.select('h3 > a')
    data = []
    
    for title in my_title:
        data.append(title.get('href'))
    return data
    

def get_content(link):
    abc_link = 'https://beomi.github.io' + link
    data = requests.get(abc_link).text
    soup = bs(data,'html.parser')
    print(soup.select('h1')[0].text)
        

if __name__ == '__main__':
    start_time = time.time()
    #print(get_link())
        
    pool = Pool(processes = 4)
    pool.map(get_content,get_link())
    
        
    print('처리시간 : %s 초'%(time.time() - start_time))