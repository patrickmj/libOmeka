
import sys
sys.path.append('/var/www/libOmeka')

from omekasite import OmekaSite
from record import *
from file import *
import json

def test(): 
    print("ok")
    
    omekasite = OmekaSite('http://localhost/Omeka/api', 'b0ed84e20774a0d1c1e48d7736591e6d6909a1b4')
    rec = Record(resource_name = 'items', site = omekasite)
    rec.get(91)
    #rec.post()
    #rec = Record('{"prop" : "value", "id": "test"}', site='site')
    

def filetest():
    jrecord = '{"id": "test", "url": "testurl"}'
    omekasite = OmekaSite('http://localhost/Omeka/api', 'b0ed84e20774a0d1c1e48d7736591e6d6909a1b4')
    ofile = File(jrecord, 'files', omekasite)
    ofile.post()

filetest()
