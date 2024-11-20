import math
import random


def test_greeting():
    name = "Анна"
    age = 25

    output = f"Привет, {name}! Тебе {age} лет."
    output_2 = "Привет, " + name + "! Тебе " + str(age) + " лет."
    output_3 = "Привет, {name}! Тебе {age} лет.".format(name=name, age=age)
    output_4 = "Привет, %s! Тебе %s лет." % (name, age)

    assert output == "Привет, Анна! Тебе 25 лет."
    assert output_2 == "Привет, Анна! Тебе 25 лет."
    assert output_3 == "Привет, Анна! Тебе 25 лет."
    assert output_4 == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20

    perimeter = (a + b) * 2
    area = a * b

    assert perimeter == 60
    assert area == 200


def test_circle():
    r = 23

    area = math.pi * math.pow(r, 2)
    area_2 = math.pi * r ** 2

    length = 2 * math.pi * r

    assert area == 1661.9025137490005
    assert area_2 == 1661.9025137490005

    assert length == 144.51326206513048


def test_random_list():
    l = []
    l_2 = []

    for i in range(10):
        l.append(random.randint(1, 100))

    for i in range(10):
        l_2 += str(random.randint(1, 100)).split()

    l.sort()
    l_3 = sorted(l_2)

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))

    assert len(l_3) == 10
    assert all(l_3[i] <= l_3[i + 1] for i in range(len(l_3) - 1))


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    temp = list(set(l))
    l = temp

    l_2 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    for i in sorted(l_2):
        if l_2.count(i) > 1:
            l_2.pop(i)

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert isinstance(l_2, list)
    assert len(l_2) == 10
    assert l_2 == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    d = {}
    d_2 = {}

    zipped_lst = list(zip(first, second))

    for i in zipped_lst:
        d[i[0]] = i[1]

    for i in range(len(first)):
        try:
            d_2[first[i]] = second[i]
        except IndexError:
            d_2[first[i]] = i + 1

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second

    assert isinstance(d_2, dict)
    assert len(d_2) == 5
    assert list(d_2.keys()) == first
    assert list(d_2.values()) == second
