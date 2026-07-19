def convert(command):

    command = command.lower().strip()

    parts = command.split()

    if len(parts) != 4 or parts[2] != "to":
        return None

    try:
        value = float(parts[0])
    except:
        return None

    from_unit = parts[1]
    to_unit = parts[3]

    conversions = {

        ("km", "m"): value * 1000,
        ("m", "km"): value / 1000,

        ("cm", "m"): value / 100,
        ("m", "cm"): value * 100,

        ("kg", "g"): value * 1000,
        ("g", "kg"): value / 1000,

        ("hour", "minutes"): value * 60,
        ("minutes", "hour"): value / 60,

        ("min", "sec"): value * 60,
        ("sec", "min"): value / 60,

    }

    result = conversions.get((from_unit, to_unit))

    if result is None:
        return None

    return f"{value} {from_unit} = {result} {to_unit}"