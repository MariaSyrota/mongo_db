import json
import requests

url = 'https://script.google.com/macros/s/AKfycbyZPugDtdFm2uWePVygStAx5naJBuM58wrwCbOJkYMU_ITB0GaYoE1vKz8u2RF1QVJc/exec'
response = requests.get(url)
data_dict = response.json()

with open('data.json', 'w') as file:
    json.dump(data_dict, file)

data = [1, 2, 3, 4, 5]

data_str = list(map(str, data))

print(data_str)

data = [1, 'apple', 3.14, 5, 'banana', 7.5, True]
integers = list(filter(lambda x: type(x) == int, data))
print(integers)
