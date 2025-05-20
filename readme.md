# Vogel Ringer

This script generates 4-letter bird ring IDs using a station letter and additional ring color letters. The output is sorted alphabetically.

## Usage

```bash
python3 ringer.py <station_letter> <letters>
```

Example:

```bash
python3 ringer.py M RLYB
```

This will output all combinations that contain exactly one occurrence of the station letter `M` and three letters chosen from `M` + `RLYB`.

