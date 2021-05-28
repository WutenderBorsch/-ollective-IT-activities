import re

#TODO: Написать регулярное выражение для проверки адреса электронной почты. 
#В электронном адресе допустимы латинские символы верхнего и нижнего регистров, цифры, точки, дефисы, подчёркивания.

trueValue = "a@b.c, a-b@c.d.e, a-b_c.d@e_f-g.h"
falseValue = "a+@b.c, a_b.c, a_b@.c-d>"

for str in trueValue.split(", "):
    result = re.findall(r'([a-z-._0-9]+@[a-z-_0-9]+\.[a-z-_0-9])', str)
    if len(result) != 0:
        print(result)


#TODO: Написать регулярное выражение, которое из текстовой строки выделяет положительное десятичное число. 
#Число может содержать дробную часть, отделяемую точкой. Число должно отделяться от текста пробелами.
        
trueVal = "some text 5678.23 some text, some text 0 some text, some text 0.15 some text"
falseVal = "some text123some text, text 123,4 text, text -123.4 text, text - text"

print()
result = re.findall(r' ([0-9]+|[0-9]+\.[0-9]+) ', trueVal)
for str in result:
    print(str)


#TODO:Из кода html-страницы выделить тег img (изображение) со всем его содержимым.

trueStr = "<a href=\"/a/index.php\" target=\"_blank\"><img alt=\"title\" src=\"http://test/image.png\"></a>" 
falseStr = "<a href=\"/a/index.php\" target=\"_blank\"><img alt=\"title\"></a>"

print()
for str in trueStr.split(", "):
    result = re.findall(r'<img ((alt|src)="[^"]*" (alt|src)="[^"]*")>', str)
    if len(result) != 0:
        print(result[0][0])

# <img ((alt=|src=)"[^"]+ (alt=|src=)"[^"]+)>