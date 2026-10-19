# Phase 2: Log analysis

**Goal:** Write my own Python script, without a tutorial, that reads Pi-hole's query log and flags:
1. The domains my devices look up most
2. Domains that have never shown up before
3. Domain names that look random (a common sign of malware)

## Step 1: Look at the raw data first

Before writing any code, look at what you'll be parsing:

```bash
ls /var/log/pihole/                          # find the query log (pihole.log on Pi-hole v6)
sudo tail -n 20 /var/log/pihole/pihole.log   # last 20 lines
sudo tail -f /var/log/pihole/pihole.log      # live view, Ctrl+C to stop
```

Paste 3–4 real lines here and label each part (time, query type, domain, which device):

```
(paste example lines here, with your device IPs replaced by 192.168.X.X)
```

## Step 2: Plan before coding

Write out in plain English what the script does, step by step:

1. _…_
2. _…_
3. _…_

## Step 3: Build it one piece at a time

- [ ] Read the file and print every line
- [ ] Pull just the domain name out of each query line
- [ ] Count domains and print the top 10
- [ ] Save "domains seen so far" to a file, and flag new ones on the next run
- [ ] Decide what "random-looking" means and flag those (look up how analysts spot **DGA** domains)
- [ ] Test it on a sanitized sample in `sample-data/`

## Results

_What did it find? Paste sanitized sample output here._

## What I'd improve

_…_
