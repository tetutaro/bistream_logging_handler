#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
package of logging handler which divides output by log level
'''
import sys
import logging

__version__ = '0.1.2'
__url = 'https://github.com/tetutaro/bistream_logging_handler'
__author = 'maruyama'


class BistreamLoggingHandler(logging.Handler):

	terminator = '\n'

	def __init__(
		self, threshold=logging.WARNING,
		format='%(asctime)s: %(levelname)s: %(name)s-%(module)s: %(message)s'
	):
		logging.Handler.__init__(self)
		self.threshold = threshold
		self.formatter = logging.Formatter(format)
		return

	def flush(self):
		self.acquire()
		try:
			sys.stdout.flush()
			sys.stderr.flush()
		finally:
			self.release()
		return

	def emit(self, record):
		try:
			msg = self.format(record)
			if record.levelno < self.threshold:
				stream = sys.stdout
			else:
				stream = sys.stderr
			stream.write(msg)
			stream.write(self.terminator)
			stream.flush()
		except Exception:
			self.handleError(record)
		return

	def __repr__(self):
		level = logging.getLevelName(self.threshold)
		return '<%s (%s)>' % (self.__class__.__name__, level)
