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


ENVIRS = os.environ.copy()

ENVIRS['PYTHONPATH'] = \
	'S:/_management/_mb_Pipeline/mb_Armada/mb_Armada/modules/dependencies/ftrack_api' + \
	';S:/_management/_mb_Pipeline/mb_Armada/mb_Armada/modules/ftrack/connect/ftrack-connect/source' + \
	';S:/_management/_mb_Pipeline/mb_Armada/mb_Armada/modules/ftrack/connect/ftrack-connect-maya/source' + \
	';S:/_management/_mb_Pipeline/mb_Armada/mb_Armada/envs/ftrack-api-env/Lib/site-packages'

ENVIRS['FTRACK_CONNECT_PLUGIN_PATH'] = \
	'S:/_management/_mb_Pipeline/mb_Armada/mb_Armada/modules/ftrack/connect/ftrack-connect' + \
	';S:/_management/_mb_Pipeline/mb_Armada/mb_Armada/modules/ftrack/connect/ftrack-connect-maya'

ENVIRS['FTRACK_CONNECT_MAYA_PLUGINS_PATH']= \
	'S:/_management/_mb_Pipeline/mb_Armada/mb_Armada/modules/ftrack/connect/ftrack-connect-maya/resource'

logger.info('Launching Ftrack...')

subprocess.Popen(['python', '-m', 'ftrack_connect'])