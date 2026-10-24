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

## 2026-10-23: Finding the Pi from my laptop, and an outage

Goal: Practice looking at the network from my Windows laptop, find the Pi's IP myself, and SSH in.

**What I did:**
- Worked on finding the Pi's IP from PowerShell: checked my own IP and subnet, listed known devices, and filtered them by the Raspberry Pi MAC prefix
- Tried to SSH in and got `Connection timed out`
- Checked the Tailscale app on my phone, which showed the Pi as offline, so the problem was the Pi and not my laptop
- Restarted the Pi, and SSH worked again

**Commands worth remembering (Windows PowerShell):**
```powershell
ipconfig                                   # my IP, subnet mask, gateway
arp -a                                     # devices my laptop knows about
1..254 | ForEach-Object { ping -n 1 -w 100 "192.168.X.$_" | Out-Null }   # ping sweep to fill the ARP table
arp -a | Select-String "2c-cf-67|d8-3a-dd" # Raspberry Pi MAC prefixes
ping -4 <hostname>.local                   # find the Pi by hostname
Test-NetConnection <pi-ip> -Port 22        # is SSH reachable?
```

**What broke and how I fixed it:**
- SSH timed out. A timeout means no reply at all (wrong IP or device offline), unlike `Connection refused` (device is up but SSH isn't running) or `Permission denied` (wrong username or key). The Tailscale app showing "offline" confirmed the Pi had dropped off the network. Fix: restarted the Pi. Root cause not found yet.

**Next time:**
- Check for power problems: `vcgencmd get_throttled` (`0x0` means fine)
- Turn off Wi-Fi power saving permanently with `nmcli`, since `iw` resets on reboot
- Find out why it dropped: `last -x | head` shows reboots and shutdowns