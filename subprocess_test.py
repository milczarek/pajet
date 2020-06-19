import logging
import subprocess
from subprocess import PIPE


formatter = logging.Formatter(
    "%(asctime)s.%(msecs)03d - %(module)s:%(lineno)3d - %(levelname)5s - %(message)s",
    datefmt='%H:%M:%S')
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
logger = logging.getLogger('')
logger.addHandler(streamHandler)
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    logging.info("Calling subprocess")
    sh = subprocess.run(['./myscript.sh', 'param1', 'param2'], env={'MYENV': 'MY-ENV-VAL'}, shell=False, stdout=PIPE, stderr=PIPE)
    logging.info("%s", sh.stdout)
    logging.info("%s", sh.stderr)
    logging.info("%s", sh.returncode)
