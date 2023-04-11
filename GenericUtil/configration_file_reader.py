from configparser import ConfigParser

from GenericUtil import global_variables

config = ConfigParser()
config.read(global_variables.basic_config_ini_path)


def get_config_file_value(section, section_key):
    return config.get(section, section_key)


def get_locators_ini_file_data(section, section_key):
    config = ConfigParser()
    config.read(global_variables.locators_ini_path)
    locator_data = config.get(section, section_key)
    locator_data = list((locator_data,)).pop()
    return locator_data

def get_config_file_sections():
    return config.sections()
