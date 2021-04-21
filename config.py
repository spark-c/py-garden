# config

import os

class Config():

    RESOLUTION = (640, 360)
    # RESOLUTION = (1280, 720)
    BG_COLOR = (0, 0, 255)
    CLIENT_FPS = 60

    def __init__(self):
        pass


class Production(Config):

    def __init__(self):
        pass


class Testing(Config):

    def __init__(self):
        pass


def get_config():
    if os.environ.get('CFG_MODE') == 'TESTING':
        cfg = Testing()
        print('***TESTING CONFIG***')
    else:
        print('***PRODUCTION CONFIG***')
        cfg = Production()

    return cfg