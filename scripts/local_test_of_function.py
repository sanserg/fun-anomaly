import json
import logging
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, func
from iotfunctions import bif
from anomaly.functions import SimpleAnomaly
from iotfunctions.metadata import EntityType
from iotfunctions.db import Database
from iotfunctions.enginelog import EngineLogging
from anomaly import settings

EngineLogging.configure_console_logging(logging.DEBUG)

'''
# Replace with a credentials dictionary or provide a credentials
# Explore > Usage > Watson IOT Platform Analytics > Copy to clipboard
# Past contents in a json file.
'''

#with open('credentials.json', encoding='utf-8') as F:
db_schema = 'bluadmin' #  set if you are not using the default
with open('credentials_Monitor-Demo.json', encoding='utf-8') as F:
#    credentials = json.loads(F.read())
#db_schema = 'dash100462'  # replace if you are not using the default schema
#with open('credentials_dev2.json', encoding='utf-8') as F:
    credentials = json.loads(F.read())

'''
Developing Test Pipelines
-------------------------
When creating a set of functions you can test how they these functions will
work together by creating a test pipeline.
'''


'''
Create a database object to access Watson IOT Platform Analytics DB.
'''
db = Database(credentials = credentials)

'''
To do anything with IoT Platform Analytics, you will need one or more entity type.
You can create entity types through the IoT Platform or using the python API as shown below.
The database schema is only needed if you are not using the default schema. You can also rename the timestamp.
'''
#entity_name = 'EnergySystemModel02'

'''
entity = EntityType(entity_name,db,
                    Column('TURBINE_ID',String(50)),
                    Column('TEMPERATURE',Float()),
                    Column('PRESSURE',Float()),
                    SimpleAnomaly( username = BI_USERNAME,
                                    password = BI_PASSWORD,
                                    request='GET',
                                    url="https://turbine-simulator.mybluemix.net/v1/api/reading",
                                    output_item = 'http_preload_done'),
                    bif.PythonExpression(expression='df["TEMPERATURE"]*df["PRESSURE"]',
                                         output_name = 'VOLUME'),
                    **{
                      '_timestamp' : 'evt_timestamp',
                      '_db_schema' : db_schema
})
'''

'''
When creating an EntityType object you will need to specify the name of the entity, the database
object that will contain entity data

After creating an EntityType you will need to register it so that it visible in the Add Data to Entity Function UI.
To also register the functions and constants associated with the entity type, specify
'publish_kpis' = True.
'''
#entity.register(raise_error=False)

# You must unregister_functions if you change the mehod signature or required inputs.
#db.unregister_functions(["SimpleAnomaly"])
db.register_functions([SimpleAnomaly])

'''
To test the execution of kpi calculations defined for the entity type locally
use this function.

A local test will not update the server job log or write kpi data to the AS data
lake. Instead kpi data is written to the local filesystem in csv form.
'''

#entity.exec_local_pipeline()

'''
view entity data
'''
print ( "Read Table of new  entity" )
#df = db.read_table(table_name=entity_name, schema=db_schema)
#print(df.head())

print ( "Done registering  entity" )
