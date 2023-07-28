from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Step1: brew install python
# Step2: which python
# Step3: sudo python2.7 -m ensurepip --default-pip
# Step4: sudo pip install selenium 
# Step5: safaridriver --enable
# Step5: Safari - preferences - advance - show develop menu in menu bar
# Step6: Safair - Develop - Allow remote automation
# Step7: write code


driver = webdriver.Safari()

def main():
	try:
		# get website
		driver.get("https://swcloud.io")

		# if we get to the page
		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))

		print driver.get_window_size()
		driver.set_window_size(1300, 1000)
		driver.implicitly_wait(5)
		input_email = driver.find_element_by_name("email")
		input_email.send_keys("XXX")
		input_email = driver.find_element_by_name("password")
		input_email.send_keys("XXX")
		

		time.sleep(3)
		print("start to cilck login")
		# click to login
		driver.find_element_by_xpath('/html/body/div/section/div/div/div/div[2]/form/div/div[4]/button').click();
		# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/div/div/div/div[2]/form/div/div[4]/button"))).click()
		print("finish cilck login")

		time.sleep(10)
		
		# click to check in
		# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/section/div[1]/div/div/a"))).click()

		# time.sleep(30)
		driver.quit()
	except Exception as error:
		print("An exception occurred:", error)
	finally:
		driver.quit()
if __name__ == "__main__":
	main()

