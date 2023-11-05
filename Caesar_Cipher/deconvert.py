import sympy.core.numbers

def inRange (range, language): #Цикличность алфавита
    if language == "Ru":
        displace = 33
    else: displace = 26
    if range >= displace:
        range -= displace
    return range

def main(language, message, displace):
    if message == '':
        return "No message"
    if not displace.isnumeric():
        return "Wrong step"
    displace = int(displace)
    result = '' 
    flag = False
    
    if language == "Ru": #Выбор алфавита + сокращение шага
        alpha_up =  'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        alpha_low = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        while displace >= 33:
            displace = displace - 33
    elif language == "En":
        alpha_up =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alpha_low = 'abcdefghijklmnopqrstuvwxyz'
        while displace >= 26:
            displace = displace - 26
    
    for i in message: #Выбор символов через шаг
        place_up = alpha_up.find(i)
        new_place_up = place_up - displace
        place_low = alpha_low.find(i)
        new_place_low = place_low - displace
        new_place_low = inRange(new_place_low, language)
        new_place_up = inRange(new_place_up, language)
        if i in alpha_up: #Сборка результата
            result += alpha_up[new_place_up] 
            flag = True
        elif i in alpha_low:
            result += alpha_low[new_place_low] 
            flag = True
        else:
            result += i
    if flag:
        return result
    return "Wrong message"