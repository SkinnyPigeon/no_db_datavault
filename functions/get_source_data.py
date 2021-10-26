# Imports and setup

from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
import subprocess

import pandas as pd

project_folder = subprocess.check_output("pwd", shell=True).decode("utf-8").rstrip()
load_dotenv(os.path.join(project_folder, '.env'))
PORT = os.getenv('PGPORT')
PASSWORD = os.getenv('PGPASSWORD')
if PORT == None:
    PASSWORD = os.environ.get('PGPASSWORD')
    PORT = os.environ.get('PGPORT')

from sources.tags.fcrb import fcrb_tags
from sources.tags.ustan import ustan_tags
from sources.tags.zmc import zmc_tags

PORT = os.getenv('PGPORT')
PASSWORD = os.getenv('PGPASSWORD')
if PORT == None:
    PASSWORD = os.environ.get('PGPASSWORD')
    PORT = os.environ.get('PGPORT')


# Helper functions

def hospital_picker(hospital):
    if hospital == 'FCRB':
        return 'fcrb', fcrb_tags
    elif hospital == 'USTAN':
        return 'ustan', ustan_tags
    elif hospital == 'ZMC':
        return 'zmc', zmc_tags


def setup_connection(schema):
    engine = create_engine('postgresql://postgres:{}@localhost:{}/source'.format(PASSWORD, PORT))
    metadata = MetaData(schema=schema, bind=engine)
    metadata.reflect(engine)
    Base = automap_base(metadata=metadata)
    Base.prepare()
    Session = sessionmaker(bind=engine)
    session = Session()
    return {"metadata": metadata, "base": Base, "engine": engine, "session": session, 'schema': schema}


def object_as_dict(obj):
    return {column.key: getattr(obj, column.key) for column in inspect(obj).mapper.column_attrs}


def select_tags(tags_list, request_tags):
    selected_tags = []
    for request_tag in request_tags:
        for tag_definition in tags_list:
            try:
                if tag_definition['tag'] == request_tag:
                    selected_tags.append(tag_definition)
            except:
                pass
    return selected_tags


def get_classes(schema, base):
    tables = {}
    for class_name in base._decl_class_registry.values():
        if hasattr(class_name, '__table__') and class_name.__table__.fullname not in ['{schema}.serums_ids'.format(schema=schema), '{schema}.hospital_doctors'.format(schema=schema)]:
            tables.update({class_name.__table__.fullname: class_name})
    return tables

def convert_tuples_to_dict(row, fields):
    row_dict = {}
    if len(row) == len(fields):
        for index, column in enumerate(fields):
            row_dict[column] = row[index]
    return row_dict


# Converting Serums ID into source system ID    


def select_source_patient_id_name(body):
    connection = setup_connection(body)
    metadata = connection['metadata']
    table_dict = dict.fromkeys(metadata.sorted_tables)
    connection['engine'].dispose()
    for keys, values in table_dict.items():
        if keys.name == 'serums_ids':
            for column in keys.columns:
                if ".serums_id" not in str(column) and '.id' not in str(column):
                    return str(column).split(".")[1]


def select_source_patient_id_value(session, id_class, serums_id, key_name):
    result = session.query(id_class).filter_by(serums_id=serums_id).one()
    res = object_as_dict(result)
    return res[key_name]



# Selecting tabular data:

def select_tabular_patient_data(connection, tables, tag_definition, patient_id, key_name):
    data = []
    table_class = tables[tag_definition['source']]
    fields = tag_definition['fields']
    entities = []
    for field in fields:
        entities.append(getattr(table_class, field))
    result = connection['session'].query(table_class).with_entities(*entities).filter_by(**{key_name: patient_id}).all()
    
    for row in result:
        data.append(convert_tuples_to_dict(row, fields))
    return data



# Selecting the data based on the tags


def select_patient_data(connection, tags_definitions, patient_id, key_name):
    results = {}
    tables = get_classes(connection['schema'], connection['base'])
    for tag_definition in tags_definitions:
        if tag_definition['table']:
            results[tag_definition['source']] = select_tabular_patient_data(connection, tables, tag_definition, patient_id, key_name)
    return results

def get_patient_data(body):
    results = {}
    for hospital_id in body['hospital_ids']:
        results[hospital_id.upper()] = {}
        hospital, tags_list = hospital_picker(hospital_id)
        tags = select_tags(tags_list, body['tags'])
        connection = setup_connection(hospital)
        id_class = connection['base'].classes.serums_ids
        key_name = select_source_patient_id_name(hospital)
        patient_id = select_source_patient_id_value(connection['session'], 
                                                        id_class, 
                                                        body['serums_id'], key_name)
        data = select_patient_data(connection, tags, patient_id, key_name)
        connection['engine'].dispose()
        if len(data) > 0:
            results[hospital_id.upper()]['data'] = data
        results[hospital_id.upper()]['tags'] = tags
    return results