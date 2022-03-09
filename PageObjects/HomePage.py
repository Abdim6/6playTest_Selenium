"Ce fichier a pour objectif de localiser les objets de la home page + la modale TCF"
"& une classe qui permetra d'éffectuer la connexion"
"!!! AVEC UNE CONNEXION EN BOUCLE LOCALISATION AVEC XML FONCTIONNE !!! "

import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class HomePage:
    moncompte_btn_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > header > div > div > nav > div.m4392j-1.imWKGD > ul > li:nth-child(5) > button"
    accepter_btnTCF_CSS = "body > div:nth-child(12) > aside > div > div.suptlw-3.dTtZno > form > div.s9pqpz-4.eGAKcX.sc-18bqyzn-0.gXHDvG > div > button.sc-1esye45-2.dVskuE.sc-1veuio6-0.dktssj.s9pqpz-2.hEklsz.is-primary > span"
    HomeBtn_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > header > div > div > nav > div.m4392j-1.imWKGD > ul > li:nth-child(3)"
    objetHomePage_CSS = "#main > div > section:nth-child(3) > div.y84eg7-0.sc-8pi7if-0.LuxLU > h1"
    recherche_btn_CSS = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > header > div > div > nav > div.m4392j-1.imWKGD > ul > li:nth-child(4) > a"
    button_txt = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > aside > button > span"
    moncompte_btn_xml = '//*[@id="__brk"]/div/div[2]/div[2]/div/header/div/div/nav/div[1]/ul/li[5]/button'
    mesinfo_btn = "#__brk > div > div.n913wo-5.cuyMWW > div.n913wo-4.fCmDdf > div > main > aside > nav > ul > li:nth-child(3) > a > span"
    mesinfo_btn_xml = '//*[@id="__brk"]/div/div[2]/div[2]/div/main/aside/nav/ul/li[3]/a'
    donneesperso_email = "email"
    dernierReplay_CSS = "#page_62209fc7e252e0\.25802620--4443f32c-c6ee-4b72-86e1-8fbeb2625bc8 > div.sc-1jzygab-5.fNJpJi > ul > li:nth-child(1)"
    listReplay_CSS ="#page_62232bab6c0893\.70856363--4443f32c-c6ee-4b72-86e1-8fbeb2625bc8 > div.sc-1jzygab-5.fNJpJi > ul"
    section_replay_class = "sc-1jzygab-5"
    dernierReplay_XPATH = '//*[@id="page_622321a29b68f1.45716632--4443f32c-c6ee-4b72-86e1-8fbeb2625bc8"]/div[1]/ul/li[1]/a/article'
    AjoutFavoris_btn_CSS = "#page_62209efac81c31\.51376685--4f8b12bd-ed93-4057-80fa-211a289dc3a4 > div.qd8avx-0.jwKxkB > div.nei5bm-2.cNRBFu > div.nei5bm-9.fEDJNC > button"

    "ce driver en paramètre d'où vient? - je vois pas trop la logique dernière"
    def __init__(self, driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver, 20)
        
    "Pour cette fonction j'utilise un explicite wait"
    def clickaccepterTCF(self):
        element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.accepter_btnTCF_CSS)))
        # self.driver.find_element(By.CSS_SELECTOR,self.accepter_btnTCF_CSS).click()
        element.click()

    def clickMonCompteBtn(self):
        # self.driver.find_element(By.XPATH,self.moncompte_btn_xml).click()
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.moncompte_btn_xml)))
        element.click()

    def clickHomeBtn(self):
        self.driver.find_element(By.CSS_SELECTOR,self.HomeBtn_CSS).click()
    
    def checkObjetHomePage(self):
        self.driver.find_element(By.CSS_SELECTOR,self.objetHomePage_CSS).is_displayed()

    def clickdeco(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_txt).click()

    def clickMesInfos(self):
        # self.driver.find_element(By.CSS_SELECTOR, self.mesinfo_btn).click()
        self.driver.find_element(By.XPATH, self.mesinfo_btn_xml).click()

    def getdonneesEmail(self):
        monEmail = self.driver.find_element(By.ID, self.donneesperso_email)
        # import pdb; pdb.set_trace()
        return monEmail.get_property("value")

    def clickDernierReplay(self):
        "cette action m'a donné un file à retordre, review et ANALYSE la"
        # actions=ActionChains(self.driver)
        # # import pdb; pdb.set_trace()
        # # section = self.driver.find_elements(By.CLASS_NAME, "section_replay_class")
        # # actions.move_to_element(section)
        # list = self.driver.find_elements(By.CSS_SELECTOR,self.listReplay_CSS)
        # print(list)
        # import pdb; pdb.set_trace()
        # # self.driver.find_element(By.XPATH, self.dernierReplay_XPATH).click()
        liste = self.driver.find_elements(By.CLASS_NAME, "sc-1jzygab-7")
        liste[0].click()
        # print(liste)
        # import pdb; pdb.set_trace()
        
    def clickSurRecherche(self):
        self.driver.find_element(By.CSS_SELECTOR, self.recherche_btn_CSS).click()
     
    def clickAjoutFavoris(self):
        # import pdb; pdb.set_trace()
        btn_ajouter = self.driver.find_elements(By.CLASS_NAME, "oxwymj-0.jtrbaw.sc-1qpa8kx-4.eOyIfE.is-secondary.is-responsive")
        btn_ajouter[0].click()
        # self.driver.find_element(By.CSS_SELECTOR, self.AjoutFavoris_btn_CSS).click()
       

