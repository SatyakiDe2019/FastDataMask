################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 15-Feb-2023               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### personal AI-driven voice assistant.    ####
####                                        ####
################################################

import os
import platform as pl

class clsConfigClient(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'REPORT_PATH': Curr_Path + sep + 'output' + sep,
        'REPORT_DIR': 'output',
        'SRC_PATH': Curr_Path + sep + 'data' + sep,
        'APP_DESC_1': 'Masking PII Data!',
        'DEBUG_IND': 'N',
        'INIT_PATH': Curr_Path,
        'FILE_NAME': 'PII.csv',
        'TITLE': "Masking PII Data!",
        'PATH' : Curr_Path
    }
