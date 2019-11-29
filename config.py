import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-santa-key'
    FILE_NAME = os.environ.get('FILE_NAME') or '/home/pi/cunning-xmas-site/santa/names.txt'
