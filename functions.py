# -*- coding: utf-8 -*-

import logging


def reroute_power():
    log = logging.getLogger()
    log.warning('Rerouting energy through the flux capacitor')
    return True


def power_transfer():
    log = logging.getLogger()
    log.error('Power tranfer failed, core overloading')
    return True

if __name__ == "__main__":
    reroute_power()
    power_transfer()
