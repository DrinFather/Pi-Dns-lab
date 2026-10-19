#!/usr/bin/env python3
"""
dns_analyzer.py: flags interesting domains in Pi-hole's query log.

Author: Adrian Kamutu
Status: NOT STARTED. This file is a placeholder. Write it yourself, no tutorial.

What it should do:
  1. Read the Pi-hole query log (or a sanitized sample file)
  2. Pull the domain out of each query line
  3. Report:
       - the 10 most-queried domains
       - domains that didn't appear in earlier runs
       - domains that look randomly generated

Usage (once it's written):
    python3 scripts/dns_analyzer.py sample-data/sample_queries.txt
"""


def main():
    # TODO Step 1: open the file named on the command line and print each line
    # TODO Step 2: pull the domain out of lines that are DNS queries
    # TODO Step 3: count the domains and print the top 10
    # TODO Step 4: remember domains between runs and flag new ones
    # TODO Step 5: flag random-looking domains
    print("Not written yet. See docs/02-log-analysis.md for the plan.")


if __name__ == "__main__":
    main()
