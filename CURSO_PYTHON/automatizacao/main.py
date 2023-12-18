import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    TIME_TO_WAIT = 10
    #Ex:
    options = ()
    browser = make_chrome_broswer(*options)

    #Abrir o navegador
    browser.get('https://www.google.com.br/')

    # Esperar até que apareça certo elemento
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.ID, 'input')
        )
    )
    search_input.send_keys('Hello, world.')

    
    time.sleep(TIME_TO_WAIT)
