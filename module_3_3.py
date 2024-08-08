# 1
def print_params(a=1, b='ball', c=True):
    print(a, b, c)

print_params()
print_params(12, 78, 34)
print_params(b=25)
print_params(c=[1,2,3])
# Функция будет работать с вводом не более 3-х параметров иначе ошибка

# 2
values_list = [1, 'cat', True]
values_dist = {'a': True, 'b': 1, 'c': 'dog'}

print_params(*values_list)
print_params(**values_dist)

# 3
values_list2 = [1, 'snake']
print_params(*values_list2, 42)