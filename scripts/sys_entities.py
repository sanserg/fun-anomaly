# Create Demo Entity to demonstrate anomaly detection with dimensional filters
# See https://github.com/ibm-watson-iot/functions/blob/development/iotfunctions/entity.py

from iotfunctions import metadata
from iotfunctions.metadata import EntityType
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, func
from iotfunctions import bif
from iotfunctions.db import Database
import logging
import sys
from collections import defaultdict


class SSTanks(metadata.BaseCustomEntityType):

    '''
    Sample entity type for monitoring a manufacturing line. Monitor comfort levels, energy
    consumption and occupany.
    '''
    def __init__(self,
                 name,
                 db,
                 db_schema=None,
                 description=None,
                 generate_days=0,
                 drop_existing=True,
                 ):

        # constants
        constants = []
        physical_name = name.lower()

        # granularities
        granularities = []

        # columns
        columns = []

        # Create Entity Type at each system level
        columns.append(Column('AlarmLo',String(5) ))
        columns.append(Column('AlarmHiDB', Float() ))
        columns.append(Column('TempSP', Float() ))
        columns.append(Column('AlarmHi', String(5) ))
        columns.append(Column('AlarmLoDB', Float() ))
        columns.append(Column('TempDB', Float() ))
        columns.append(Column('AlarmEnable', String(5) ))
        columns.append(Column('Alarm', Float() ))
        columns.append(Column('AlarmHiDly', Float() ))
        columns.append(Column('AlarmLoDly', Float() ))
        columns.append(Column('Valve', Float() ))
        columns.append(Column('TempACT', Float() ))

        # dimension columns
        dimension_columns = []
        dimension_columns.append(Column('Client', String(50)))
        dimension_columns.append(Column('Location', String(50)))
        dimension_columns.append(Column('Room', String(50)))
        dimension_columns.append(Column('System', String(50)))

        # functions
        functions = []
        # simulation settings
        # uncomment this if you want to create entities automatically
        '''
        sim = {
            'freq': '5min',
            'auto_entity_count' : 1,
            'data_item_mean': {'TEMPERATURE': 22,
                               'STEP': 1,
                               'PRESSURE': 50,
                               'TURBINE_ID': 1
                               },
            'data_item_domain': {
                'CLIENT' : ['Riverside MFG','Collonade MFG','Mariners Way MFG' ],
                'ORG': ['Engineering','Supply Chain', 'Production', 'Quality', 'Other'],
                'FUNCTION': ['New Products','Packaging','Planning','Warehouse', 'Logistics', 'Customer Service','Line 1', 'Line 2', 'Quality Control', 'Calibration', 'Reliability']
            },
            'drop_existing': False
        }

        generator = bif.EntityDataGenerator(ids=None, parameters=sim)
        functions.append(generator)
        '''
        # data type for operator cannot be inferred automatically
        # state it explicitly

        output_items_extended_metadata = {}

        super().__init__(name=name,
                         db = db,
                         constants = constants,
                         granularities = granularities,
                         columns=columns,
                         functions = functions,
                         dimension_columns = dimension_columns,
                         output_items_extended_metadata = output_items_extended_metadata,
                         generate_days = generate_days,
                         drop_existing = drop_existing,
                         description = description,
                         db_schema = db_schema)
