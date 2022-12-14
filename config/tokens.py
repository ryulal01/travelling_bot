import os
import sys

from dotenv import load_dotenv

load_dotenv()
TOKEN_TG = os.environ.get("TOKEN_TG")
TOKEN_AVIASALES = os.environ.get("TOKEN_AVIASALES")
try:
	BOT_ID = int(TOKEN_TG.split(':')[0])
except:
	print('Видимо нет токена бота в файле .env'
		  'Программа будет остановлена!')

	sys.exit()
