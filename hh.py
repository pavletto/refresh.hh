#!/usr/bin/env python

# coding utf-8
import sys
import requests
import logging
import time
import pynotify

if __name__ == '__main__':
    def sendmessage(title, message):
        pynotify.init("Test")
        notice = pynotify.Notification(title, message)
        notice.show()
        return

    def sendRequest(): 
        if len(sys.argv) != 3:
            print >> sys.stderr, 'Usage: %s <file with token> <resume id>' % (sys.argv[0],)
            exit(1)
        i =  0
        resume_id = sys.argv[2]
        access_token = sys.argv[1]
        LOG_FILENAME = 'hh.log'
        logging.getLogger("requests.packages.urllib3")
        logging.propagate = True
        logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG, format=u'%(levelname)-8s [%(asctime)s]  %(message)s')
        logTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        url = 'https://api.hh.ru/resumes/'+resume_id+'/publish'
        headers ={'Authorization': 'Bearer '+access_token}

        r = requests.post(url, headers=headers)
        logging.debug('Got response from server: %s', repr(r.text))
       
        if r.status_code == 429:
            sendmessage('Error','Token TTL has expired. Get new token on https://dev.hh.ru/admin/')
            i += 1
            time.sleep(60)
            sendRequest()
        if r.status_code == 403:
            sendmessage('Error','Token TTL has expired. Get new token on https://dev.hh.ru/admin/')
        if r.status_code == 200:
            sendmessage('Success', 'Your resume https://hh.ru/resume/' + resume_id + ' is update')
    sendRequest()
