"""
Created 13 september 2025
Author: Jean-Jacques BABIN-DAMANA
license: MIT
"""

import logging
import os
import sys
from core.execution import ExecutionEngine
from adapters.tradovate_api import TradovateAPI

GLOBAL_LOGS = r"C:\Users\babin\Project_trading_bot\trading_bot_sw\strading_bot\logging_package\logs.txt"


def main():
    """ This is a trading bot for futures market 
    Feature 1 : Open buy or sell position
    Feature 2 : Risk management based on specific rules and market condition
    Feature 3 : Position Management (trailling stop, add/close small part)
    Feature 4 : Close buy or sell position
    """
    # Configure the log system 
    if len(sys.argv) >1 and sys.argv[1] == "v":
        logging.basicConfig(level="DEBUG")
        logger = logging.getLogger(__name__)
        # Start main
        logger.debug("trading bot is running ...")
    else :
        logging.basicConfig(filename=GLOBAL_LOGS, level="WARNING")
        logger = logging.getLogger(__name__)
        # Start main
        logger.debug("trading bot is running ...")

    
    adapter = TradovateAPI(api_key="...")
    engine = ExecutionEngine(adapter)

    # Exemple d’ordre
    order = engine.send_order(symbol="ESU5", qty=1, side="buy")
    logger.debug(f"Order placed: {order}")


if __name__=="__main__":
    status = main()
    sys.exit(status)