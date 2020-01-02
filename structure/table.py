import os
import json
conn_settings = {
    'account_name': 'bx73861.eu-west-1',
    'schema_name': 'DEMO_DB',
    'database_name': 'TRAFFILOG',
    'warehouse_name': 'COMPUTE_WH'
}


class Table(object):
    """__init__() functions as the class constructor"""
    def __init__(self, table_parameters, db_settings):
        self.name = table_parameters["name"]
        self.method = table_parameters["need_to_update"]  # 0- insert(append) ; 1- update
        self.truncate_query = get_truncate_query(table_parameters["name"], db_settings)
        self.insert_query = get_insert_query(table_parameters)
        self.update_query = get_update_query(table_parameters)


def get_truncate_query(table_name, db_settings):
    return 'TRUNCATE TABLE {database_name}.' \
           '{schema_name}.{table_name}'.format(database_name=db_settings['database_name'],
                                               schema_name=db_settings['schema_name'],
                                               table_name=table_name)


def get_insert_query(table_parameters):
    return 1


def get_update_query(table_parameters):
    return 1


def get_data_from_json_file(file_path):
    with open(file_path) as json_data:
        data = json.load(json_data)
        return data


def main():
    tables_structure = []
    file_path = "{folder_path}\\table_structure.json".format(folder_path=os.getcwd())
    tables = get_data_from_json_file(file_path)
    for table in tables:
        tables_structure.append(Table(table, conn_settings))
    return tables_structure


if __name__ == '__main__':
    main()