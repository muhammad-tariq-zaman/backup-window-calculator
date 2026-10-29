"""Compute maximum data-loss window (RPO) from a backup interval in hours.

Usage: python3 main.py --interval-hours 24
Also prints the number of backups per week for that interval.
"""
import argparse
import sys


def window_hours(interval):
    return interval


def per_week(interval):
    return int(7 * 24 // interval) if interval else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--interval-hours", type=float, required=True)
    args = parser.parse_args(argv)
    if args.interval_hours <= 0:
        parser.error("interval must be positive")
    print(f"Backup every {args.interval_hours:g}h -> max data loss {window_hours(args.interval_hours):g}h, {per_week(args.interval_hours)} backups/week")
    return 0


if __name__ == "__main__":
    sys.exit(main())
