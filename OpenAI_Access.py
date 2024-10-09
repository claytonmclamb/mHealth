import openai 
from dotenv import load_dotenv
import os

class GPT:
    def __init__(self):
        key = self.getAPIKey()
        


    def getAPIKey(self):
        load_dotenv()
        return os.getenv("OPEN_AI_KEY")