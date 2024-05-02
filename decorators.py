def start_end_decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper


@start_end_decorator    # funkci print_name() jsme přidali funkcionalitu funkce start_end_decorator
def print_name():
    print("Alex")


# print_name = start_end_decorator(print_name)    # print_name funkci jsem přidal funkcionalitu funkce start_end_decorator
print_name()                    # jednodušší je ale napsat nad funkci print_name tohle: @start_end_decorator


