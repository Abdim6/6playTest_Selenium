import configparser

config = configparser.RawConfigParser()
config.read("./Configuration/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url
    
    @staticmethod
    def getUserEmail():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getUserPassword():
        pwd = config.get('common info','password')
        return pwd

