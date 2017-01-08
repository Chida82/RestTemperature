from bottle import route, request, response, post, get, put, delete
from datetime import datetime
import help
import json
import glob



@get('/temperature')
def get_temperature():
    t_list = read_temperature()    
    help.json_header_set(response)
    #return  json.dumps({"c":t_list[0],"f":t_list[1],"w": datetime.isoformat(datetime.now())})
    return  json.dumps({"c":t_list[0],"w": datetime.isoformat(datetime.now())})


def read_temperature():
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(device_file)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = 0 # temp_c * 9.0 / 5.0 + 32.0
    return temp_c,temp_f

def read_temp_raw(device_file):
   f = open(device_file, 'r')
   lines = f.readlines()
   f.close()
   return lines