#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import logging.config
from config_logging import config_logging_dict

logging.config.dictConfig(config_logging_dict)
logger = logging.getLogger('bistream_logging_sample')


def main():
	logger.debug("デバッグ")
	time.sleep(1)
	logger.info("インフォ")
	time.sleep(1)
	logger.warning("ワーニング")
	time.sleep(1)
	logger.error("エラー")
	time.sleep(1)
	logger.critical("クリティカル")
	return


if __name__ == "__main__":
	main()
