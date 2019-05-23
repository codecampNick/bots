import requests
import time
import logging as log

log.basicConfig(level=log.INFO, 
filename='easyFyi.log', 
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
datefmt='%Y-%m-%d %H:%M:%S')

def main():
    base_url = 'https://www.easyfyinow.com/'
    loads = 0
    for num in range(0,2):
        page = requests.get(base_url)
        time.sleep(2)
        if page.status_code != 200:
            log.info('bad request from ' + base_url)
        page = requests.get(base_url + 'strategy.html')
        if page.status_code != 200:
            log.info("bad request retuned from " + base_url + 'strategy.html')
        loads += 1
    log.info('number of loops: ' + str(loads))      


if __name__ == '__main__':
    main()