import json
import logging
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, func
from iotfunctions import bif
#from anomaly.functions import DemoHTTPPreload
from iotfunctions.metadata import EntityType
from iotfunctions.db import Database
from iotfunctions.enginelog import EngineLogging
from anomaly import settings
from scripts.sys_entities import SSTanks

EngineLogging.configure_console_logging(logging.DEBUG)

#with open('credentials.json', encoding='utf-8') as F:
#db_schema = 'bluadmin' #  set if you are not using the default
#with open('credentials_Monitor-Demo.json', encoding='utf-8') as F:
#    credentials = json.loads(F.read())
print("here")
db_schema = 'bluadmin' #  set if you are not using the default
with open('credentials_beta-2.json', encoding='utf-8') as F:
    credentials = json.loads(F.read())
#db_schema = 'dash100462'  # replace if you are not using the default schema
#with open('credentials_dev2.json', encoding='utf-8') as F:
#    credentials = json.loads(F.read())
print("Create Entity Types")
db = Database(credentials = credentials)

print("Creating SSTanks")
entity_type_name = 'SSTanks'
#db.drop_table(entity_type_name, schema = db_schema)
sstanks_entity_type = SSTanks(name = entity_type_name,
                db = db,
                db_schema = db_schema,
                description = "SCADA Operations Control Center",
                )
sstanks_entity_type.register(raise_error=False)
# You must unregister_functions if you change the mehod signature or required inputs.
#db.unregister_functions(["DataHTTPPreload"])
#db.register_functions([DemoHTTPPreload])

#entity.add_slowly_changing_dimension(self,property_name,datatype,**kwargs):
sstanks_entity_type.make_dimension()
#Exectute Pipeline
sstanks_entity_type.exec_local_pipeline()

'''
view entity data
'''
print ( "Read Table of new  entity" )
df = db.read_table(table_name=entity_name, schema=db_schema)
print(df.head())

print ( "Done registering  entity" )
