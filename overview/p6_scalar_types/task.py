# hints:
# 1. https://docs.python.org/3/library/stdtypes.html#typesnumeric
# 2. https://docs.python.org/3/library/functions.html#int
# 3. https://docs.python.org/3/library/functions.html#bool

# print 10 literal in decimal base
# your implemetation here

# print 10 literal in binary base
# your implemetation here

# print 10 literal in hexadecimal base
# your implemetation here

# convert to int and print
f = 1.5
# your implemetation here

# convert to int and print
s = "121"
# your implemetation here

# fill in objects_as_bool
objects = [0, 12, 0.0, -1.5, [], [1, 2], "", "False", None]
objects_as_bool = [# your implemetation here]
for obj, obj_as_bool in zip(objects, objects_as_bool):
    print(f"bool({obj}) is {bool(obj)} --> "
          f"{'good!' if obj_as_bool is bool(obj) else 'try again!'}")
