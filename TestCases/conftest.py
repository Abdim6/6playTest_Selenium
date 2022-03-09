
from random import random
from selenium import webdriver
import pytest
import string

"un fixture qui permet de se lancer l'app et faire la deconnexion"
@pytest.fixture
def setup_4():
    driver=webdriver.Chrome()
    print("")
    print("Nous utilisons Chrome ......")
    
    driver.implicitly_wait(3)
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture
def setup_3():
    driver=webdriver.Chrome()
    print("")
    print("Nous utilisons Chrome ......")
    # driver.implicitly_wait(3)
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture
def setup_2():
    driver=webdriver.Chrome()
    print("")
    print("Nous utilisons Chrome ......")
    driver.maximize_window()
    return driver

"La commande pour lancer le test selon le browser : "
@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver=webdriver.Chrome()
        print("")
        print("Nous utilisons CHROME ......")
    elif browser == "firefox":
        driver=webdriver.Firefox()
        print("")
    else:
        driver=webdriver.Safari()
        print("")
        print("Nous utilisons IE ......")
    driver.maximize_window()
    return driver

def pytest_addoption(parser):   #this will ger rhe value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #this will return the browser value to setup method
    return request.config.getoption("--browser")

##################### Pytest HTML Report ########################

"Ceci est UNIQUEMENT des paramètrages dans le rapport d'exécution HTML"
#pytest -v -s TestCases/test_IDenBoucle.py -n=2 --html=Reports/reports.html 

"It is hook for adding environment info to HTML Reports"
def pytest_configure(config):
    config._metadata['Project Name'] = '6 play'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Abdi'

"It is hook for delete/Modify Environment info to HTML Report"
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

def pytest_html_report_title(report):
    report.title = "My very own title!"

# "creer une fonction teardown//amuse toi avec ou sans fixture //avec les drive"
# # @pytest.fixture
# def tear_down():
#     driver=setup
#     driver.quit()


# "Faire une classe qui permet de realiser une bne structure de set up et tearndown"
# @pytest.fixture 
# class TestClass :
#     @classmethod
#     def setup_class(cls):
#         self.driver=webdriver.Chrome()
#         print("")
#         print("Nous utilisons Chrome ......")
#         self.driver.maximize_window()

#     @classmethod
#     def teardown_class(cls):
#         self.driver.quit()


#     def teset_method(self, method):
#         #saisir l'URL + connexion
#         pass

#     def teardown_method(self, method):
#         #deconnexion user 
#         pass


# "fonction qui génère les email randoms"
# def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))