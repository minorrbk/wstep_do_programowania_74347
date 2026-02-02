import keyword

slowa = ["for", "print", "break", "done", "bad"]

print(f"{'Słowo':<10} {'Czy jest słowem kluczowym?':<25}")

for slowo in slowa:

    jest_kluczowe = keyword.iskeyword(slowo)
    print(f"{slowo:<10} {str(jest_kluczowe)}")