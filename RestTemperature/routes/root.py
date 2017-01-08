from bottle import route, request, response, post, get, put, delete
from datetime import datetime
import help
import json

@route('/')
def home():
    return ""

@get('/status')
def listing_handler():
    help.json_header_set(response)
    return  json.dumps({"status":"ok","now": datetime.isoformat(datetime.now())}) 


