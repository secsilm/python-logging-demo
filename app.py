import logging
import logging.config

import yaml

from package_a import module_a

with open("logging_config.yml", "r", encoding="utf8") as f:
    logging_config = yaml.safe_load(f)
logging.config.dictConfig(logging_config)
logger = logging.getLogger('app')

logger.debug("来自 app 的 DEBUG 日志。")
logger.warning("来自 app 的 WARNING 日志。")
module_a.print_log()