def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params()
print_params(a=2, c=False)
print_params(a=1)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [1, "Swiat", True]
values_dict = {'a': 100, 'b': "Urban", 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, True]
print_params(*values_list_2, 42)