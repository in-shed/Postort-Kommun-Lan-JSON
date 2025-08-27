# Postort-Kommun-Lan-JSON

Postort–Kommun–Län JSON

This repository provides a tool for exporting JSON of Swedish Postort-Kommun-Län mappings.
Data should be sourced from https://raw.githubusercontent.com/Axelsson2000/data/master/Postort-Kommun-Lan.csv 

The script can convert data into three different JSON structures, depending on your use case.

Flat json:
```json
[
  {
    "Postort": "Alafors",
    "KnNamn": "Ale kommun",
    "KnNamnKort": "Ale",
    "KnKod": 1440,
    "LnNamn": "Västra Götalands län",
    "LnNamnKort": "Västra Götaland",
    "LnKod": 14,
    "LnBokstav": "O"
  }
]
```
By Postort:
```json
{
  "Alafors": {
    "KnNamn": "Ale kommun",
    "KnNamnKort": "Ale",
    "KnKod": 1440,
    "LnNamn": "Västra Götalands län",
    "LnNamnKort": "Västra Götaland",
    "LnKod": 14,
    "LnBokstav": "O"
  },
  "Älvängen": {
    "KnNamn": "Ale kommun",
    "KnNamnKort": "Ale",
    "KnKod": 1440,
    "LnNamn": "Västra Götalands län",
    "LnNamnKort": "Västra Götaland",
    "LnKod": 14,
    "LnBokstav": "O"
  }
}
```

Hierarchecal conversion:
```json
{
  "Västra Götalands län": {
    "Ale kommun": {
      "KnKod": 1440,
      "LnKod": 14,
      "LnBokstav": "O",
      "Postorter": [
        "Alafors",
        "Älvängen",
        "Alvhem",
        "Bohus",
        "Hålanda",
        "Nödinge",
        "Nol",
        "Skepplanda",
        "Surte"
      ]
    }
  }
}
```
