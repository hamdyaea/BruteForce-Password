# Offline password enumeration demo

Developer: Hamdy Abou El Anein — hamdy.aea@protonmail.com

Python standard library only. `python3 BruteForce.py --demo 00 --max-attempts 100000` demonstrates enumeration against a toy string. No network, authentication service, hash dump or credential store is accessed. Do not enter real passwords. Attempts are bounded to at most one million; unsupported characters fail immediately. Leading zero characters are correctly enumerated.

Run `python3 -m unittest -v` for five offline regression tests.
