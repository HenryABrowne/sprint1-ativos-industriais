def converter_sensor(sensor, valor_bruto):
    if sensor == "corrente":
        return round(valor_bruto * 0.0035, 2), "A"

    if sensor == "tensao":
        return round(valor_bruto * 0.1, 2), "V"

    if sensor == "rpm":
        return round(valor_bruto * 0.34, 0), "RPM"

    if sensor == "vibracao":
        return round(valor_bruto * 0.003, 2), "mm/s"

    return valor_bruto, "unidade"