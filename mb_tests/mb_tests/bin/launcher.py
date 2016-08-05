import os
import subprocess
import logging

###########################
# Directory helpers
_ROOT_DIR = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
_LOGS_DIR = os.path.join(_ROOT_DIR, 'logs') 
_VENVS_DIR = os.path.join(_ROOT_DIR, 'venv', 'ftrack-api-env') 
_MODULES_DIR = os.path.join(_ROOT_DIR, 'modules')
_FTRACK_DIR = os.path.join(_MODULES_DIR, 'ftrack')
_CONNECT_DIR = os.path.join(_FTRACK_DIR, 'connect')
_PYTHONPATH_DIR = os.path.join(_FTRACK_DIR, 'pythonpath')

###########################
# Make dirs
if not os.path.exists(_LOGS_DIR):
	os.makedirs(_LOGS_DIR) 

if not os.path.exists(_VENVS_DIR):
	os.makedirs(_VENVS_DIR) 

###########################
# Set up logging
logger = logging.getLogger(__name__)
handler = logging.FileHandler('%s/launcher_log.log' % _LOGS_DIR, mode='w')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler) 
logger.setLevel(logging.INFO)


###########################
# Build environments
ENVS = os.environ.copy()

ENVS['PYTHONPATH'] = \
	os.path.join(_VENVS_DIR, 'Lib', 'site-packages') + \
	os.pathsep + os.path.join(_FTRACK_DIR, 'pythonpath', 'ftrack_api') + \
	os.pathsep + os.path.join(_FTRACK_DIR, 'pythonpath', 'ftrack-python-api', 'source') + \
	os.pathsep + os.path.join(_CONNECT_DIR, 'ftrack-connect', 'source') + \
	os.pathsep + os.path.join(_CONNECT_DIR, 'ftrack-connect-maya', 'source')

ENVS['FTRACK_CONNECT_PLUGIN_PATH'] = \
	os.path.join(_CONNECT_DIR, 'ftrack-connect') + \
	os.pathsep + os.path.join(_CONNECT_DIR, 'ftrack-connect-maya')

ENVS['FTRACK_CONNECT_MAYA_PLUGINS_PATH']= \
	os.path.join(_CONNECT_DIR, 'ftrack-connect-maya', 'resource')

###########################
# Logging pretty print
for key, val in sorted(ENVS.iteritems()):
	logger.info('_____________________________________________________________________')
	logger.info(key)
	item_list = []
	for item in val.split(';'):
		item_list.append(item)
		item_list.sort()
	for item in item_list:
		logger.info(item)

###########################
# Launch ftrack connect
logger.info('Launching Ftrack...')

subprocess.Popen(['python', '-m', 'ftrack_connect'], env=ENVS)