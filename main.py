from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройки Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Скрываем автоматизацию
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://bbc12.ru/?date=26052025")

try:
    # Ожидаем загрузки плеера (может быть iframe)
    wait = WebDriverWait(driver, 15)

    # Проверяем, есть ли iframe с плеером
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    if iframes:
        print("Переключаемся на iframe...")
        driver.switch_to.frame(iframes[0])

    # Ждём появления кнопки меню (три точки)
    menu_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".playerjs-button-menu, .playerjs-button[title='Меню']"))
    )
    menu_button.click()
    print("Меню открыто")

    # Ждём кнопку "Скачать" и кликаем
    download_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'playerjs-context-item') and contains(text(), 'Скачать')]"))
    )
    download_button.click()
    print("Скачивание началось")

    # Ждём 10 секунд (или пока файл не появится в папке)
    time.sleep(10)

except Exception as e:
    print(f"Ошибка: {e}")
finally:
    driver.quit()