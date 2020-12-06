# for automating chrome importing selenium
from selenium import webdriver
from selenium.webdriver.common.by import By  # for locating elements
from selenium.webdriver.support import expected_conditions as ec  # condition that wait for element
from selenium.webdriver.support.ui import WebDriverWait  # for wait if condition is not fulfilled

# python


import time  # for waiting

print('Watch the details you enter are correct, else this program will fail')
username_input = input('type your username >> ')
password_input = input('type your password >> ')
traget_username_input = input('type username of the person you want to send message(username) >> ')
message = input('What message you want to send >> ')
times_of_message = int(input('how many time you want to send the message >> '))


driver = webdriver.Chrome(executable_path="path\\ to \\chromedriver.exe")

# creating waiting element
wait = WebDriverWait(driver, 15)

# opening instagram
base_url = "https://instagram.com"
driver.get(base_url)

username = username_input
password = password_input

# filling the information
element = wait.until(ec.element_to_be_clickable((By.NAME, 'username')))
element.send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('//button[@type="submit"]').click()

# Save password page
element = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
element.click()

# turn on notification page
element = wait.until(ec.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]')))
element.click()

# going to traget user profile
traget_username_url = base_url + f'/{traget_username_input}'
driver.get(traget_username_url)

# clicking on the message button
element = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Message')]")))
element.click()

# for loading the screen
element = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/button[2]')))

i = 0
while i != times_of_message:
    i += 1
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()