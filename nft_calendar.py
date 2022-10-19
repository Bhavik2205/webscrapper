from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
from bs4 import BeautifulSoup
import pandas as pd
import threading
import proxy3


class cpu_thread:
    def nft_response(self):
        options = Options()
        options.headless = True
        PROXY = proxy3.Proxy3().proxy()[0]
        options.add_argument('--proxy-server=%s' % PROXY)
        driver = webdriver.Chrome(
            options=options, executable_path='/Users/bhavikpatel/Downloads/chromedriver')

        driver.implicitly_wait(1)
        driver.get('https://nftcalendar.io/events/archive')
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, 'html5lib')
        content = soup.find('div', {'class': 'content'}).find_all('a')

        div_data = []
        for a_tag in content:
            print("working on ", a_tag['href'])
            url = "https://nftcalendar.io"+a_tag['href']

            driver.implicitly_wait(1)
            driver.get(url)
            time.sleep(1)
            new_soup = BeautifulSoup(driver.page_source, 'html5lib')
            div_mx = new_soup.find('div', {'class': 'mx-2'}).find_all(
                'div', {'class': 'p-4'}) if new_soup.find('div', {'class': 'mx-2'}) != None else ''
            div_data.extend(div_mx)


        self.web_response(div_data)
"""
    def web_response(self, div_data):
        coin_data = []
        n = 1
        for tag_a in div_data:
            print("\tCurrent count is : ", n)
            new_urls = "https://nftcalendar.io" + tag_a.find('a')['href']
            driver = webdriver.Chrome(executable_path='E:\Project\erience solutions\chrome_driver\chromedriver')
            
            driver.implicitly_wait(1)
            driver.get(new_urls)
            time.sleep(1)

            soup_content = BeautifulSoup(driver.page_source, 'html5lib')
            div_class = soup_content.find('div', {'class': 'p-6'})
            if div_class != None:
                name = div_class.find('h1').text
                image = div_class.find('img', {'class': 'rounded'})['src']
                verification_type = div_class.find('span', {'class': 'text-sm'}).text.strip()

                time_boundation = div_class.find('div', {'class': 'text-lg py-3 dark:text-yellow-50'}).text.strip().replace('\n', ' ') if div_class.find('div', {'class': 'text-lg py-3 dark:text-yellow-50'}) != None else ''
                start_time = time_boundation.split('–')[0].strip()
                end_time = time_boundation.split('–')[-1].strip()

                network_links = div_class.find('div', {'class': 'flex flex-wrap items-center pt-1'})#.find_all('a')
                website_link = 'https://nftcalendar.io' + network_links.find('a', {'href': re.compile('/out*')})['href'] if network_links.find('a', {'href': re.compile('/out*')}) != None else ''
                twitter_link = network_links.find('a', {'href': re.compile('twitter*')})['href'] if network_links.find('a', {'href': re.compile('twitter*')}) != None else ''
                discord_link = network_links.find('a', {'href': re.compile('discord*')})['href'] if network_links.find('a', {'href': re.compile('discord*')}) != None else ''
                market_place_url = network_links.find('a', {'href': re.compile('opensea*')})['href'] if network_links.find('a', {'href': re.compile('opensea*')}) != None else ''
                
                more_link = div_class.find('div', {'class': 'flex flex-wrap'}).find_all('a')
                marketplace_link = 'https://nftcalendar.io' + more_link[0]['href']
                marketplace_name = more_link[0].text.strip()

                blockchain_url = 'https://nftcalendar.io' + more_link[1]['href'] if len(more_link)>1 else ''
                blockchain_name = more_link[1].text.strip() if len(more_link)>1 else ''
                description = '\"'+ div_class.find('div', {'class': 'content'}).text.strip().replace(',', '') +'\"'

                data = {"Name": name, "Image": image, "Verification Type": verification_type, "Start Time": start_time, "End Time": end_time, 
                        "Website": website_link, "Twitter": twitter_link, "Discord": discord_link, "Marketplace URL": market_place_url, 
                        "Marketplace Link": marketplace_link, "Marketplace Name": marketplace_name, "blockchain Link": blockchain_url, 
                        "Blockchain Name": blockchain_name, "Description": description}
                coin_data.append(data)
            n += 1

            df = pd.DataFrame(coin_data)
            df.to_csv('nft_calendar.csv')
            df.to_json('nft_calendar.json')
"""


def __init__(self):
    thread_1 = threading.Thread(target=self.nft_response)
    #thread_2 = threading.Thread(target=self.web_response)
    thread_1.start()
    #thread_2.start()


#cpu_thread().web_response()
