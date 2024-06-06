from configparser import ConfigParser

def get_config(category,key):
    con = ConfigParser()
    con.read("E:\\sample pytest\\Pytest_OrangeHRM\\Pytest_OrangeHRM\Utility\\config.ini")
    return con.get(category,key) #return here