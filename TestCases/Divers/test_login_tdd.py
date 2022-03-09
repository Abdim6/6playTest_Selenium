"Ici est un cdt de connexion - lié aux objets de la page loginPage."

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginmaPage
from PageObjects.HomePage import HomePage
import time
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
# from testCases import conftest 


"ce bloc devrait se trouver dans un setup, en commun pour tous les tests"
class Test_002_Login:
    # baseURL = "https://www.6play.fr/"
    # # baseURL2 = "http://demostore.supersqa.com/my-account/"
    # username = "abdi.bilehm6@gmail.com"
    # password = "bonjourA1"
    
    path = "./testData/LoginData.xlsx"
    baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUserEmail()
    # password = ReadConfig.getUserPassword()
    # username = XLUtils.readData(path,"Feuil1",3,3)
    # password = XLUtils.readData(path,"Feuil1",3,4)
    logger = LogGen.loggen()
    logger.info("***************** DEBUT - Test_002_Login ****************")
    logger.info("***************** vérification du titre de la page d'accueil ****************")

    def test_homePageTitle(self,setup_2):
       
        self.driver = setup_2
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
        
        "Cliquer sur la modale + cliquer sur le bouton mon compte"
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
        print("")
        print("Le user est connecté - TOUT EST OK")
        self.hp.clickHomeBtn()
        time.sleep(2)
        self.hp.checkObjetHomePage()
        time.sleep(2)
        print("Home page est affichee - TOUT EST OK")
        self.driver.save_screenshot("./screenshot/page_title_0.png")
        self.driver.close()
        self.logger.info("***************** FIN - Test_002_Login ****************")
        # conftest.tear_down()
        
      
#--- -- 
        # self.nbLigne = XLUtils.getRowCount(self.path, "Feuil1")
        # print("Le nombre de lignes dans le fichier excel est : "+self.nbLigne)
        # for nb in range(2, self.nbLigne+1):
        #     self.username = XLUtils.readData(self.path,"Feuil1",nb,3)
        #     self.pwd = XLUtils.readData(self.path,"Feuil1",nb,4)
        #     self.exp = XLUtils.readData(self.path,"Feuil1",nb,5)


        #--- -- 

        #    #--- -- 
        # import pdb; pdb.set_trace()
        # self.nbLigne = XLUtils.getRowCount(self.path, "Feuil1")
        # print("Le nombre de lignes dans le fichier excel est : ",self.nbLigne)
        # for nb in range(2, self.nbLigne+1):
        #     self.username = XLUtils.readData(self.path,"Feuil1",nb,3)
        #     self.password = XLUtils.readData(self.path,"Feuil1",nb,4)
        #     self.exp = XLUtils.readData(self.path,"Feuil1",nb,5)
        # #--- --    