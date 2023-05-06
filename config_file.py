import os
from configparser import ConfigParser


def get_database_params(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise FileNotFoundError(
            'Section {0} is not found in the {1} file.'.format(
                section,
                filename
                ))
    return db

databasename='products'


