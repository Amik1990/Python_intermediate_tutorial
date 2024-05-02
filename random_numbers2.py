import random   # nedoporučuje se používát při bezpečnostních záležitostech. Na to je lepší modul secrets.


random.seed(1)    # funguje jako kotva pro zapamatování vygenerovaných čísel
print(random.random())  # vygeneruje náhodné float číslo
print(random.randint(1, 10))  # vygeneruje náhodné integer číslo

random.seed(2)    # funguje jako kotva pro zapamatování vygenerovaných čísel
print(random.random())  # vygeneruje náhodné float číslo
print(random.randint(1, 10))


random.seed(1)   # vygeneruje stejná čísla jako minule u seed(1)
print(random.random())
print(random.randint(1, 10))
