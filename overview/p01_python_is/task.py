
# --- python is strongly typed
# lets verify that every object has a definite type
for obj in [1, True, 2.5, "hello", [1, 2, 3], {1: "one", 2: "two"}]:

    # hints:
    # 1. print is your buddy
    # 2. https://docs.python.org/3/library/functions.html#type

    raise NotImplementedError("YOUR IMPLEMENTATION HERE")



# --- python is dynamically typed - adding new code
# can you change the code so that 'new_code' will be added and executed?
new_code = "print('where the hell this line came from?')"
# hints:
# 1. https://docs.python.org/3/library/functions.html#eval
raise NotImplementedError("YOUR IMPLEMENTATION HERE")


# --- python is dynamically typed - extend objects
# now make student instance having also 'gender' attribute with value 'male'
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("jhon", 27)

# hints:
# 1. setting an object attribute is similar to accessing it
raise NotImplementedError("YOUR IMPLEMENTATION HERE")

print("student %s is %s" % (student.name, student.gender))
