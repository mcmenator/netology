def solve(phrases: list):
    result = [] # список палиндромов    
    for phrase in phrases: # пройдите циклом по всем фразам
        text = phrase.replace(' ', "") # сохраните фразу без пробелов
        if text == text[::-1]: # сравните фразу с ней же, развернутой наоборот (через [::-1])
           result.append(phrase)
    return result

def solve(cook_book: list, person: int):
    result = []
    # самостоятельно напишите код решения:
    for i in cook_book:
        res_i=(f'{i[0]}: ')
        for j in i[1]:
            res_i+=(f'{j[0]} {j[1]*person} {j[2]}, ')
        result.append(res_i[0:-2])
    return result