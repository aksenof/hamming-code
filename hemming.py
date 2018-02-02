from math import *
 
def log_func(f):  # функция для поиска кол-ва проверочных символов
    return ceil(log2(f + 1 + ceil(log2(f + 1))))
 
def invert(bol):  # функция инвертирования 1 в 0 и наоборот
    return 0 if bol == 1 else 1
 
def check_even(number):  # функция проверки на четность/нечетность
    return 0 if number % 2 == 0 else 1
 
def place(position):  # функция распределения чисел в закодированном сообщении
    position += 1
    step = log_func(position)
    new_position = (position+step) - 1
    return new_position
 
def search(index, mas, bins):  # функция поиска единиц в разрядах
    return check_even(sum(list(mas[bins.index(i)] for i in bins if i[index] == "1")))
 
def check_error(er, cod):  # функция проверки на наличие ошибки
    if er == 0:
        print("error not found")
        print("decode message: ", cod)
        exit()
    else:
        return 0
 
data = input("enter your data: ")
lst = list(int(i) for i in data)
print("data  in  list: ", lst)
k = len(lst)  # количество информационных разрядов
p = log_func(k)  # количество проверочных символов
lob = log_func(k)  # максимальная длина бинарных индексов
n = k+p  # общая длина закодированного сообщения
#  print("numbers of data bits: ", k)
#  print("numbers of check symbols: ", p)
#  print("length of encode message: ", n)
x = "x"*n
code = list(i for i in x)
for j in range(len(lst)):
    code[place(j)] = lst[j]
#  print("check symbols <x> : ", code)
 
b = lambda numb: str("{0:0"+"{}".format(lob)+"b}").format(numb)
bin_list = list(b(i) for i in range(1, len(code)+1))  # лист бинарных индексов
#  print(bin_list)
 
x_bin_list = bin_list.copy()
for i in range(p):
    x_bin_list[(2**i)-1] = "x"*lob  # лист бинарных индексов без индексов проверочных символов
#  print(x_bin_list)
 
check_symbols_list = list(search(i, code, x_bin_list) for i in range(p))
check_symbols_list.reverse()  # лист проверочных символов
#  print(check_symbols_list)
 
for i in range(p):
    code[(2**i)-1] = check_symbols_list[i]   # закодированное сообщение
print("encode message: ", code)
 
error = int(input("number of error: "))
check_error(error, lst)
ercode = code.copy()
ercode[error-1] = invert(code[error-1])  # сообщение с ошибкой
print("error  message: ", ercode)
 
syndrome_list = list(str(search(i, ercode, bin_list)) for i in range(p))
syndrome = "".join(syndrome_list)  # синдром
print("syndrome: ", syndrome)
 
ind = bin_list.index(syndrome)+1  # номер индекса в котором произошла ошибка
print("error in number: ", ind)
 
fixcode = ercode.copy()
fixcode[ind-1] = invert(ercode[ind-1])   # исправленное сообщение
print("fixed  message: ", fixcode)
 
for j in list(i for i in range(p))[::-1]:
    del fixcode[(2**j)-1]
print("decode message: ", fixcode)  # декодированное сообщение
