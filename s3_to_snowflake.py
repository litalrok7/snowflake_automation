#!/usr/bin/env python

from connection_settings import snowflake_settings
import os
from utils import db_session
from utils import tables_structures
import time

FOLDER_PATH = os.path.dirname(os.path.realpath(__file__))
ENV = snowflake_settings.get_connection_settings(FOLDER_PATH)


def create_connection_string(conn_settings):
    return 'snowflake://{user_login_name}:{password}@{account_name}/' \
           '{database_name}/{schema_name}?warehouse={warehouse_name}'.format(
            user_login_name=conn_settings.UserSection.user_login_name,
            password=conn_settings.UserSection.password,
            account_name=conn_settings.DBSection.account_name,
            database_name=conn_settings.DBSection.database_name,
            schema_name=conn_settings.DBSection.schema_name,
            warehouse_name=conn_settings.DBSection.warehouse_name)


def update_schema_to_query(query, db_settings, table_name = None):
    return query.format(database_name=db_settings.database_name,
                        schema_name=db_settings.schema_name) \
        if table_name is None \
        else query.format(
        database_name=db_settings.database_name,
        schema_name=db_settings.schema_name,
        table_name=table_name)


def trancate_table(table_settings, db_settings, connection):
    sql_trancate_query = \
        update_schema_to_query('TRUNCATE TABLE {database_name}.{schema_name}.{table_name}',
                               db_settings, table_settings['name'])
    connection.execute(sql_trancate_query, autocommit=True)
    return


def update_data(table_settings, db_settings, connection):
    if table_settings['need_to_update'] == 1:
        connection.execute(update_schema_to_query(table_settings['create_query'],
                                                  db_settings), autocommit=True)
        connection.execute(update_schema_to_query(table_settings['stg_query'],
                                                  db_settings), autocommit=True)
    connection.execute(update_schema_to_query(table_settings['update_query'],
                                              db_settings), autocommit=True)
    return


def drop_temp_table(table_settings, db_settings, connection):
    sql_drop_query = \
        update_schema_to_query('DROP TABLE {database_name}.{schema_name}.{table_name}_TEMP',
                               db_settings, table_settings['name'])
    connection.execute(sql_drop_query, autocommit=True)
    return


def main():
    snowflake_conn_str = create_connection_string(ENV)
    try:
        db_settings = ENV.DBSection
        tables = tables_structures.table_query
        with db_session.DBSession(snowflake_conn_str)as db_:
            for table in tables:
                trancate_table(table, db_settings, db_)
                update_data(table, db_settings, db_)
                if table['need_to_update'] == 1:
                    drop_temp_table(table, db_settings, db_)
    except Exception as e:
            print(type(e), e)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s minutes ---" % ((time.time() - start_time)/60))
