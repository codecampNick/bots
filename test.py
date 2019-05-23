from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import re
import time
import logging

def main():
    base_url = 'https://www.python.org/'
    try:
        logging.debug('This is a debug message')
        logging.error('This is a error message')
        print('imported webdriver')
        print('Imported Beautiful Soup')
        driver = webdriver.Chrome('./chromeDriver')
        print('Driver loaded. Webpage opened in "Chrome" in an new instanse of Chrome.')
        print('Opening the python website')
        print('Getting nav bar in selenium')
        driver.get(base_url)
        try:
            #page = driver.text
            print(f"python.org is loaded in chrome.")
            nav_bar = driver.find_element_by_id('mainnav')
            print(nav_bar.text)
            nav_links = nav_bar.find_elements_by_xpath('child::ul/child::li')
            print(nav_links)
            for nav in nav_links:
                #print(nav.text)
                #print(nav)
                if(nav.text == 'Documentation'):
                    print('found documentation')
                    time.sleep(1)
                    hover = ActionChains(driver).move_to_element(nav)
                    hover.perform()
                    links = nav.find_elements_by_xpath('child::ul/child::li/child::a')
                    print(len(links))
                    link_list = []
                    for link in links:
                        link_title = link.get_attribute('outerHTML')
                        print(link_title)
                        path = link.get_attribute('href')
                        print(path)
                        link_list.append(path)
                    for l in link_list:
                        driver.get(l)
                        current_url = driver.current_url
                        if  current_url.endswith('/') and not l.endswith('/'):
                            current_url = current_url[0:-1]
                        if current_url == l:
                            driver.back()
                            continue
                        else:
                            raise ValueError(f"urls do not match. was looking for {l} but url is {current_url}")
                else:
                    continue

            #return to main page and do a search
            driver.get(base_url)
            search_field = driver.find_element_by_id('id-search-field')
            search_go_button = driver.find_element_by_id('submit')
            search_field.send_keys('careers')
            search_go_button.clck()
            input('did the search work?')


            print('Cool! Working so far!')
            
        except Exception as ex:
            print("Dang! Error." + ex)

    except Exception as e:
        print(e)
        closeProgram = input('Ooops! This crashed! Press "Enter" to close Browser and exit the program.')
        driver.close()
        closeProgram()
    driver.close()
    input('No errors! Press enter to close program.')
    
    #*[@id="mainnav"]
    

if __name__ == "__main__":
    main()
print('Done!')
