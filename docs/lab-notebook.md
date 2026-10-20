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