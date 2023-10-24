with open('qert.py', 'w') as json_file:
    json.dump(data, json_file)
data = [1, 2, 3, 4, 5]
print(data_str)
data = [1, 'hello', 2.5, True, 'world']
integers = list(filter(lambda x: isinstance(x, int), data))

print(integers)