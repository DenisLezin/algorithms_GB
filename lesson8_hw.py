
import hashlib
from pympler import asizeof

word = input('Введите строку: ')

def get_substrings(word):
    '''
    :param word: на вход принимает строку
    :return: возвращает набор подстрок без перестановки
    '''
    res = []
    res_forward = [word[i:] for i in range(len(word))]   # в каждой итерации убираем первую букву
    for elm in res_forward:
        res += [elm[:len(elm) - i] for i in range(len(elm))
                if elm[:len(elm) - i] != word and elm[:len(elm) - i] not in res]  # для каждого эемента убираем
                                                                                  # последнюю букву и конкатенируем
    return res                                                                    # с результирующим списком


res = get_substrings(word)
res_hash = [hashlib.sha1(i.encode('utf-8')).hexdigest() for i in res]

print(f'\nВведенная строка: {word}\n'
      f'Всего подстрок: {len(res)}\n'
      f'Список подстрок: {res}\n'
      f'Хеш-список подстрок: {res_hash}\n\n'
      f'Просто ради интереса (понимаю что хэш может быть использован для быстрого поиска)\n'
      f'Список подстрок занимает {asizeof.asizeof(res)} байт\n'
      f'Хэш-список - {asizeof.asizeof(res_hash)} байт\n'
      f'Множество подстрок - {asizeof.asizeof(set(res))} байт')



# def spliter(word):
#     res_forward = [word[i:] for i in range(len(word))]
#     res_backward = [word[:len(word) - i] for i in range(len(word))]
#     return res_forward + res_backward
#
#
# res_forw = [word[i:] for i in range(len(word))]
# res_bakw = [word[:len(word) - i] for i in range(len(word))]
# res_concat = spliter(word)
#
# res1 = []
# res2 = [spliter(j) for j in spliter(word)]
#
# for j in spliter(word):
#     # res1 += [j[i:] for i in range(len(j))]
#     res1 += spliter(j)
#
# # res_hash = [hashlib.sha1(i.encode('utf-8')).hexdigest() for i in res]
#
# print(res_forw)
# print(res_bakw)
# print(res_concat)
# print(res1)
# print(len(set(res1)))
# print(set(res1))
# print(res2)
# # print(res_hash)
