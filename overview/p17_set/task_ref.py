
# given list of programming language experts (with duplicates) find the following:
# 1. print programmers names, sorted (in format ['X', 'Y', 'Z']).
# 2. print those who are expert in one language only, sorted (in format ['X', 'Y', 'Z'])
# 3. print those who are expert in 2 or more languages, sorted (in format ['X', 'Y', 'Z'])

cpp_expert = ['Jhon', 'Neli', 'Mike', 'Dave', 'Lena', 'Mark', 'Shira', 'Neli', 'Dave']
java_expert = ['Neli', 'Mike', 'Shira', 'Mike', 'Jessy']
python_expert = ['Jhon', 'Lena', 'Shira', 'Lena', 'Elthon']

cpp_set = set(cpp_expert)
java_set = set(java_expert)
python_set = set(python_expert)

print(sorted(set(cpp_expert + java_expert + python_expert)))
print(sorted((cpp_set | java_set | python_set) - (cpp_set & java_set) - (cpp_set & python_set) - (java_set & python_set)))
print(sorted((cpp_set & java_set) | (cpp_set & python_set) | (java_set & python_set)))
