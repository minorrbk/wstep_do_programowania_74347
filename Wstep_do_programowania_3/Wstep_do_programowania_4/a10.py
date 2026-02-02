def hanoi(n, miejsce, cel, pomocniczy):

    if n == 1:
        print(f"Przenieś krążek 1 z {miejsce} na {cel}")
        return

    hanoi(n - 1, miejsce, pomocniczy, cel)

    print(f"Przenieś krążek {n} z {miejsce} na {cel}")

    hanoi(n - 1, pomocniczy, cel, miejsce)

liczba_krazkow = 4
print(f"--- Rozwiązanie dla {liczba_krazkow} krążków ---")
hanoi(liczba_krazkow, 'A', 'C', 'B')