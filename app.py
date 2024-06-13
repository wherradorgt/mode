import mode

json = [
    {
        "operator": "mode",
        "columns": ["ENG_SPEED", "DEF_LEVEL","ENG_COOLANT_TEMP"]
    }
]
print(mode.getMode(json))