#!/usr/bin/env python

# coding utf-8
import sys
import requests
import logging

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print >> sys.stderr, 'Usage: %s <file with token> <resume id>' % (sys.argv[0],)
        exit(1)
    resume_id = sys.argv[2]
    access_token = open(sys.argv[1]).read().strip()
    LOG_FILENAME = 'hh.log'
    logging.getLogger("requests.packages.urllib3")
    logging.propagate = True
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG, format=u'%(levelname)-8s [%(asctime)s]  %(message)s')

    url = 'https://api.hh.ru/resumes/'+resume_id+'/publish'
    headers ={'Authorization': 'Bearer '+access_token}

    r = requests.post(url, headers=headers)
    logging.debug('Got response from server: %s', repr(r.text))
