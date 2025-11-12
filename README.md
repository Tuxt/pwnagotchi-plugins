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
sudo su
source .pwn/bin/activate
pip install MAX17048-smbus
pwnagotchi plugins install batman
systemctl restart pwnagotchi
```

### Options

Add the necessary lines to `/etc/pwnagotchi/config.toml`

Required:

```toml
main.plugins.batman.enabled = true
```

Optional:

```toml
main.plugins.batman.x_offset = 15           # X-offset from the center of the screen
main.plugins.batman.y_offset = 0            # Y-offset from the top of the screen
main.plugin.batman.label = "BAT:"           # Label for the battery info
main.plugins.batman.percent_precision = 0   # Decimal precision for percentage
main.plugins.batman.voltage_precision = 2   # Decimal precision for voltage
main.plugins.batman.format = "percent"      # Data to print: "percent" | "voltage" | "both"
```





