# -E-commerce_Site_Monitoring_Architecture
Code Readme
This code is designed to extract information from Instagram search results based on a specified business category. It utilises the Selenium and BeautifulSoup libraries in Python to automate the process.
Prerequisites
Before running this code, make sure you have the following dependencies installed:
	•	Selenium
	•	BeautifulSoup
	•	pandas
Also, you need to download the Chrome driver compatible with your operating system and update the path to the driver file in the code.
Usage
	1	Open the code file in a Python environment or editor.
	2	Update the path to the Chrome driver on your system: driver = webdriver.Chrome('/Users/kobby/Desktop/chromedriver'). Make sure the path points to the correct location of the Chrome driver file.
	3	Specify the business category you want to search for by assigning a value to the business_category variable.
	4	Provide your Instagram username and password in the respective input boxes: username.send_keys('your_username') and password.send_keys('your_password').
	5	Run the code.
Output
The code will open the Instagram website and log in with the provided credentials. It will then search for the specified business category and extract information from the search results, including the business name, Instagram username, bio link, and image link. The extracted data will be saved in a CSV file named "ig_business.csv" at the specified path: df.to_csv('/Users/Kobby/Desktop/ig_business.csv').
Note: The code assumes a specific HTML structure of the Instagram website and may need adjustments if the structure changes in the future.
Please ensure you comply with Instagram's terms of service and usage policies when using this code for web scraping purposes.
