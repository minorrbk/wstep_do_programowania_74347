def odwroc(tekst):

    if len(tekst) == 0:
        return tekst

    return odwroc(tekst[1:]) + tekst[0]

s = "minorbarton"
print(odwroc(s))