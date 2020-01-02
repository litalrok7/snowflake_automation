import configparser

DB_SETTINGS_FILE = '\config\\environment_settings.ini'


def get_connection_settings(current_path, file_name = DB_SETTINGS_FILE,
                            sections=None, options=None):
    file_path = str(current_path) + str(file_name)
    config = configparser.ConfigParser()
    config.read(file_path)

    if not sections:
        sections = config.sections()

    res = {}
    for section in sections:
        res[section] = {}
        if not options:
            get_options = config.options(section)
        else:
            get_options = [item for item in config.options(section)
                           if item in options]

        for option in get_options:
            res[section][option] = config.get(section, option)

    return res


def get_server_settings(current_path):
    return get_connection_settings(current_path=current_path,
                                   sections=['db_settings'])


def get_user_credentials(current_path):
    return get_connection_settings(current_path=current_path,
                                   sections=['user_credentials'])



