"Ce fichier a pour objectif de localiser les objets de la page OB"
"& une classe qui permetra d'éffectuer la connexion"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class LoginmaPage:
    textbox_username_id = "email"
    textbox_password_id = "password"
    # button_login_CSS_Selector = 'body > div:nth-child(9) > div > div > div > div > div.izd9z0-4.jQonvK > form > button > span > span > span'
    button_login_xml = "/html/body/div[3]/div/div/div/div/div[2]/form/button"
    button_inscription = "body > div:nth-child(9) > div > div > div > div > div.izd9z0-5.jhrtwX > div > a"
    email_inscription ="email"
    pwd_inscription ="password"
    button_inscrire_new = "body > div:nth-child(9) > div > div > div > div > div.izd9z0-4.jQonvK > div.sc-1skm6pc-0.kosLNi.kqtu9n-2.hsHvHs > form > div.sc-1skm6pc-1.dkVizr > button"
    liste_genre = "gender"
    section_age = "birthdate"
    button_terminer = "body > div:nth-child(9) > div > div > div > div > div.izd9z0-4.jQonvK > div > form > div.sc-1skm6pc-1.dkVizr > button"

    # link_logout_xpath = '//*[@id="post-9"]/div/div/nav/ul/li[6]/a'
    
    def __init__(self, driver):
        self.driver = driver
    
    def setUsername(self, username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
        
    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
        
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xml).click()

    def clickInscription(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_inscription).click()

    def setemail(self,email):
        self.driver.find_element(By.ID,self.email_inscription).clear
        self.driver.find_element(By.ID,self.email_inscription).send_keys(email)

    def setpwd(self,pwd):
        self.driver.find_element(By.ID,self.pwd_inscription).clear
        self.driver.find_element(By.ID,self.pwd_inscription).send_keys(pwd)

    def clickInscrire(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_inscrire_new).click()
 
    def choixGenre(self):
        elem = self.driver.find_element(By.ID,self.liste_genre)
        drp = Select(elem)
        drp.select_by_index(1)
       
    def setAge(self, age):
        self.driver.find_element(By.ID,self.section_age).click() 
        self.driver.find_element(By.ID,self.section_age).send_keys(age)
  
    def ClickTerminer(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_terminer).click() 

    # def clickLogout(self):
    #     self.driver.find_element(By.XPATH,self.link_logout_xpath).click()


        