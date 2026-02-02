from datetime import datetime


def raport_czasu(data_lab, data_kolokwium):
    teraz = datetime.now()

    def formatuj(dt):
        return dt.strftime("%d %B %Y")

    print(f"Dzisiaj jest: {formatuj(teraz)}")

    delta_lab = teraz - data_lab
    print(f"Od laboratoriów ({formatuj(data_lab)}) minęło: {delta_lab.days} dni.")

    delta_kol = data_kolokwium - teraz

    if delta_kol.days >= 0:
        print(f"Do kolokwium ({formatuj(data_kolokwium)}) zostało: {delta_kol.days + 1} dni.")
    else:

        print(f"Termin kolokwium ({formatuj(data_kolokwium)}) minął {abs(delta_kol.days)} dni temu.")

lab_str = "17.01.2026"
kol_str = "30.01.2026"

data_lab = datetime.strptime(lab_str, "%d.%m.%Y")
data_kol = datetime.strptime(kol_str, "%d.%m.%Y")

# Uruchomienie
raport_czasu(data_lab, data_kol)