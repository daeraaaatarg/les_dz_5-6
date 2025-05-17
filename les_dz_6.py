# task 1 (for dz!!!!!!!!!!!)
print("====================== Task 1 ==========================")
people = {"Aaron" : 19, "Adam" : 17, "James" : 12}
name = input("Input name: ")
try:
    age = people[name]
    print(f"{name} is {age} years old")
except KeyError:
    print("There's no one with such name")


# task 2
print("====================== Task 2 ==========================")

user = input("Input a number: ")
try:
    float_user = float(user)
    number = round(float_user)
    print(f"Whole number: {number}")
except ValueError:
    print("A number, dumbie, not anything else")

# task 3 -- знаю що чуть не так - я забула про файли, тому зробила більш по своєму
print("====================== Task 3 ==========================")

files = {"Name1" : "2132", "Name2" : "Hello world", "Name3" : "la la la"}
file = input("Name of the file: ")
try:
    info = files[file]
    print(f"File's info is {info}")
except KeyError:
    print("File does not exist")

# task 4
print("====================== Task 4 ==========================")

try:
    moduleE = input("Input module: ")
    try:
        functionN = input("Input function: ")

        module = __import__(moduleE)
        func = getattr(module, functionN)

        result = func()
        print(f"Result of the : {result}")
    except AttributeError:
        print("No function")
    except TypeError:
        print("No arguments")
except ModuleNotFoundError:
    print("No module")