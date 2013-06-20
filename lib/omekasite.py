'''
Created on Jun 14, 2013

@author: patrickmj
'''
import urllib
import urllib2
import httplib
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
#import urlparse

class OmekaSite(object):
    '''
    classdocs
    '''


    def __init__(self, url, key = False):
        '''
        Constructor
        '''
        self.url = url
        self.key = key
        self.resources = None
        
    def api_get_record(self, resource_name, record_id):
        if isinstance(record_id, int):
            record_id = str(record_id)
        url = self.url + '/' + resource_name + '/' + record_id
        response = self.request(url, 'GET')
        return response.read()
        
    def api_post_record(self, resource_name, data, headers = None):
        if not self.key:
            raise Exception('need a key to post')
        url = self.url + '/' + resource_name + '?key=' + self.key
        response = self.request(url, 'POST', data, headers)
        
        return response.read()        
    
    
    def request(self, url, method, data = None, headers = None):
        #opener = urllib2.build_opener(urllib2.HTTPHandler)
        if data is None:
            req = urllib2.Request(url)
        else:
            #register_openers()
            #datagen, headers = multipart_encode({"image1": open("DSC0001.jpg", "rb")}) #put in file record?            
            #urllib2.Request(url, datagen, headers)
            #print(data)
            #data = urllib.urlencode(data)
            #print(data)
            if headers is None:
                req = urllib2.Request(url, data)
            else:
                datagen, headers = multipart_encode({"image1": open("after.png", "rb")}) #put in file record?
                #print(str(data))
                url = 'http://localhost/apitest/apitest.php'
                #datagen = '{"data" : "wtf"}'
                req = urllib2.Request(url, datagen, headers)
        req.get_method = lambda: method
        try:
            print(urllib2.urlopen(req).read())
            #res = urllib2.urlopen(req)
            #return res
        except (urllib2.URLError, urllib2.HTTPError) as err:
            return err
        
