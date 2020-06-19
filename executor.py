import time
import logging
from concurrent.futures import ThreadPoolExecutor

formatter = logging.Formatter(
    "%(asctime)s.%(msecs)03d - %(module)s:%(lineno)3d - %(levelname)5s - %(message)s",
    datefmt='%H:%M:%S')
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
logger = logging.getLogger('')
logger.addHandler(streamHandler)
logger.setLevel(logging.DEBUG)


def long_task(input):
    logging.info('%s start' % input)
    time.sleep(1)
    logging.info('%s stop' % input)
    pass


if __name__ == '__main__':
    to_process = list(range(0, 20))

    with ThreadPoolExecutor(5) as executor:
        futures = [executor.submit(long_task, i) for i in to_process]
        time.sleep(3)
        for f in futures:
            print('%s' % f)
    logging.info('elo')
