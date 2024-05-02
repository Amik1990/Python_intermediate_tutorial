# %, .format(), f-Strings

# %, .format() jsou starší způsoby zápisu. Nově se spíše používá f-strings
var = "Tom"
my_string = "the variable is %s" % var    # %s je ukotvení stringu
print(my_string)    # the variable is Tom

var = 3
my_string = "the variable is %d" % var    # %d je ukotvení integeru
print(my_string)    # the variable is 3

var = 3.05252
my_string = "the variable is %d" % var    # %d je ukotvení integeru. Ikdyž máme float, tak se zobrazí integer
print(my_string)   # the variable is 3

var = 3.05252
my_string = "the variable is %f" % var    # %f je ukotvení float
print(my_string)   # the variable is 3.052520

var = 3.05252
my_string = "the variable is %.2f" % var    # %.2f je ukotvení float, který se zaokrohlí na dvě desetinná místa
print(my_string)   # the variable is 3.052


# Použití .format()
var = 3.05252
my_string = "the variable is {}".format(var)
print(my_string)   # the variable is 3.052520

var = 3.05252
my_string = "the variable is {:.2f}".format(var)
print(my_string)   # the variable is 3.05

var = 3.05252
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string)   # the variable is 3.05 and 6


# Použití f-strings
var = 3.05252
var2 = 6
my_string = f"the variable is {var} and {var2}"
print(my_string)  # the variable is 3.05252 and 6

var = 3.05252
var2 = 6
my_string = f"the variable is {var*2} and {var2}"
print(my_string)  # the variable is 6.10504 and 6


