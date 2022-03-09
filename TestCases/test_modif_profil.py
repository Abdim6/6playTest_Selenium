"Ici est un cdt de connexion - lié aux objets de la page loginPage."

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginmaPage
from PageObjects.HomePage import HomePage
from PageObjects.MonCompte import MonCompte
import time
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


"ce bloc devrait se trouver dans un setup, en commun pour tous les tests"
class Test_003_Login:
    "Données en DUR"
    baseURL = "https://www.6play.fr/"
    username = "abdi.bilehm6@gmail.com"
    password = "bonjourA1"
    # logger = LogGen.loggen()

    @pytest.mark.mesTests
    def test_homePageTitle(self,setup_2):
        self.driver = setup_2
        self.driver.get(self.baseURL)
       
        "Cliquer sur la modale + mon compte"
        self.hp=HomePage(self.driver)
        self.hp.clickaccepterTCF() 
        time.sleep(2)

        self.hp.clickMonCompteBtn() 
        time.sleep(2)

        "Saisi des ID dans OB pour se connecter" 
        self.lp=LoginmaPage(self.driver) 
        self.lp.setUsername(self.username)
        time.sleep(1)
        self.lp.setPassword(self.password)
        time.sleep(1)
        self.lp.clickLogin()   
        time.sleep(2)

        "Modifier les données de User"
        self.mn = MonCompte(self.driver)
        self.mn.clickgenerInfo()
        time.sleep(1)
        self.mn.clickModifier()
        time.sleep(1)
        self.mn.setPrenom("abdi")
        time.sleep(1)
        self.mn.setNom("Bileh")
        time.sleep(2)
        self.mn.clickValider()
        time.sleep(5)
        "Retour sur la home page + ajout de programme dans le favoris"
        self.hp.clickHomeBtn()
        time.sleep(1)
        self.hp.clickSurRecherche()
        time.sleep(1)
        self.hp.clickDernierReplay()
        time.sleep(3)
        self.hp.clickAjoutFavoris()
        time.sleep(5)
        self.hp.clickMonCompteBtn()
        time.sleep(1)
        self.hp.clickdeco()
        time.sleep(3)

        print("Le parcours est complet - fermeture de driver .... ")
        self.driver.close()

        