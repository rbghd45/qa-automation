from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 크롬 열기
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 사이트 접속
driver.get("https://www.saucedemo.com")
time.sleep(2)

# 로그인
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# 로그인 성공 확인
print("현재 URL:", driver.current_url)

# 상품 목록 확인
products = driver.find_elements(By.CLASS_NAME, "inventory_item")
print("상품 개수:", len(products))

# 첫번째 상품 장바구니 담기
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)

# 장바구니 확인
cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
print("장바구니 수량:", cart.text)

driver.quit()