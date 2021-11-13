#!/usr/bin/python
import logging
import time
import signal

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
# create logger object with 'ERROR' level logging.

def handler1(signum, frame):
    logger.setLevel(logging.DEBUG)

def handler2(signum, frame):
    logger.setLevel(logging.INFO)

signal.signal(signal.SIGUSR1, handler1)
# if process receives SIGUSR1 signal, the logging level changes to DEBUG.

signal.signal(signal.SIGUSR2, handler2)
# if process receives SIGUSR1 signal, the logging level changes to INFO.

while True:
    logger.info('info logging')
    logger.debug('debug logging')
    logger.error('error logging')
    logger.warn('warn logging')
    time.sleep(2)

# 1. watchdog read config file changes, send SIGUSR1 to `python main`
# 2. `python main` SIGUSR1 handler re-read config file and set logging level
