#1. Дан список повторяющихся элементов.
#Вернуть список с дублирующимися элементами.
#В результирующем списке не должно быть дубликатов.


def only_double(my_list: list) -> list:
    return list(set(filter(lambda x: my_list.count(x) > 1, my_list)))



#2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
#Не учитывать знаки препинания и регистр символов.
#За основу возьмите любую статью из википедии или из документации к языку.


def ten_words(text: str) -> list[str]:
    delete = ".,!?;:-[]{}()="
    for i in delete:
        text = text.replace(i, "")
    text = text.lower()
    return sorted(set(text.split()), key=lambda x: text.count(x))[-10:]

#3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
#Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


def backpack(shop: dict[str:int], size: int) -> list[list[str]]:
    pcs, weight = zip(*sorted(shop.items(), key=lambda x: x[1], reverse=True))
    result, temp, temp_w = [], [], 0
    for index, w in enumerate(weight, 0):
        temp_w += w
        temp.append((pcs[index]))
        for index_n, wn in enumerate(weight[index:], index):
            if wn + temp_w <= size:
                temp_w += wn
                temp.append(pcs[index_n])
        result.append(temp)
        temp, temp_w = [], 0
    return result