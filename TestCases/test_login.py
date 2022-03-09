"Ici est un cscénario qui test la connexion - Vérification sur un objets de la page loginPage."

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
    # baseURL = "https://www.6play.fr/"
    # # baseURL2 = "http://demostore.supersqa.com/my-account/"
    # username = "abdi.bilehm6@gmail.com"
    # password = "bonjourA1"
    
    #récuperation de données depuis config.ini
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("***************** DEBUT - Test_001_Login ****************")
        self.logger.info("***************** vérification du titre de la page d'accueil ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # print(act_title)
        time.sleep(2)
        if act_title == "6play, regardez des programmes TV en Replay ou en Direct":
            self.logger.info("***************** Test titre de la page OK ****************")
            assert True
            # self.driver.close()
        else:
            print(act_title)
            self.driver.save_screenshot(".\screenshot\\"+"page_title_1.png")
            self.logger.error("***************** Test titre de la page KO ****************")
            assert False
            # self.driver.close()
        
        "Cliquer sur la modale"
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

        # self.hp.clickdeco()

        print("")
        print("Le user est connecté - TOUT EST OK")
        self.hp.clickHomeBtn()
        time.sleep(2)
        self.hp.checkObjetHomePage()
        time.sleep(2)
        print("Home page est affichee - TOUT EST OK")
        self.driver.save_screenshot("./screenshot/page_title_0.png")
        self.logger.info("***************** FIN - Test_001_Login ****************")
        self.driver.close()
        # conftest.tear_down()
        
        


    # def test_login(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     time.sleep(1)
    #     self.driver.get(self.baseURL2)
    #     time.sleep(1)
    #     self.lp=LoginmaPage(self.driver)
    #     self.lp.setUsername(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()   
    #     time.sleep(2)
    #     act_title = self.driver.title

    #     # import pdb; pdb.set_trace()

    #     if act_title == "My account – DemoStore":
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot("\\screenshot\\"+"page_title_2.png")
    #         self.driver.close()
    #         assert False


