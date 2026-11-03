#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
"""Bounded, offline demonstration using a caller-supplied toy password."""
import argparse
from itertools import product
import string

DEFAULT_ALPHABET = string.digits + string.ascii_lowercase[:20]


def find_password(password, alphabet=DEFAULT_ALPHABET, max_attempts=100000):
    if not alphabet or len(set(alphabet)) != len(alphabet):
        raise ValueError("Alphabet must contain unique characters.")
    if not 1 <= max_attempts <= 1000000:
        raise ValueError("Attempt limit must be between 1 and 1000000.")
    if any(character not in alphabet for character in password):
        raise ValueError("Password contains characters outside the alphabet.")
    if not password:
        return "", 0
    attempts = 0
    for length in range(1, len(password) + 1):
        for candidate in product(alphabet, repeat=length):
            attempts += 1
            word = "".join(candidate)
            if word == password:
                return word, attempts
            if attempts >= max_attempts:
                return None, attempts
    return None, attempts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", default="00", help="Toy string only; do not enter a real password")
    parser.add_argument("--max-attempts", type=int, default=100000)
    args = parser.parse_args()
    try:
        found, attempts = find_password(args.demo, max_attempts=args.max_attempts)
    except ValueError as exc:
        parser.error(str(exc))
    print(f"{'Found' if found is not None else 'Limit reached'} after {attempts} attempts.")
    return 0 if found is not None else 1


if __name__ == "__main__":
    raise SystemExit(main())
