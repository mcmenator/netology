def solve(phrases: list):
    result = [] # список палиндромов    
    for phrase in phrases: # пройдите циклом по всем фразам
        text = phrase.replace(' ', "") # сохраните фразу без пробелов
        if text == text[::-1]: # сравните фразу с ней же, развернутой наоборот (через [::-1])
           result.append(phrase)
    return result