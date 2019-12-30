import logging

logger = logging.getLogger(__name__)


def print_log():
    logger.debug("来自 module_a 的 DEBUG 日志")
    logger.warning("来自 module_a 的 WARNING 日志")
