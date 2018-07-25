#!/usr/bin/env python

# coding utf-8
import sys
import requests
import logging
import time
import os
import platform


def sendmessage(title, message):
    platform_name = platform.system()
    if platform_name == 'Linux':
        os.system('notify-send "%s" "%s"' % (title, message))
    if platform_name == 'Darwin':
        os.system(
            """osascript -e 'display notification "%s" with title "%s"' """
            % (message, title)
        )
    return


def sendRequest():
    if len(sys.argv) != 3:
        print >> sys.stderr, 'Usage: %s <token> <resume id>' % (
            sys.argv[0],)
        exit(1)
    resume_id = sys.argv[2]
    access_token = sys.argv[1]
    LOG_FILENAME = 'hh.log'
    logging.getLogger("requests.packages.urllib3")
    logging.propagate = True
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,
                        format=u'%(levelname)-8s [%(asctime)s]  %(message)s')
    logTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    url = 'https://api.hh.ru/resumes/'+resume_id+'/publish'
    headers = {'Authorization': 'Bearer '+access_token}

    r = requests.post(url, headers=headers)
    logging.debug('Got response from server: %s', repr(r.text))

    if r.status_code == 429:
        sendmessage(
            'Error', 'You are trying to update your resume too often')
    if r.status_code == 403:
        sendmessage(
            'Error', 'Token TTL has expired. Get a new token on https://dev.hh.ru/admin/')
    if r.status_code == 200:
        sendmessage(
            'Success', 'Your resume was updated')


if __name__ == '__main__':
    sendRequest()
