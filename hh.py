# coding utf-8
import requests
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
resume_id = ''
access_token = ''
url = 'https://api.hh.ru/resumes/'+resume_id+'/publish'
headers ={'User-Agent': 'pvlt(pvlt.job@gmail.com)', 'Authorization': 'Bearer '+access_token}

r = requests.post(url, headers=headers)