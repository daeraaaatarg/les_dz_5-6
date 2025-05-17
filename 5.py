# task 1

class Task:
    def __init__(self, name, deadline, status):
        self.name = name
        self.deadline = deadline
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_emp(self, *args):
        for task in args:
            self.tasks.append(task)

    def print_emp_names(self):
        if self.tasks != []:
            print("Task one")
            print(f"All the tasks")
            print("==========================================")
            for task in self.tasks:
                print(f"Task's name: {task.name}")
                print(f"Task's deadline: {task.deadline}")
                print(f"Task's status: {task.status}")
                print("==========================================")
        else:
            print(f"There's no tasks")

one = Task("Advertisment design", "07/07/3056", "done")
two = Task("App design", "34/87/9000", "undone")
three = Task("Logo design", "82/09/0001", "done")
manager = TaskManager()
manager.add_emp(one, two, three)
manager.print_emp_names()



#task 2

class Product:
    def __init__(self, name, price, availability):
        self.n = name
        self.p = price
        self.a = availability

class Cart:
    def __init__(self):
        self.products = []

    def add_emp(self, *args):
        for product in args:
            self.products.append(product)

    def print_emp_names(self):
        if self.products != []:
            print(" ")
            print("Task two")
            print(f"All the products")
            print("==========================================")
            for product in self.products:
                print(f"Product's name: {product.n}")
                print(f"Product's deadline: {product.p} gryvnas")
                print(f"Product's status: {product.a}")
                print("==========================================")
        else:
            print(f"There's no products")

one = Product("Bread", 40, "available")
two = Product("Milk", 34, "not available")
three = Product("Eggs (10)", 54, "available")
gen = one.p + two.p + three.p
cart = Cart()
cart.add_emp(one, two, three)
cart.print_emp_names()
print(f"General price: {gen} gryvnas")



#task 3

class BankAccount:
    def __init__(self, name, surname, number, balance):
        self.name = name
        self.sur = surname
        self.n = number
        self.b = balance

class Bank:
    def __init__(self):
        self.accs = []

    def add_emp(self, *args):
        for acc in args:
            self.accs.append(acc)

    def print_emp_names(self):
        if self.accs != []:
            print(" ")
            print("Task three")
            print(f"All the accounts")
            print("==========================================")
            for acc in self.accs:
                print(f"User's name: {acc.name}")
                print(f"User's surname: {acc.sur}")
                print(f"User's number: {acc.n}")
                print(f"User's balance: ${acc.b}")
                print("==========================================")
        else:
            print(f"There's no users")

one = BankAccount("Aaron", "Warner", 3528164923, 1000000)
two = BankAccount("Adam", "Kent", 3729562085, 500000)
three = BankAccount("James", "Anderson", 8735208745, 100000)
bank = Bank()
bank.add_emp(one, two, three)
bank.print_emp_names()