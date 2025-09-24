nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)

nombres_2 = range(-10, 10)
nombres_positifs = [i for i in nombres_2 if i >= 0]
print(nombres_positifs)

nombres_3 = range(5)
nombres_doubles = [i * 2 for i in nombres_3]
print(nombres_doubles)

nombres_4 = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres_4]
print(nombres_inverses)