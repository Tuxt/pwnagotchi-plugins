import logging
from max1704x_smbus import MAX17048 # pip install MAX17048-smbus
from pwnagotchi.plugins import Plugin
import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK

class BatMan(Plugin):
    __author__ = "Tuxt <tuxt@protonmail.com>"
    __version__ = "1.1.1"
    __license__ = "GPL3"
    __description__ = "MAX17048-based battery manager"

    def __init__(self):
        self.battery = MAX17048()
    
    def on_loaded(self):
        logging.info("[BatteryManager] Plugin loaded")

    def on_ready(self, agent):
        logging.info("[BatteryManager] Plugin ready")
    
    def on_unload(self, ui):
        with ui._lock:
            ui.remove_element("battery")
        logging.info("[BatteryManager] Plugin unloaded")
    
    def on_ui_setup(self, ui):
        with ui._lock:
            ui.add_element(
                "battery",
                LabeledValue(
                    color=BLACK,
                    label=self.options.get("label", "BAT"),
                    value="-",
                    position=(ui.width() / 2 + self.options.get("x_offset", 14), self.options.get("y_offset", 0)),
                    label_font=fonts.Bold,
                    text_font=fonts.Medium,
                ),
            )
    
    def on_ui_update(self, ui):
        ui.set("battery", self._get_info())
    
    def with_charge(func):
        state = {"last_voltage": 5, "charging": False}
        def wrapper(self, *args, **kwargs):
            info = func(self, *args, **kwargs)
            if not self.options.get("show_charge_icon", False):
                return info
            
            new_voltage = self.battery.cell_voltage
            diff = new_voltage - state["last_voltage"]
            if abs(diff) > 0.1:
                state["charging"] = diff > 0
            state["last_voltage"] = new_voltage
            
            icon = self.options.get("charge_icon", "⚡") if state["charging"] else ""
            return info + icon
        return wrapper
    
    @with_charge
    def _get_info(self):
        info = self.options.get("format", "percent")
        percent_precision = self.options.get("percent_precision", 0)
        voltage_precision = self.options.get("voltage_precision", 2)

        if info == "percent":
            return f"{self.battery.cell_percent:.{percent_precision}f}%"
        elif info ==  "voltage":
            return f"{self.battery.cell_voltage:.{voltage_precision}f}V"
        elif info ==  "both":
            return f"{self.battery.cell_percent:.{percent_precision}f}% ({self.battery.cell_voltage:.{voltage_precision}f}V)"
