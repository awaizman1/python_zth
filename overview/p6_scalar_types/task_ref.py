# print 10 literal in decimal base
print(10)

# print 10 literal in binary base
print(0b10)

# print 10 literal in hexadecimal base
print(0x10)

# convert to int
f = 1.5
print(int(f))

# convert to int
s = "121"
print(int(s))

# fill in objects_as_bool
objects = [0, 12, 0.0, -1.5, [], [1, 2], "", "False", None]
objects_as_bool = [False, True, False, True, False, True, False, True, False]
for obj, obj_as_bool in zip(objects, objects_as_bool):
    print(f"bool({obj}) is {bool(obj)} --> "
          f"{'good!' if obj_as_bool is bool(obj) else 'try again!'}")
