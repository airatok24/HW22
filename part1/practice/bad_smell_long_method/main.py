# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля

from operator import itemgetter

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""
AGE_LIMIT = 10


def _read(str_value):
    values_per_row = str_value.split("\n")
    data_in_list = []
    for element in values_per_row:
        name, age = element.split(";")
        data_in_list.append({"name": name, "age": int(age)})
    return data_in_list


def _sort(data):
    # Сортировка по возрасту по возрастанию
    data_sorted = sorted(data, key=itemgetter("age"))
    return data_sorted


def _filter(data):
    # берем людей не младше 10 лет (см AGE_LIMIT)
    data_filtered_by_age = []
    for person in data:
        if person["age"] >= AGE_LIMIT:
            data_filtered_by_age.append(person)
    return data_filtered_by_age


def get_users_list():
    data_dicts_in_list = _read(csv)
    data_sorted_by_age = _sort(data_dicts_in_list)
    data_result = _filter(data_sorted_by_age)
    return data_result


if __name__ == '__main__':
    print(get_users_list())
