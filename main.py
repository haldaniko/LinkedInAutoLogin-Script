import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

username = os.getenv("LINKEDIN_USERNAME")
password = os.getenv("LINKEDIN_PASSWORD")


class LinkedInParser:
    def __init__(self, user_login: str, user_password: str):
        self.login = user_login
        self.password = user_password

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)

        if self.login_page():
            print("Авторизація успішна.")
        else:
            self.driver.quit()
            raise Exception("Не вдалось авторизуватись.")

    def login_page(self) -> bool:
        try:
            login_url = "https://www.linkedin.com/login"
            self.driver.get(login_url)

            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.send_keys(self.login)

            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(self.password)

            password_field.send_keys(Keys.RETURN)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "global-nav"))
            )
            return True
        except Exception as e:
            print(f"Помилка авторизації: {e}")
            return False

    def get_profile_image(self) -> str:
        try:
            self.driver.get("https://www.linkedin.com/in/me/")

            img_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    "img.evi-image.ember-view.profile-photo-edit__preview"
                ))
            )

            img_url = img_element.get_attribute("src")
            return img_url
        except Exception as e:
            raise Exception(f"Помилка при отриманні зображення профілю: {e}")

    def close(self):
        self.driver.quit()


try:
    parser = LinkedInParser(username, password)
    profile_image_url = parser.get_profile_image()
    print(f"URL зображженя профілю: {profile_image_url}")
except Exception as e:
    print(f"Помилка: {e}")
finally:
    if 'parser' in locals():
        parser.close()
