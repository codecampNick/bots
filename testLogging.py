import logging as log
import time
from selenium import webdriver

class JobProperites:
    def __init__(self):
        self.id = ""
        self.title = ""

log.basicConfig(level=log.INFO, 
filename='/Users/iSagui/Desktop/python.log', 
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
datefmt='%Y-%m-%d %H:%M:%S')

base_url = 'https://python.org/'

def main():
    log.info('starting program')
    log.info('**Initializing chrome driver**')
    driver = webdriver.Chrome('./chromeDriver')
    log.info('**chrome driver initialized**')
    try:
        log.info('Opening python website')
        driver.get(base_url)
        driver.find_element_by_id('text-input-what')
        time.sleep(10)
        job = JobProperites()
        log.info('Closing website')
        driver.close()
        log.info('Website and window closed.')
        job.id = 'testId'
        job.title = 'Great Job!'
        log.info(f'Job Id: {job.id} Job Title: {job.title}')
    except:
        log.info('The "try" failed.')


if __name__ == '__main__':
    main()
log.info('Done!')