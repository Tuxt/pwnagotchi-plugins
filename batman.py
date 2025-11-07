import logging
from max1704x_smbus import MAX17048 # pip install MAX17048-smbus
from pwnagotchi.plugins import Plugin

class BatMan(Plugin):
    __author__ = "Tuxt <tuxt@protonmail.com>"
    __version__ = "1.0.0"
    __license__ = "GPL3"
    __description__ = "MAX17048-based battery manager"

    
