import os
from pprint import pprint
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()
username = os.getenv("LINKEDIN_USERNAME")
password = os.getenv("LINKEDIN_PASSWORD")


class LinkedInParser:
    def __init__(self, user_login: str, user_password: str):
        self.login = user_login
        self.password = user_password
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/113.0.0.0 Safari/537.36"
        })

        if self.login_page():
            print("Авторизація успішна.")
        else:
            raise Exception("Не вдалось авторизуватись.")


    def login_page(self) -> bool:
        login_url = "https://www.linkedin.com/login"
        submit_url = "https://www.linkedin.com/checkpoint/lg/login-submit"

        response = self.session.get(login_url)
        if response.status_code != 200:
            print("Помилка при завантаженні сторінки логіну")
            return False

        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token = soup.find("input", {"name": "loginCsrfParam"})["value"]

        login_data = {
            'session_key': self.login,
            'session_password': self.password,
            'loginCsrfParam': csrf_token,
        }

        login_response = self.session.post(submit_url, data=login_data)
        pprint(login_response.url)
        if login_response.status_code == 200 and "feed" in login_response.url:
            return True
        print("Неправильний логін або пароль")
        return False


try:
    parser = LinkedInParser(username, password)
except Exception as e:
    print(f"Ошибка: {e}")
