# AppLogger : The application logger for python
# Useful in auditing actions/variables and storing everything to a log file.
# Git repo: https://github.com/codarrenvelvindron/AppLogger-python
# By Codarren Velvindron
# Contact: devildron@gmail.com
# 25/02/2021
# Licence: MIT

import os
from datetime import datetime

class Logger:
    __logname = ''
    __folderpath = ''
    __logpath = ''
    __gen_date_v = ''
    __timestamp = ''
   
    def __init__(self, logname):
        """ Init for class """
        self.__logname = logname

    def __make_folder(self):
        cwd = os.getcwd()
        dirname = self.__logname + "_logs"
        self.__folderpath = os.path.join(cwd, dirname)
        try:
            os.makedirs (self.__folderpath,exist_ok = True)
        except OSError:
            pass

    def __gen_date(self):
        """ To generate date for logfile """
        now = datetime.now()
        format = "%d%m%Y"
        self.__gen_date_v = now.strftime(format)

    def __gen_log(self):
        """ Create log with with date and extension """
        self.__gen_date()
        logdate = self.__gen_date_v
        logext = ".log"
        current_logname = str(self.__logname) + "_" + str(logdate) + logext
        self.__logpath = os.path.join(self.__folderpath, current_logname)
        if not os.path.exists(self.__logpath):
            f = open (self.__logpath, "w")
            f.close()
    
    def __gen_timestamp(self):
        self.__timestamp = datetime.now()

    def write(self, action='action', data='data'):
        self.__make_folder()
        self.__gen_log()
        self.__gen_timestamp()

        timestamp = str(self.__timestamp)
        data = str(data)
        action = str(action)
        separator = " "
        entry = timestamp + separator + action + separator + data
        f = open (self.__logpath, "a")
        f.write(f'{entry}\n')
        f.close
