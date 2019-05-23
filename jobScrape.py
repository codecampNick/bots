from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as AC
import logging as log
import time
import re
import utilities
import csv
import jobProperties

log.basicConfig(level=log.INFO, 
filename='/Users/iSagui/Desktop/python.log', 
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
datefmt='%Y-%m-%d %H:%M:%S')
log.debug('Initializing.....')

file_handel = utilities.CsvFunctions()
jobList = []

options = Options()
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(chrome_options=options, executable_path='./chromeDriver')
def main():
    log.info('Starting Program')
    log.info('Opening website...')
    driver.get('https://www.indeed.com/')
    log.info('Website opened!')
    job_type_text_box = driver.find_element_by_id('text-input-what')
    log.info('Entering job type')
    job_type_text_box.send_keys('Developer')
    job_type_text_box.send_keys(Keys.TAB)
    job_location_text_box = driver.find_element_by_id('text-input-where')
    job_location_text_box.send_keys(Keys.DELETE)
    time.sleep(1)
    log.info('Entering location')
    job_location_text_box.send_keys('Parker, CO')
    find_button = driver.find_element_by_xpath('//form/div[3]/button')
    log.info('Clicking Search button')
    find_button.click()
    
    print('**********************')


    log.info('Getting postings')
    log.info("looping page")
    lastPage = False
    page_num, total_postings = 0, 0
    job_ids = []
    while not lastPage:
        jobs = driver.find_element_by_id('resultsCol').find_elements_by_class_name('jobsearch-SerpJobCard')
        
        lastPage = True
        for el in jobs:
            job = jobProperties.Job()
            job_ids.append(job.Id)
            company = el.find_element_by_class_name('company').text
            if company == 'Indeed Prime':
                continue
            else:
                job.CompanyName = company
            job.CompanyName = el.find_element_by_class_name('company').text
            job.Title = el.find_element_by_xpath('.//a').text
            if re.search('writer|technician|manager|sales|retail|marketing|help wanted',job.Title, re.IGNORECASE):
                continue
            job.Headline = el.find_element_by_xpath(".//span[contains(@class, 'summary')]").text
            location = el.find_element_by_class_name('location').text
            job.City = job.get_city(location)
            job.State = job.get_state(location)
            job.Country = job.get_country(location)
            job.Zip = job.get_zip(location)
            el.click()
            #time.sleep(1)
            WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, 'resultsCol')))
            open_tabs = driver.window_handles
            if(len(open_tabs) > 1):
                driver.switch_to_window(open_tabs[1])
                try:
                    log.info('trying first xpath - //main/div/div[1]/div[2]/div')
                    job.Description = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, '//main/div/div[1]/div[2]/div'))).get_attribute('innerHTML')
                    log.info('got description with first xpath')
                except TimeoutError:
                    log.info('trying the second xpath - //div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[4]/div/div')
                    job.Description = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, '//div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[4]/div/div'))).get_attribute('innerHTML')
                    log.info('got desctiption with second xpath')
                except TimeoutError:
                    log.info('second "except"')
                    #add this xpath //div[1]/div[3]/div[3]/div/div/div[1]/div[1]
                    job.Description = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, '//div[1]/div[3]/div[3]/div/div/div[1]/div[1]'))).get_attribute('innerHTML')
                    raise ValueError('WOW caught in second exception')
                except:
                    job.Description = 'description didn''t load in new tab'
                    log.error(f'***couldn''t get description for {job.Id} on results page {page_num}')
                driver.close()
                driver.switch_to_window(open_tabs[0])
            else:
                try:
                    job.Description = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.ID, 'vjs-content'))).get_attribute('innerHTML')
                except:
                    log.info(f'Couldn''t get description for job title: {job.Title}, on page# {total_postings}')
                    continue

            job.UrlToPosting = driver.current_url
            try:
                job.Id = re.search('.*(?:vjk=|\-)(.*)$', job.UrlToPosting).group(1)
            except:
                log.info(f'****************************couldn''t extract job id from {job.Id}')
                break
            if job.Id in job_ids:
                break    
            jobList.append(job)
            total_postings += 1
            #print(el.find_element_by_xpath('.//a').text)
            log.info(f'postings added to list: {total_postings}')

        log.info('Clicking next button')
        main_window_handel = driver.current_window_handle
        try:
            driver.find_element_by_class_name('pagination').find_element_by_partial_link_text('Next').click()
            log.info(f'hitting wait for url to change')
            #WebDriverWait(driver, 15).until(EC.url_changes)
            log.info(f'urlchanged. should to to next page')
            try:
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'popover-x')))
                driver.find_element_by_id('popover-x').find_element_by_xpath('.//a').click()
                log.info('closed popup')                         
            except:
                log.info('no popup to close')
            log.info('next button clicked')
            lastPage = False
            log.info('last page is false')
            page_num += 1
        except:
            log.info(f'No next button to click after {page_num}. finished getting postings')
            lastPage = True
            log.info(f'lastpage is set to true')

    log.info('finished getting postings, closing window')
    log.info(f'total pages: {page_num}\tTotal postings: {total_postings}')
    driver.close()

    #create header in csv
    file_handel.createCsv('testFile.csv','w',job)

    #create rows in csv
    for job in jobList:
        file_handel.addCsvRows('a',job)

if __name__ == "__main__":
    main()
print('Done!!!')

