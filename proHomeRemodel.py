from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


def main():
    link_text = ['About Our Company','Contact Us','Home','Map','Samples of Our Work','Testimonials']
    print(f'in main. Loading website!')
    driver = webdriver.Chrome('./chromeDriver')
    driver.get('http://professionalhomeremodeling.com/')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text[0]))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text[5]))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text[4]))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text[3]))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text[1]))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text[2]))).click()
    time.sleep(3)
    driver.close()

if __name__ == '__main__':
    main()
    print(f'Done! Yep! No errors......')