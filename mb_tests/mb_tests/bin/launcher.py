import os
import sys
import subprocess
import logging


# Directories
_ROOT_DIR = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]

_LOGS_DIR = os.path.join(_ROOT_DIR, 'logs') 
_ENVS_DIR = os.path.join(_ROOT_DIR, 'envs') 
_MODULES_DIR = os.path.join(_ROOT_DIR, 'modules')
_FTRACK_DIR = os.path.join(_MODULES_DIR, 'ftrack')
_CONNECT_DIR = os.path.join(_FTRACK_DIR, 'connect')
print _CONNECT_DIR

if not os.path.exists(_LOGS_DIR):
	os.makedirs(_LOGS_DIR) 

logger = logging.getLogger(__name__)
handler = logging.FileHandler('%s/launcher_log.log' % _LOGS_DIR, mode='w')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler) 
logger.setLevel(logging.INFO)

envs = os.environ.copy()

envs['PYTHONPATH'] = \
	os.path.join(_FTRACK_DIR, 'pythonpath') + \
	';' + os.path.join(_CONNECT_DIR, 'ftrack-connect', 'source') + \
	';' + os.path.join(_CONNECT_DIR, 'ftrack-connect-maya' 'source') + \
	';' + os.path.join(_ENVS_DIR, 'ftrack-api-env', 'Lib', 'site-packages')

envs['FTRACK_CONNECT_PLUGIN_PATH'] = \
	os.path.join(_CONNECT_DIR, 'ftrack-connect') + \
	';S:/_management/_mb_Pipeline/mb_Armada/mb_Armada/modules/ftrack/connect/ftrack-connect-maya'

envs['FTRACK_CONNECT_MAYA_PLUGINS_PATH']= \
	'S:/_management/_mb_Pipeline/mb_Armada/mb_Armada/modules/ftrack/connect/ftrack-connect-maya/resource'

logger.info('Launching Ftrack...')

subprocess.Popen(['python', '-m', 'ftrack_connect'], env=envs)