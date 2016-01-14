# coding utf-8
import requests
import logging

resume_id = ''
access_token = ''
LOG_FILENAME = 'hh.log'
logging.getLogger("requests.packages.urllib3")
logging.propagate = True
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG, format=u'%(levelname)-8s [%(asctime)s]  %(message)s')

url = 'https://api.hh.ru/resumes/'+resume_id+'/publish'
headers ={'Authorization': 'Bearer '+access_token}

r = requests.post(url, headers=headers)