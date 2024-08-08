def calculate_structure_sum(data_structure):
    if isinstance(data_structure, (list, tuple, set)):
        return sum(calculate_structure_sum(item) for item in data_structure)

    elif isinstance(data_structure, dict):
        return sum(
            calculate_structure_sum(key) + calculate_structure_sum(value) for key, value in data_structure.items())

    elif isinstance(data_structure, int):
        return data_structure

    elif isinstance(data_structure, str):
        return len(data_structure)

    return 0


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)

data_structure1 = [
    {'x':10, 'y':[20, 30], 'z':{'a': 5, 'b': 15}}, "Python", (42, {'nested': "string", 'value':100}),
    [99, {"key":"value"}, "test"], set([7, 14, 21]), ]

result1 = calculate_structure_sum(data_structure1)
print(result1)
