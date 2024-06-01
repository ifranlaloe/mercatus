import logging

def setup_logger(name, level=logging.INFO):
    """
    Set up a logger with the specified name and level.
    
    Parameters:
    name (str): The name of the logger.
    level (int): The logging level (default is logging.INFO).
    
    Returns:
    logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
