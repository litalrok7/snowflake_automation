from utils import snowflake_utils


class ConnectionSettings:
    def __init__(self, **kwargs):
        class DBSection:
            def __init__(self, **section_args):
                self.account_name = section_args.get('account_name')
                self.database_name = section_args.get('database_name')
                self.schema_name = section_args.get('schema_name')
                self.warehouse_name = section_args.get('warehouse_name')

        class UserSection:
            def __init__(self, **section_args):
                self.user_login_name = section_args.get('user_login_name')
                self.password = section_args.get('password')

        self.DBSection = DBSection(**kwargs.get('db_settings'))
        self.UserSection = UserSection(**kwargs.get('user_credentials'))


def get_connection_settings(root_path):
    return ConnectionSettings(**snowflake_utils.get_connection_settings(root_path))


def connection_settings_as_dict(root_path):
    return snowflake_utils.get_connection_settings(root_path)

