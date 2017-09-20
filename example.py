# -*- coding: utf-8 -*-

from logger import debug_logging
from functions import reroute_power
from functions import power_transfer


def main():
    log = debug_logging()

    # Run One
    log.info('Reroute power')
    reroute_power()

    # Run Two
    log.info('Initiate power tranfer')
    power_transfer()

if __name__ == "__main__":
    main()
