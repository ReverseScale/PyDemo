import json

numbers = [2, 3, 4, 5]

filename = 'json_files/numbers.json'
with open(filename, 'a') as f_obj:
    json.dump(numbers, f_obj)