"Ici est un cdt de connexion - lié aux objets de la page loginPage."

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginmaPage
from PageObjects.HomePage import HomePage
import time
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
# from testCases import conftest 


"ce bloc devrait se trouver dans un setup, en commun pour tous les tests"
class Test_001_Login:
    "Données en DUR"
    baseURL = "https://www.6play.fr/"
    # baseURL2 = "http://demostore.supersqa.com/my-account/"
    username = "abdi.bilehm6@gmail.com"
    password = "bonjourA1"
    logger = LogGen.loggen()
    logger.info("***************** DEBUT - Test_001_Login ****************")
    logger.info("***************** vérification du titre de la page d'accueil ****************")

    def test_homePageTitle(self,setup_2):
        self.driver = setup_2
        self.driver.get(self.baseURL)
       
        "Cliquer sur la modale + mon compte"
        self.hp=HomePage(self.driver)
        self.hp.clickaccepterTCF() 
        time.sleep(2)

        self.hp.clickMonCompteBtn() 
        time.sleep(2)

        "Saisi des ID dans OB"
        "le self.driver en paramètre ici, doit faire reference à celui mis dans le __init__ de logmapage()"
        self.lp=LoginmaPage(self.driver) 
        self.lp.setUsername(self.username)
        time.sleep(1)
        self.lp.setPassword(self.password)
        time.sleep(1)
        self.lp.clickLogin()   
        time.sleep(2)

        "Vérification de la page mon compte"
        act_title = self.driver.title
        print("Le titre de la page est : " + act_title)
        # print(act_title)
        time.sleep(2)
        if act_title == "6play : Mon espace personnel":
            self.logger.info("***************** Test titre de la page OK ****************")
            self.hp.clickdeco()
            assert True
            # self.driver.close()
        else:
            print(act_title)
            self.driver.save_screenshot("./screenshot/page_title_0.png")
            self.logger.error("***************** Test titre de la page KO ****************")
            self.driver.close()
            assert False
            
        self.driver.refresh()
        time.sleep(2)
        print("Home page est affichee - TOUT EST OK")
        self.logger.info("***************** FIN - Test_001_Login ****************")
        self.driver.close()

        