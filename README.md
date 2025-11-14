# pwnagotchi-plugins

Custom plugins for pwnagotchi


Add the repository to the `/etc/pwnagotchi/config.toml` file:

```toml
main.custom_plugin_repos = [
    "https://github.com/Tuxt/pwnagotchi-plugins/archive/master.zip",
]
```

And run:
```bash
sudo pwnagotchi plugins update
```

## BatMan

Battery Manager for MAX17048-based power supply

### Installation

```bash
cd ~
sudo bash -c 'source .pwn/bin/activate && pip install MAX17048-smbus'
sudo pwnagotchi plugins install batman
```

### Configuration

Add the necessary lines to `/etc/pwnagotchi/config.toml`

Required:

```toml
main.plugins.batman.enabled = true
```

Optional:

```toml
main.plugins.batman.x_offset = 14               # X-offset from the center of the screen
main.plugins.batman.y_offset = 0                # Y-offset from the top of the screen
main.plugin.batman.label = "BAT"                # Label for the battery info
main.plugins.batman.percent_precision = 0       # Decimal precision for percentage
main.plugins.batman.voltage_precision = 2       # Decimal precision for voltage
main.plugins.batman.format = "percent"          # Data to print: "percent" | "voltage" | "both"
main.plugins.batman.show_charge_icon = false    # Show an icon when device is charging
main.plugins.batman.charge_icon = "⚡"          # Icon to indicate the device is charging
```

> The example values ​​are the default values.

Finally, restart the service:

```bash
sudo systemctl restart pwnagotchi
```

### 🧾 Changelog

#### [1.1.1] - 2025-11-14
##### Fixed
- Adjusted the voltage threshold for charger detection from 0.05V to 0.1V to reduce false positives during battery-only operation.

#### [1.1.0] - 2025-11-13
##### Added
- Added an optional charging indicator to show when the device is charging.

#### [1.0.0] - 2025-11-12
##### Initial release
- Initial version of the plugin.