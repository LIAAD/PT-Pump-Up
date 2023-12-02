import os
import logging

CURRENT_PATH = os.getcwd()

logs_file = os.path.join(CURRENT_PATH, 'out', 'logs.txt')

# Make directory if it does not exist
if not os.path.exists(os.path.dirname(logs_file)):
    os.makedirs(os.path.dirname(logs_file))

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', filename=os.path.join(CURRENT_PATH, 'out', 'logs.txt'), filemode='w')

logging.info(f"Current path: {CURRENT_PATH}")
