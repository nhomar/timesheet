"""Main module."""
from configparser import ConfigParser
from os import environ
from os.path import isfile, join
from odoorpc import ODOO


config = ConfigParser()
DEFAULT_CONFIG = {
    "host": "localhost",
    "port": "8069",
    "username": "admin",
    "password": "admin",
    "dbname": "odoo"
}


def get_config(server='localhost', user='admin'):
    config_path = join(environ['HOME'], '.timesheet.ini')
    config.read(config_path)
    servers = config.sections()
    if server not in servers:
        config[server] = DEFAULT_CONFIG
        with open(config_path, 'a') as configfile:
            config.write(configfile)
    return config[server]


def tasks(config, domain=[]):
    odoo = ODOO(config['host'], port=int(config['port']))
    odoo.login(config['dbname'], config['username'], config['password'])
    task_obj = odoo.env['project.task']
    task_ids = task_obj.search(domain)
    tasks = odoo.execute('project.task', 'read', task_ids, ['name'])
    return tasks
