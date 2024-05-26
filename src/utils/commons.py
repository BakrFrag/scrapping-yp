import os
from dotenv import load_dotenv

load_dotenv()

def get_config(name:str):
    """
    get the config variable and read it as enviroment variable
    """
    return os.environ.get(name)

