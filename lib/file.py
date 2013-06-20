import json
import poster
from record import *
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers


class File(Record):
    
    def add_file(self, file_url):
        self.file_url = file_url
        
        
        
    def post(self):
        self.file_url = 'test.txt'
        if not self.record:
            data = {}
        else:
            #data = json.JSONEncoder().encode(self.record)
            data = self.record
        data.update({"file": open(self.file_url, "rb")})
        data = {"file": open(self.file_url, "rb")}
        register_openers()
        datagen, headers = multipart_encode(data) #put in file record?
        print(headers)
        response = self.site.api_post_record(self.resource_name, datagen, headers)
        print(response)        