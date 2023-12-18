import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

# chrome_options = webdriver.ChromeOptions()
# chrome_service = Service(executable_path=CHROMEDRIVER_EXC)
# chrome_browser = webdriver.Chrome(
#     service=chrome_service,
#     options=chrome_options,
# )

# chrome_browser.get('https://www.google.com.br/')
# time.sleep(30)


# criou uma função para não ter que configurar toda hora.
def make_chrome_broswer(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    chrome_service = Service(
        executable_path=CHROMEDRIVER_EXC,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )
    return browser

if __name__ == '__main__':
    #Ex:
    options = ()
    browser = make_chrome_broswer(*options)

    browser.get('https://www.google.com.br/')
    time.sleep(10)
