'''
Created on Apr 30, 2022

@author: dongn
'''

from requests.auth import HTTPBasicAuth
import requests
import pprint
import json

class RESTGet :
    '''
    classdocs
    '''
    
    m_params = {'fields':'name'}
    m_headers = { 'Content-Type': 'application/yang-data+json;charset=utf-8'}
    base_url = f"https://10.10.20.50:8888"
    endpoint_path_data = f"/restconf/data"
    endpoint_path_devices = f"{endpoint_path_data}/tailf-ncs:devices"
    endpoint = f"{base_url}{endpoint_path_devices}/device"

    def __init__(self, username, passwd):
        '''
        Constructor
        '''
        
        r = requests.get(self.endpoint,auth=HTTPBasicAuth(username,passwd),headers=self.m_headers, params=self.m_params,verify=False )
        if r.status_code in range(200, 299):
            data = r.json()
            self.dataString = json.dumps(data)

     
    def getDataResults(self):
        pprint.pprint(self.dataString)
        print("----------getDATAResults -----------------")

        return self.dataString  