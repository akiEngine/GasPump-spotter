from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


def main():

    # Installer le driver Chrome
    service = ChromeService(executable_path=ChromeDriverManager().install())

    # Initialiser le navigateur
    driver = webdriver.Chrome(service=service)

    # Ouvrir la page web spécifiée
    url = 'https://www.example.com'  # Remplacez par l'URL de votre choix
    driver.get(url)

    # Attendre que l'utilisateur fasse des actions
    input("Appuyez sur Entrée après avoir terminé vos actions sur la page...")

    # Récupérer le HTML de la page
    page_html = driver.page_source

    # Afficher le HTML de la page
    print(page_html)

    # Fermer le navigateur
    driver.quit()


if __name__=="__main__":
    main()