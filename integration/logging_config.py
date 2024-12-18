import logging

def setup_logging():

    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    return logger


logger = setup_logging()
