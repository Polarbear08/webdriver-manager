import os
import shutil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

custom_path = f"{os.path.dirname(os.path.realpath(__file__))}\\webdriver"
driver_path = f"{os.path.dirname(os.path.realpath(__file__))}\\target"

if not os.path.isdir(driver_path):
    os.mkdir(driver_path)
if not os.path.isdir(custom_path):
    os.mkdir(custom_path)

def copyDriverToTargetDir(source: str, destination: str):
    shutil.copy(source, destination)

# chrome
chrome_driver_path = ChromeDriverManager(path=custom_path).install()
copyDriverToTargetDir(chrome_driver_path, driver_path)
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)
chrome_driver.get('https://www.google.com')
chrome_driver.quit()

# firefox
gecko_driver_path = GeckoDriverManager(path=custom_path).install()
copyDriverToTargetDir(gecko_driver_path, driver_path)
gecko_driver = webdriver.Firefox(executable_path=gecko_driver_path)
gecko_driver.get('https://www.google.com')
gecko_driver.quit()

# Edge
edge_driver_path = EdgeChromiumDriverManager(path=custom_path).install()
copyDriverToTargetDir(edge_driver_path, driver_path)
edge_driver = webdriver.Edge(executable_path=edge_driver_path)
edge_driver.get('https://www.google.com')
edge_driver.quit()

# IE
ie_driver_path = IEDriverManager(path=custom_path).install()
copyDriverToTargetDir(ie_driver_path, driver_path)
ie_driver = webdriver.Ie(ie_driver_path)
ie_driver.get('https://www.google.com')
ie_driver.quit()

