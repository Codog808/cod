from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

def shorter_EC(driver_wait, locator, indentier):
    return driver_wait.until(EC.visibility_of_element_located((locator, indentier)))

def main(test=False):
    service = ChromeService(ChromeDriverManager().install())
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("window-size=720,900")
    options.add_argument("memory-saver=True")
    chrome_driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(chrome_driver, 10)
    if test:
        chrome_driver.get("https://www.google.com")
    print("Success in Chrome Driver Initalization...")
    return chrome_driver, wait

if __name__ == "__main__":
    main(True)
