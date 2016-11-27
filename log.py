#ver .03
# -*- coding: utf-8 -*-

import logging

def log(key,massage):
        logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG,filename = u'logs.log')
        if key == 'D':
            # Сообщение отладочное
            logging.debug( massage)
        if key == 'I':
            # Сообщение информационное
            logging.info( massage )
        if key == 'W':
            # Сообщение предупреждение
            logging.warning( massage )
        if key == 'E':
            # Сообщение ошибки
            logging.error( massage )
        if key == 'C':
            # Сообщение критическое
            logging.critical( massage )

