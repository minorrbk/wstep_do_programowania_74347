#a

Imiona = ["seba", "damian", "lucas", "dawid"]
alfabet = sorted(Imiona)

print(alfabet)

#b

alfabet.extend(["kamil", "mikołaj"])
alfabet.pop(5)
print (alfabet)



#C
alfabet.insert(2, "gumis")
print(alfabet)

#d
alfabet.reverse()
alfabet = alfabet * 2
print(alfabet)