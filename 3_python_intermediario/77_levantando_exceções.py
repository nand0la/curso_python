def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as error:
        print(error)
        raise 


try:
    print(divide(10, 0))
except ZeroDivisionError as error:
    pass    
