import os
import logging

CURRENT_PATH = os.getcwd()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', filename=os.path.join(CURRENT_PATH, 'out', 'logs.txt'), filemode='w')

logging.info(f"Current path: {CURRENT_PATH}")