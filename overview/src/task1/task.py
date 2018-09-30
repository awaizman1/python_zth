# --- python is strongly typed
# lets verify that every object has a definite type
for obj in [1, True, 2.5, "hello", [1, 2, 3], {1: "one", 2: "two"}]:
    print(type(obj))


# --- python is dynamically typed - adding new code
# can you change the code so that 'new_code' will be added and executed?
new_code = "print('where the hell this line came from?')"
eval(new_code)


# --- python is dynamically typed - extend objects
# now make student instance having also 'gender' attribute with value 'male'
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("jhon", 27)
student.gender = 'male'

print("student %s is %s" % (student.name, student.gender))
