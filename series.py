import pandas as p

s = [10, 23, 45, 56, 89]
v = p.Series(s)
print(v)

v = p.Series(s, index=["a", "b", "c", "d", "e"])
print(v)

# if u want to aceess the date from index

v = p.Series(s, index=["a", "b", "c", "d", "e"])
print(v["c"])
# in dictionary format
calories = {'day1': 200, 'day2': 320, 'day3': 400}
v = p.Series(calories)
print(v)

# if u have filter a perticular data from dictionary
v = p.Series(calories, index=["day3", "day2"])
print(v)

fruit_set = {'fruit': ["mangos", "banana", "watermalon", "kivi"], 'count': [10, 34, 78, 44]}
v = p.Series(fruit_set)
print(v)
