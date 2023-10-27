import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6570374387:AAEbb8O7StFdzGBrawhc1vqvcDBtLdmdZ7E")
      API_ID = int(os.environ.get("APP_ID", "26852980"))
      API_HASH = os.environ.get("API_HASH", "b69a1ec7ff063aa1a4d1955238ad47c9")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "bookuploadingbot")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 123476535 )) 
      DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://syedamanhusain:<syedamanhusain>@cluster0.k009uml.mongodb.net/?retryWrites=true&w=majority")
