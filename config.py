import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23353706"))
    API_HASH = os.environ.get("API_HASH", "c4111548b30bad77d59931b8e76d4f31")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6345424142:AAHYTC_CHOjQdgSRqLxiTRvt-m686MjaU84")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "776367418")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://shobitgupta51:Dhruv123@cluster0.wqqotze.mongodb.net/")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQFkWWoAXD7umRadvCrXYrUop0PYFn5iYYcWViUK25-YLoBHdzyaACPZrzGpoKp06cFQyLUu7hUSmIh8AcTR8gX5-6yJtOxeT-931OsBpWWPe1PzFJrvuaMmAH8u8w-LeosX81Z-InNH17rV7zjc670WS4r1Jrgnzkr2a8fnL9MmOwrDDmCBiGqLclDZz06_6K5T9BJ7bdqy9lay3T1MVstdpNw5zuoHv93jhp6JIScKKvIil4ql4a45LWynXcKeSDo_quNL8LhYQexmMDKcnHwKjwOMiD1ZSwEYZpG14Ul_j8ugFgB-N5Q4EiCcnIeWrEWjEB5Ni7hZ_M5eGb-MnsFh-_81_QAAAAAuRm06AA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001933583960"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Dhruv04_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
