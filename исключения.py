#print(10 / 0)
#print(a) - NameError
#Int('ghgjj') - ValueError
#print("232" + "5245") - TypeError


try:
    print(gfyguy / jhuhi)
except ZeroDivisionError:
    print("На 0 делить нельзя!")
except NameError:
    print("Переменная не задана!")
except  ValueError:
    print("Невозможно привести к целому числу!")
except  TypeError:
    print("Ошибка типа данных!")
except:
    print("Произошла ошибка!!!")
