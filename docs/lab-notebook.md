## 2026-10-19: Session 1: First boot and SSH

Goal: Flash the SD card, boot the Pi, and SSH in from my laptop.

**What I did:**
- Generated an ed25519 SSH key on my laptop
- Flashed the SD card with Raspberry Pi Imager (ended up with the full desktop version of Raspberry Pi OS instead of Lite)
- Booted the Pi on house Wi-Fi and checked it on a monitor
- Turned on SSH and connected from my laptop over Wi-Fi
- Set the Pi to boot to the text console to save RAM (raspi-config → System Options → Boot → Console)

**Commands worth remembering:**
```bash
ssh-keygen -t ed25519
hostname -I
whoami
sudo systemctl enable --now ssh
sudo raspi-config
```

**What broke and how I fixed it:**
- Typed the `cat` command at ssh-keygen's "save to file" prompt, so the key never saved. Fix: reran it and pressed Enter at that prompt.
- SSH said `Permission denied` because I used my Windows username instead of the Pi's. Fix: ran `whoami` on the Pi and used that name.
- Opened Wireless LAN in raspi-config by mistake (it asked for an SSID). Fix: backed out, since the Pi was already on Wi-Fi.

**Next time:**
- Copy my SSH key to the Pi so I can log in without the password
- Install Pi-hole and point my laptop's DNS at it

## 2026-10-21: Remote access with Tailscale and Cockpit

Goal: Use Pi-hole on my phone, and be able to check on the Pi from my phone from anywhere. Details in [04-remote-access.md](04-remote-access.md).

**What I did:**
- Tried setting my iPhone's Wi-Fi DNS to the Pi's Wi-Fi IP. The phone lost internet, so I set it back to Automatic.
- Installed Tailscale on the Pi and my iPhone, so the Pi has a `100.x.x.x` address I can reach from anywhere
- Installed Cockpit and logged in from Safari on my phone at `https://<tailscale-ip>:9090`
- Started setting up Pi-hole as the DNS server for my whole tailnet

**Commands worth remembering:**
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
tailscale ip -4
ip -4 -br addr show wlan0
sudo apt install cockpit
systemctl status cockpit.socket
sudo tailscale set --accept-dns=false
```

**What broke and how I fixed it:**
- iPhone said "No Internet Connection" with its DNS pointed at the Pi. Cause not confirmed (IP change, client isolation, different subnet, or Pi-hole's interface setting). Fix: set it back to Automatic and moved to Pi-hole over Tailscale.
- `hostname -I` showed several IPs. Fix: `tailscale ip -4` shows just the Tailscale one.
- Cockpit asked for the "server user account". Fix: that's the Pi's own Linux login, not Tailscale or Pi-hole.

**Next time:**
- Finish Pi-hole over Tailscale and check that my phone's queries show up in the Query Log
- Disable key expiry for the Pi in the Tailscale admin console
- Set up Termius and a healthchecks.io alert