#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import logging

config_logging_dict = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'bistream': {
			'format': '[%(levelname)s] %(name)s-%(module)s: %(asctime)s: %(message)s',
			'datefmt': '%Y/%m/%d %H:%M:%S',
		},
	},
	'handlers': {
		'bistream': {
			'class': 'bistream_logging_handler.BistreamLoggingHandler',
			'level': 'DEBUG',
			'formatter': 'bistream',
			'threshold': logging.WARNING,
		},
	},
	'loggers': {
		'bistream_logging_sample': {
			'level': 'DEBUG',
			'handlers': ['bistream'],
		},
	},
}
