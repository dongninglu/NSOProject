'''
Created on Apr 30, 2022

@author: dongn
'''

from RESTDelete import RESTDelete
from RESTGet import RESTGet
from RESTPatch import RESTPatch

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


if __name__ == '__main__':

    username = 'admin'
    passwd = 'admin'    
    get = RESTGet(username, passwd)
    deviceNameList = get.getDataResults()
    
    patch = RESTPatch(username, passwd)
    serviceNames = patch.createLoopServices(deviceNameList)
    
    user_delete = input(" type any key to delete added loopservices .....")
    print ("deleting ....  ")
    
    delete = RESTDelete(username, passwd)
    delete.delete_loopservices(serviceNames)

    
    