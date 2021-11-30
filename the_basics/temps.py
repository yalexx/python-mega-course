my_list = [99, 'no data', 95, 94, 'no data']


def foo(data):
    return [temp if isinstance(temp, int) else 0 for temp in data]


print(foo(my_list))
