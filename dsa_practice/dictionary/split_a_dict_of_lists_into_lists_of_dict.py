"""
47.

Write a Python program to split a given dictionary of lists into lists of dictionaries.
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]


"""


d = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

# dd = [{k: value[i] for key, value in d.items()} for i in range(len(list(value)))]

dd = [{'Science': a, 'Language': b}
      for (a, b) in zip(d['Science'], d['Language'])]

print(dd)
