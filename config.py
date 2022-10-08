import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1766902841:AAEx_oFZSOUAkUV50Uze_blRVuhlFQxsuI4")
SUDO = int(os.environ.get("SUDO", "1593675355"))
HEROKU = os.environ.get("HEROKU", "")
APP_URL = "https://"+ HEROKU +".herokuapp.com/" + BOT_TOKEN
