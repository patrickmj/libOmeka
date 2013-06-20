'''
Created on Jun 14, 2013

@author: patrickmj
'''
import logging
import json

class Resource(object):
    '''
    classdocs
    '''


    def __init__(self, jresource):
        '''
        Constructor
        '''
        self.resource = json.loads(jresource)
        self.url = self.resource.url
        self.controller = self.resource.controller
        self.recordType = self.resource.record_type
        self.actions = self.resource.actions
        self.indexParams = self.resource.indexParams
        logging.info('constructed Resource')
        