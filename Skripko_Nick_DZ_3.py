# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
#
# num_dict = {'zero': 'ноль',
#             'one': 'один',
#             'two': 'два',
#             'three': 'три',
#             'four': 'четыре',
#             'five': 'пять',
#             'six': 'шесть',
#             'seven': 'семь',
#             'eight': 'восемь',
#             'nine': 'девять',
#             'ten': 'десять'}
#
#
# def num_translate(num_word):
#     return num_dict.get(num_word)
#
#
# print(num_translate('eight'))
#
#
# 2.* Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
#
#
# def num_translate_adv(num_word):
#     word = num_dict.get(num_word.lower())
#     if word:
#         return word.capitalize() if num_word[0].isupper() else word
#     return None
#
#
# print(num_translate_adv('Nine'))
#
#
# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

# Выполнил после разбора


def thesaurus(*names):
    new_dict = dict()
    for name in names:
        new_dict.setdefault(name[0], [])
        new_dict[name[0]].append(name)
    return new_dict


print(thesaurus('Николай', 'Наталья', 'Иван', 'Кирилл', 'Анастасия'))

# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

# import random
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# def get_jokes(word):
#     joke_list = []
#     for i in range(word):
#         ch_nouns = random.choice(nouns)
#         ch_adverbs = random.choice(adverbs)
#         ch_adjectives = random.choice(adjectives)
#         joke_list.append(f'{ch_nouns} {ch_adverbs} {ch_adjectives}')
#     return joke_list
#
#
# print(get_jokes(3))

# Выполнил после разбора

# def get_jokes_adv(word, repeat = True):
#     joke_list = []
#
#     if not repeat:
#         if word > min(len(nouns), len(adverbs), len(adjectives)):
#             return 'Нет вариантов'
#         else:
#             random.shuffle(nouns)
#             random.shuffle(adverbs)
#             random.shuffle(adjectives)
#             for i in range(word):
#                 joke_list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
#
#     else:
#         for i in range(word):
#             ch_nouns = random.choice(nouns)
#             ch_adverbs = random.choice(adverbs)
#             ch_adjectives = random.choice(adjectives)
#             joke_list.append(f'{ch_nouns} {ch_adverbs} {ch_adjectives}')
#     return joke_list
#
#
# print(get_jokes_adv(6))