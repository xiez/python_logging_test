import logging
import logging.config
import time
import os
import threading

# read initial config file
logging.config.fileConfig('logging.conf')

# create and start listener on port 9999
t = logging.config.listen(9999)
t.start()

logger = logging.getLogger()

def reload_logging():
    while True:
        print('reload logging..')
        logging.config.fileConfig('./logging.conf')
        time.sleep(10)
conf_monitor = threading.Thread(target=reload_logging, daemon=True)
conf_monitor.start()

try:
    # loop through logging calls to see the difference
    # new configurations make, until Ctrl+C is pressed
    while True:
        print('log messages..')
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        time.sleep(1)
except KeyboardInterrupt:
    print('clean up ...')
    # cleanup
    logging.config.stopListening()
    t.join()

print('DONE.')
