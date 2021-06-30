import logging
import time

from logging.handlers import RotatingFileHandler

# ----------------------------------------------------------------------
def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=2000, backupCount=5)
    logger.addHandler(handler)

    for i in range(9999):
        logger.info("This is test log line %s" % i)
        time.sleep(0.1)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    log_file = "test.log"
    create_rotating_log(log_file)