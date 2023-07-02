import random

from requests_html import HTMLSession
from selenium.webdriver.chrome import webdriver

from speak_and_listen import speak, hear_me


def main():
    # speak("bienvenido al precio justo, vamos a intentar adivinar el precio de algunos productos")
    session = HTMLSession()
    main_site = session.get("https://sanjose.edu.co/")

    #categories = main_site.html.find(".icon alk-icon-categories")
    #category = random.choice(categories)


if __name__ == "__main__":
    main()
