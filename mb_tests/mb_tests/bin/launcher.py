import os
import sys
import subprocess
import logging

_ROOT_DIR = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]

_LOGS_DIR = os.path.join(_ROOT_DIR, 'logs') 

if not os.path.exists(_LOGS_DIR):
	os.makedirs(_LOGS_DIR) 

logger = logging.getLogger(__name__)
handler = logging.FileHandler('%s/launcher_log.log' % _LOGS_DIR, mode='w')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler) 
logger.setLevel(logging.INFO)


logger.info('Launching Ftrack...')


subprocess.Popen(['python', '-m', 'ftrack_connect'], env=envs)