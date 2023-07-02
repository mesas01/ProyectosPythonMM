from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

url = "https://sanjose.edu.co/"
session = HTMLSession()

product_page = session.get(url)
found = product_page.html.find("#ssb-btn-2")


def hay_acceso():

    while True:
        se_puede = session.get(url)
        buy_zone = se_puede.html.find("#menu-menu-principal")
        if len(buy_zone) > 0:
            print("se puede acceder")
            return True
        else:
            print("no se pude acceder")
        sleep(30)


def main():
    hay_acceso()


if __name__ == "__main__":
    main()
