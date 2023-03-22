geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55,
         'yandex': 120,
         'vk': 115,
         'google': 99,
         'email': 42,
         'ok': 98
         }


def get_visit_russia(geo_logs):
    geo_logs_russia = []
    for elem in range(0, len(geo_logs)):
        if 'Россия' in list(geo_logs[elem].values())[0]:
            geo_logs_russia.append(geo_logs[elem])
    return geo_logs_russia


def get_unic_id(ids):  # Выводит на экран все уникальные гео-ID из значе ний словаря ids
    list_1 = []
    for key, value in ids.items():
        list_1 += value
    return list(set(list_1))


def name_channal_max(stats):    # Возвращает название канала с максимальным объемом
    res = max(stats, key=stats.get)
    return res


get_visit_russia(geo_logs)
get_unic_id(ids)
name_channal_max(stats)
