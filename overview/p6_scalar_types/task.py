# hints:
# 1. https://docs.python.org/3/library/stdtypes.html#typesnumeric
# 2. https://docs.python.org/3/library/functions.html#int
# 3. https://docs.python.org/3/library/functions.html#bool

# print 10 literal in decimal base
# your implementation here

# print 10 literal in binary base
# your implementation here

# print 10 literal in hexadecimal base
# your implementation here

# convert to int and print
f = 1.5
# your implementation here

# convert to int and print
s = "121"
# your implementation here

# fill in objects_as_bool with the truth value of objects in 'objects'
objects = [0, 12, 0.0, -1.5, [], [1, 2], "", "False", None]
objects_as_bool = [# your implementation here]
for obj, obj_as_bool in zip(objects, objects_as_bool):
    print(f"bool({obj}) is {bool(obj)} --> "
          f"{'good!' if obj_as_bool is bool(obj) else 'try again!'}")

# now modify Connection class so that open connections truth value is True otherwise False
class Connection:

    def __init__(self):
        self.is_open = False

    def open_conn(self):
        self.is_open = True

    # your implementation here


conn = Connection()
if not conn:
    print("conn is closed, opening...")
    conn.open_conn()

if conn:
    print("conn is now open")