table_query = [{
    "name": "COLLISION_EVENTS",
    "need_to_update": 0,
    "field_date_to_int": 3,
    "table_columns": [{'name': 'EVENT_ID', 'type': 'NUMBER'},
                      {'name': 'VEHICLE_ID', 'type': 'NUMBER'},
                      {'name': 'EVENT_DATE', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'LATITUDE', 'type': 'FLOAT'},
                      {'name': 'LONGITUDE', 'type': 'FLOAT'},
                      {'name': 'SPEED', 'type': 'NUMBER'},
                      {'name': 'COLLISION_ENERGY', 'type': 'FLOAT'},
                      {'name': 'DIRECTION', 'type': 'NUMBER'},
                      {'name': 'DIRECTION_STRING', 'type': 'VARCHAR'},
                      {'name': 'COLLISION_SEVERITY', 'type': 'VARCHAR'},
                      {'name': 'FILE_NAME', 'type': 'VARCHAR'},
                      {'name': 'FILE_DATE', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'EVENT_DATE_INT', 'type': 'NUMBER'}],
    "number_of_fields": 10
    }, {
    "name": "DRIVES",
    "need_to_update": 0,
    "field_date_to_int": 5,
    "table_columns": [{'name': 'DRIVE_ID', 'type': 'NUMBER'},
                      {'name': 'VEHICLE_ID', 'type': 'NUMBER'},
                      {'name': 'DRIVER_ID', 'type': 'NUMBER'},
                      {'name': 'START_EVENT', 'type': 'NUMBER'},
                      {'name': 'START_DRIVE', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'START_LATITUDE', 'type': 'FLOAT'},
                      {'name': 'START_LONGITUDE', 'type': 'FLOAT'},
                      {'name': 'END_EVENT', 'type': 'NUMBER'},
                      {'name': 'END_DRIVE', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'END_LATITUDE', 'type': 'FLOAT'},
                      {'name': 'END_LONGITUDE', 'type': 'FLOAT'},
                      {'name': 'MILEAGE', 'type': 'FLOAT'},
                      {'name': 'DRIVE_DURATION', 'type': 'NUMBER'},
                      {'name': 'TOTAL_MILEAGE', 'type': 'FLOAT'},
                      {'name': 'FUEL_USED', 'type': 'FLOAT'},
                      {'name': 'ENGINE_HOURS', 'type': 'FLOAT'},
                      {'name': 'FUEL_CONSUMPTION', 'type': 'NUMBER'},
                      {'name': 'IDLE_DURATION', 'type': 'NUMBER'},
                      {'name': 'TURN1', 'type': 'NUMBER'},
                      {'name': 'TURN2', 'type': 'NUMBER'},
                      {'name': 'TURN3', 'type': 'NUMBER'},
                      {'name': 'BREAK1', 'type': 'NUMBER'},
                      {'name': 'BREAK2', 'type': 'NUMBER'},
                      {'name': 'BREAK3', 'type': 'NUMBER'},
                      {'name': 'ACCELERATION1', 'type': 'NUMBER'},
                      {'name': 'ACCELERATION2', 'type': 'NUMBER'},
                      {'name': 'ACCELERATION3', 'type': 'NUMBER'},
                      {'name': 'SPEED1', 'type': 'NUMBER'},
                      {'name': 'SPEED2', 'type': 'NUMBER'},
                      {'name': 'SPEED3', 'type': 'NUMBER'},
                      {'name': 'DRIVER_GRADE', 'type': 'NUMBER'},
                      {'name': 'MECAHNICAL_EVENT', 'type': 'NUMBER'},
                      {'name': 'BREAKING_SYSTEM', 'type': 'NUMBER'},
                      {'name': 'GEARBOX', 'type': 'NUMBER'},
                      {'name': 'ENGINE', 'type': 'NUMBER'},
                      {'name': 'CLUTCH_SYSTEM', 'type': 'NUMBER'},
                      {'name': 'MECHANICAL_GRADE', 'type': 'NUMBER'},
                      {'name': 'TIME_FROM_PREV_DRIVE', 'type': 'NUMBER'},
                      {'name': 'DRIVE_SAFETY_SCORE_SD', 'type': 'NUMBER'},
                      {'name': 'FILE_NAME', 'type': 'VARCHAR'},
                      {'name': 'FILE_DATE', 'type': 'VARCHAR'},
                      {'name': 'START_DRIVE_INT', 'type': 'NUMBER'}],
    "number_of_fields": 39
    }, {
    "name": "EVENTS",
    "need_to_update": 0,
    "field_date_to_int": 5,
    "table_columns": [{'name': 'EVENT_ID', 'type': 'NUMBER'},
                      {'name': 'VEHICLE_ID', 'type': 'NUMBER'},
                      {'name': 'SCHEME_ID', 'type': 'NUMBER'},
                      {'name': 'DRIVE_ID', 'type': 'NUMBER'},
                      {'name': 'START_TIME', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'LONGITUDE', 'type': 'FLOAT'},
                      {'name': 'LATITUDE', 'type': 'FLOAT'},
                      {'name': 'LOCATION', 'type': 'VARCHAR'},
                      {'name': 'SPEED', 'type': 'NUMBER'},
                      {'name': 'LAST_DIRECTION', 'type': 'NUMBER'},
                      {'name': 'END_TIME', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'END_LONGITUDE', 'type': 'FLOAT'},
                      {'name': 'END_LATITUDE', 'type': 'FLOAT'},
                      {'name': 'END_LOCATION', 'type': 'VARCHAR'},
                      {'name': 'START_MILEAGE', 'type': 'FLOAT'},
                      {'name': 'END_MILEAGE', 'type': 'FLOAT'},
                      {'name': 'MAX_SPEED', 'type': 'NUMBER'},
                      {'name': 'FILE_NAME', 'type': 'VARCHAR'},
                      {'name': 'FILE_DATE', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'START_DRIVE_INT', 'type': 'NUMBER'}],
    "number_of_fields": 17
}, {
    "name": "GPS",
    "need_to_update": 0,
    "field_date_to_int": 4,
    "table_columns": [{'name': 'VEHICLE_ID', 'type': 'NUMBER'},
                      {'name': 'LONGITUDE', 'type': 'FLOAT'},
                      {'name': 'LATITUDE', 'type': 'FLOAT'},
                      {'name': 'ORIG_TIME', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'SPEED', 'type': 'NUMBER'},
                      {'name': 'DIRECTION', 'type': 'NUMBER'},
                      {'name': 'VEHICLE_STATE', 'type': 'NUMBER'},
                      {'name': 'MILEAGE', 'type': 'FLOAT'},
                      {'name': 'ROAD_SPEED', 'type': 'NUMBER'},
                      {'name': 'FILE_NAME', 'type': 'VARCHAR'},
                      {'name': 'FILE_DATE', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'ORIG_TIME_INT', 'type': 'NUMBER'}],
    "number_of_fields": 9
}, {
    "name": "PARAMS",
    "need_to_update": 0,
    "field_date_to_int": 3,
    "table_columns": [{'name': 'VEHICLE_ID', 'type': 'NUMBER'},
                      {'name': 'EVENT_ID', 'type': 'NUMBER'},
                      {'name': 'ORIG_TIME', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'PARAM_TYPE', 'type': 'NUMBER'},
                      {'name': 'PARAM_VALUE', 'type': 'FLOAT'},
                      {'name': 'FILE_NAME', 'type': 'VARCHAR'},
                      {'name': 'FILE_DATE', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'ORIG_TIME_INT', 'type': 'NUMBER'}],
    "number_of_fields": 5
}, {
    "name": "METADATA_PARAMS",
    "need_to_update": 1,
    "field_date_to_int": 4,
    "table_columns": [{'name': 'PARAM_TYPE', 'type': 'NUMBER'},
                      {'name': 'PARAM_TYPE_DESCR', 'type': 'VARCHAR'},
                      {'name': 'FILE_NAME', 'type': 'VARCHAR'},
                      {'name': 'FILE_DATE', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'ROW_VERSION', 'type': 'NUMBER'}],
    "number_of_fields": 2
}, {
    "name": "METADATA_SCMS",
    "need_to_update": 1,
    "field_date_to_int": 14,
    "table_columns": [{'name': 'SCHEME_ID', 'type': 'NUMBER'},
                      {'name': 'SCHEME_DESCR', 'type': 'VARCHAR'},
                      {'name': 'SCHEME_TYPE_CODE', 'type': 'NUMBER'},
                      {'name': 'SCHEME_TYPE_DESC', 'type': 'VARCHAR'},
                      {'name': 'SCHEME_PARENT_ID', 'type': 'NUMBER'},
                      {'name': 'PARENT_DESCR', 'type': 'VARCHAR'},
                      {'name': 'SEVERITY_LEVEL', 'type': 'NUMBER'},
                      {'name': 'SOURCE', 'type': 'NUMBER'},
                      {'name': 'SOURCE_NAME', 'type': 'VARCHAR'},
                      {'name': 'MECHANICAL_GRADE', 'type': 'NUMBER'},
                      {'name': 'SIXT_TYPE', 'type': 'NUMBER'},
                      {'name': 'SIXT_CATEGORY', 'type': 'VARCHAR'},
                      {'name': 'FILE_NAME', 'type': 'VARCHAR'},
                      {'name': 'FILE_DATE', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'ROW_VERSION', 'type': 'NUMBER'}],
    "number_of_fields": 12
 }, {
    "name": "METADATA_VCLS",
    "need_to_update": 1,
    "field_date_to_int": 6,
    "table_columns": [{'name': 'VEHICLE_ID', 'type': 'NUMBER'},
                      {'name': 'LICENSE_NMBR', 'type': 'VARCHAR'},
                      {'name': 'MANUFACTURER', 'type': 'VARCHAR'},
                      {'name': 'MODEL', 'type': 'VARCHAR'},
                      {'name': 'FILE_NAME', 'type': 'VARCHAR'},
                      {'name': 'FILE_DATE', 'type': 'TIMESTAMP_NTZ'},
                      {'name': 'ROW_VERSION', 'type': 'NUMBER'}],
    "number_of_fields": 4
}]

