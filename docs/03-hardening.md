# Phase 3: Hardening

**Goal:** Lock down the Pi the way you would a real server, then check who has been trying to get in.


## Checklist

### SSH
- [ ] Confirm key login works from my laptop
- [ ] Turn off password logins (`PasswordAuthentication no`). Check `/etc/ssh/sshd_config` **and** the files in `/etc/ssh/sshd_config.d/`
- [ ] Restart SSH, then test in a **second** terminal before closing the first one

### Firewall (ufw)
- [ ] Install ufw
- [ ] Allow SSH (22/tcp), DNS (53 tcp and udp) and the Pi-hole web admin (80/tcp, 443/tcp). Ideally allow them only from my home network range.
- [ ] Allow traffic on the Tailscale interface (`sudo ufw allow in on tailscale0`) so SSH, DNS and Cockpit (9090/tcp) keep working over Tailscale. Don't open 9090 to the house network.
- [ ] Turn ufw on, then confirm SSH and DNS still work, both on Wi-Fi and over Tailscale
- [ ] Save the output of `sudo ufw status verbose` to `configs/`

### fail2ban
- [ ] Install fail2ban and enable the `sshd` jail in `/etc/fail2ban/jail.local`
- [ ] If it won't start because a log file is missing, set `backend = systemd` for that jail
- [ ] Check that it's running: `sudo fail2ban-client status sshd`

### Review login attempts
- [ ] Look through the SSH login history. Current Raspberry Pi OS may not have `/var/log/auth.log`, so use `journalctl -u ssh` instead.
- [ ] Note what you find: successful logins, failed attempts, anything unexpected

## What I actually did

_…_

## Problems & fixes

| Problem | Cause | Fix |
|---|---|---|
| _…_ | _…_ | _…_ |

## Screenshots

_…_
