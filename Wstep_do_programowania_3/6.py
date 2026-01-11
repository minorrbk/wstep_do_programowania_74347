prad = {"styczen" : 952, "luty" : 738, "marzec" : 821, "kwiecien" : 412}

maks = max(prad.values())
print(f"najwieksza wartosc to: {maks}zł")

najmniejszy = min(prad.values())
print(f"najmniejsza wartość to: {najmniejszy}zł")

sredni = sum(prad.values()) / len(prad)
print(f"srednia wartosc to: {sredni:.2f}zł")

wartoscprad = list(prad.values())


if sredni < wartoscprad[2]:
    print("Trzeba zacisnąć pasa")
else:
    print("jest luz")