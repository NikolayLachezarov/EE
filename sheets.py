import gspread
import math
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/spreadsheets"]

key = "AIzaSyDbkSn2JXz2pFzQ3CSwXwVAl9wZfw_15j0"
# google sheets api

creds = ServiceAccountCredentials(key, scope)

client = gspread.authorize(creds)

#sheet = client.open("EE - python x sheets test").sheet1
