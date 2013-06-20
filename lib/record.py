import json

class Record(object):
    
    def __init__(self, jrecord = None, resource_name = None, site = None):
        if jrecord is not None:
            self.set_record(jrecord)
        if resource_name is not None:
            self.resource_name = resource_name
        if site is not None:
            self.associate_with_site(site)

    def set_record(self, jrecord):
            self.record = json.loads(jrecord)
            self.id = self.record['id']
            self.url = self.record['url']
                            
    def get(self, record_id):
        if not self.resource_name:
            raise Exception('Resource name must be set')
        jrecord = self.site.api_get_record(self.resource_name, record_id)
        self.set_record(jrecord)
        
    def post(self):
        data = json.JSONEncoder().encode(self.record)
        response = self.site.api_post_record(self.resource_name, data)
        print(response)
        
    def put(self):
        data = self.record ##make json
        
    def associate_with_site(self, site):
        self.site = site
        
    def set_resource_name(self, resource_name):
        self.resource_name = resource_name