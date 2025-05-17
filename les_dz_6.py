# task 1 (for dz!!!!!!!!!!!)
print("====================== Task 1 ==========================")
people = {"Aaron" : 19, "Adam" : 17, "James" : 12}
name = input("Input name: ")
try:
    age = people[name]
    print(f"{name} is {age} years old")
except KeyError:
    print("There's no one with such name")

