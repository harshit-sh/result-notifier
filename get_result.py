import selenium
from selenium import webdriver
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
import os
import sys
import time

browser = webdriver.PhantomJS()

url = 'http://iiitb.campusmetalink.com/cml/pages/selfService/CssAssignmentReg.jsf'

browser.get(url)

site_id = 'iiitb'
#username = 'IMT2012019'

password = os.environ.get("password")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

client = TwilioRestClient(account_sid, auth_token)
twilio_no = os.environ.get("twilio_no")
your_no = os.environ.get("your_no")

#term = '2016TERM2'

xpaths = {'site_id' : "//input[@name='recqIDId:j_id15']", \
        'username' : "//input[@name='recqIDId:j_id17']", \
        'password': "//input[@name='recqIDId:j_id19']",
        'submitButton': "//input[@name='recqIDId:j_id25']",\
        'term': "//input[@name='scheduleForm:j_id113']"}

no_of_rows = 0

while no_of_rows != 5:
 	browser.find_element_by_xpath(xpaths['site_id']).send_keys(site_id)
	browser.find_element_by_xpath(xpaths['username']).send_keys(username)
	browser.find_element_by_xpath(xpaths['password']).send_keys(password)
	browser.find_element_by_xpath(xpaths['submitButton']).click()
	time.sleep(10)
	browser.find_element_by_link_text("Assignment & Grades").click();
	time.sleep(10)
	browser.find_element_by_id("scheduleForm:coltrm").send_keys(term)
	browser.find_element_by_link_text("Search").click();
	time.sleep(10)

	table = browser.find_elements_by_xpath("//table[@id='scheduleForm:svres']/tbody/tr")
	no_of_rows = len(table)

 	if no_of_rows > 3 and no_of_rows <= 5:
    		message = client.messages.create(body="Check Result!",
                	to= your_no,    # Replace with your phone number
                	from_= twilio_no # Replace with your Twilio number
        	)
  	browser.find_element_by_link_text("logout").click();
  	if no_of_rows == 5:
  		sys.exit(1)
	time.sleep(900)