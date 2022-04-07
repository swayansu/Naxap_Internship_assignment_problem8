from selenium import webdriver
import time

# Intializing the webdriver and specifying we are using the Chrome driver
web = webdriver.Chrome()

# to open the desired URL
web.get('https://www.bookchor.com/Contact#')

time.sleep(2)

# to initialize the field values like email, fullname, message 

FullName = 'Your full name'
fm = web.find_element_by_xpath('//*[@id="contacts-name"]')
fm.send_keys(FullName)

emailId = 'your email@gmail.com'
em = web.find_element_by_xpath('//*[@id="contacts-email"]')
em.send_keys(emailId)

messageHere = 'Your message goes here...'
msg = web.find_element_by_xpath('//*[@id="contacts-message"]')
msg.send_keys(messageHere)

time.sleep(5)

# to take the screenshot
web.save_screenshot('ss.png')

submit = web.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[1]/form/button[1]')
submit.click()

'''
  Uncomment the following line if you want to close the browser automatically after the form is submitted
'''

# web.quit()