# backup-window-calculator

Work out the maximum data-loss window and backups per week from a backup interval, for RPO planning.

## How to run

```sh
python3 main.py --interval-hours 24
```

## Example output

```
Backup every 24h -> max data loss 24h, 7 backups/week
```

Standard library only. Run the tests with `python3 -m unittest discover`.
