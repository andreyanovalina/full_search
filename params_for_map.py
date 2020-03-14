def params_for_map(toponym_coodrinates, delta, type):
    return {
        "ll": ",".join(toponym_coodrinates.split(" ")),
        "spn": delta,
        "l": type,
        "pt": toponym_coodrinates.split(" ")[0] + ',' + toponym_coodrinates.split(" ")[1] + ",pmrdm1"
    }
