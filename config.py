import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23353706"))
    API_HASH = os.environ.get("API_HASH", "c4111548b30bad77d59931b8e76d4f31")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6097665193:AAGEbTXDkfouo5m-BhY1JjQkwS9kMQsEFNs")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "776367418")                             
    DATABASE_URI = os.environ.get("mongodb+srv://forwardbot:forwardbot@cluster0.wqqotze.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQAm1xZFiFiI2siRf1z3zsNDj9Q7g6EdxfTjSSO6zfUyFrQM7ICCv1XmFlvjXI1S4fflS9c7pnZ62HyOHZbFYHND8Etjl7vkFV5CUQXAE09ns8S-izpnMc6sqJ6ESPTrW44LopZ1w7Gr6lkYamFTIWGjGnleymZeDlGcM_DcoJ9InWQ6oRPR1GShcGxiVJlqHEre0Ombiqwi6YDO5TQoPq7OuUVpe7VD89FLeMVTOYOo6YAGb60USf02_L1zf6pckMGYE7rP63wZatprR5Z7Sw49QqqYEJV-hGshj4h0IUnEhBq9ipx-Sk3FoaodsjYvE2vAdbn-SXtKwQsbguPC3c71LkZtOgA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001933583960"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "forward1703_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
