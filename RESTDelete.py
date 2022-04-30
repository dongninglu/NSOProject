'''
Created on Apr 30, 2022

@author: dongn
'''
from requests.auth import HTTPBasicAuth
import requests
import pprint


class RESTDelete(object):
    '''
    classdocs
    '''
    m_endpoint = "https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service="
    m_headers = { 'Content-Type': 'application/yang-data+json;charset=utf-8'}


    def __init__(self, username, passwd):
        '''
        Constructor
        '''
        self.usrname = username
        self.passwd = passwd
        
        
    def delete_loopservices(self, namelist):
        for name in namelist :
            my_delete_endpoint = self.m_endpoint+name
            r = requests.delete(my_delete_endpoint,  auth=HTTPBasicAuth(self.usrname,self.passwd), headers=self.m_headers,verify=False)
            print("----------------------delete -------------------------")
            print(r.url)
            pprint.pprint(r.status_code)
