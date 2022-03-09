"Ce fichier a pour objectif de localiser les objets de la page OB"
"& une classe qui permetra d'éffectuer la connexion"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class MonCompte:
    btn_gererInfos_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > div > div.r1if2e-1.bqqlfm.sc-1eq6ctx-0.kabTKW > div:nth-child(1) > article > div.gvmwfe-0.o6a45d-0.kfijhj > a"
    btn_modifier_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > div > div.r1if2e-1.bqqlfm.sc-1eq6ctx-0.kabTKW > div:nth-child(1) > article > div > div.gvmwfe-0.o6a45d-0.kfijhj > button"
    textbox_firstname_id = "firstName"
    textbox_lastname_id = "lastName"
    btn_valider_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > div > div.r1if2e-1.bqqlfm.sc-1eq6ctx-0.kabTKW > div:nth-child(1) > article > form > div.gvmwfe-0.o6a45d-0.kfijhj > button.sc-1esye45-2.bTcnKU.o6a45d-1.hCltVO.is-primary"
    
    def __init__(self, driver):
        self.driver = driver
    
    def clickgenerInfo(self):
        self.driver.find_element(By.CSS_SELECTOR,self.btn_gererInfos_CSS).click()

    def clickModifier(self):
        self.driver.find_element(By.CSS_SELECTOR,self.btn_modifier_CSS).click()

    def setPrenom(self, prenom):
        self.driver.find_element(By.ID,self.textbox_firstname_id).clear()
        time.sleep(1)
        self.driver.find_element(By.ID,self.textbox_firstname_id).send_keys(prenom)

    def setNom(self, nom):
        self.driver.find_element(By.ID,self.textbox_lastname_id).clear()
        self.driver.find_element(By.ID,self.textbox_lastname_id).send_keys(nom)

    def clickValider(self):
        self.driver.find_element(By.CSS_SELECTOR,self.btn_valider_CSS).click()

  