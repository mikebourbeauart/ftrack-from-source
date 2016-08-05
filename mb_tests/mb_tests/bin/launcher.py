import os
import subprocess
import logging

# Directory helpers
_ROOT_DIR = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
_LOGS_DIR = os.path.join(_ROOT_DIR, 'logs') 
_ENVS_DIR = os.path.join(_ROOT_DIR, 'envs') 
_MODULES_DIR = os.path.join(_ROOT_DIR, 'modules')
_FTRACK_DIR = os.path.join(_MODULES_DIR, 'ftrack')
_CONNECT_DIR = os.path.join(_FTRACK_DIR, 'connect')

# Logging
if not os.path.exists(_LOGS_DIR):
	os.makedirs(_LOGS_DIR) 

logger = logging.getLogger(__name__)
handler = logging.FileHandler('%s/launcher_log.log' % _LOGS_DIR, mode='w')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler) 
logger.setLevel(logging.INFO)

# Set env vars
ENVS = os.environ.copy()

ENVS['PYTHONPATH'] = \
	os.path.join(_ENVS_DIR, 'ftrack-api-env', 'Lib', 'site-packages') + \
	os.pathsep + os.path.join(_FTRACK_DIR, 'pythonpath', 'ftrack_api') + \
	os.pathsep + os.path.join(_FTRACK_DIR, 'pythonpath', 'ftrack-python-api', 'source') + \
	os.pathsep + os.path.join(_CONNECT_DIR, 'ftrack-connect', 'source') + \
	os.pathsep + os.path.join(_CONNECT_DIR, 'ftrack-connect-maya', 'source')

ENVS['FTRACK_CONNECT_PLUGIN_PATH'] = \
	os.path.join(_CONNECT_DIR, 'ftrack-connect') + \
	os.pathsep + os.path.join(_CONNECT_DIR, 'ftrack-connect-maya')

ENVS['FTRACK_CONNECT_MAYA_PLUGINS_PATH']= \
	os.path.join(_CONNECT_DIR, 'ftrack-connect-maya', 'resource')

# Logging
for key, val in sorted(ENVS.iteritems()):
	logger.info('_____________________________________________________________________')
	logger.info(key)
	item_list = []
	for item in val.split(';'):
		item_list.append(item)
		item_list.sort()
	for item in item_list:
		logger.info(item)

# Launch Ftrack
logger.info('Launching Ftrack...')

subprocess.Popen(['python', '-m', 'ftrack_connect'], env=ENVS)