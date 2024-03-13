from decorators2 import logger

@logger()
def flat_generator(list_of_lists):
    for my_list in list_of_lists:
        yield from my_list

list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]
for i in flat_generator(list_of_lists_1):
    print(i)