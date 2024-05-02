# 1 příklad
# x = -5
# if x < 0:
#     raise Exception("x should be positive.")

# 2. příklad
# x1 = -5
# assert (x1 >= 0)   # AssertionError


# 3. příklad
# x1 = -5
# assert (x1 >= 0), "x is not positive"

# 4. příklad
# try:
#     a = 5 / 0
# except:
#     print("An error happened")

# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)   # division by zero


# 5. Příklad
try:
    a = 5 / 1
    b = a + "10"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)   # unsupported operand type(s) for +: 'float' and 'str'
else:
    print("Everything is fine")    # zobrazí se v případě, že kód se nevyskytne except error
finally:
    print("Cleaning up....")
