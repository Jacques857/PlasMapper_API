from abc import ABC
from decouple import config

class Utility(ABC): # abstract class
    # Returns the value of the specified key in .env
    def getEnvValue(key):
        return config(key)