import secrets
# má pouze 3 funkce. Používá se pro přihlašování, ověření identity atd

a = secrets.randbelow(10)   # vygeneruje  číslo do 10. 10 se nepočítá.
print(a)
a = secrets.randbits(4)   # vygeneruje  4 bitove číslo. Max je 15 u 4 bitoveho čísla
print(a)

mylist = list("ABCDEFGH")
a = secrets.choice(mylist)   # vygeneruje jednu hodnoty z listu, která není reprodukovatelná
print(a)

