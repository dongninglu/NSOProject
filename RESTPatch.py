'''
Created on Apr 30, 2022

@author: dongn
'''

from requests.auth import HTTPBasicAuth
import requests
import pprint
import json

class RESTPatch :
    '''
    classdocs
    '''
    m_data = '{ "loopback-service:loopback-service": [ { "name": "test2", "device": "dist-rtr01", "dummy": "1.1.1.1"} ] }'
    m_newname = "foobar"
    m_headers = { 'Content-Type': 'application/yang-data+json;charset=utf-8'}


    def __init__(self, username, passwd):
        '''
        Constructor
        '''
        self.usrname = username
        self.passwd = passwd
        
        
    def createLoopServices (self, dataString): 
        data = json.loads(dataString)
        results = data['tailf-ncs:device']

        if len(results) > 0:
    #        print("results[0].keys()--- 55555   ")
    #        print(results[0].keys())
            i=0 
            servicename = []
            
            for result in results:
                
                device_name = result['name']
                print("------------  REST PATCH  --- 111111111--------------  " +  result['name'] )
                my_updatedData = json.loads(self.m_data)
                my_value= my_updatedData['loopback-service:loopback-service']
                my_list= my_value[0];
                
                servicename.append(self.m_newname+str(i))
                
                print ("---------------REST PATCH    222222222----------------")
                pprint.pprint(servicename)
                pprint.pprint(my_list)
    #            pprint.pprint(my_updatedData)
    #            print ("original    "  )
                my_updatedData['loopback-service:loopback-service'][0].update({'device': device_name}) 
                my_updatedData['loopback-service:loopback-service'][0].update({'name': self.m_newname+str(i)})
                my_newdatastr = json.dumps(my_updatedData)
    
            
                r = requests.patch('https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service', 
                                   auth=HTTPBasicAuth(self.usrname, self.passwd), headers=self.m_headers,  data=my_newdatastr,verify=False)
                i = i+1
                if r.status_code in range(400,500) :
                    print("----------- error creating loopback services ------")
                    print(r.status_code)
                    
            return servicename
                
