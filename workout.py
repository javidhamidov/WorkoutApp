import json

class Workout():
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
    def get_ripped(self):
        with open("get_ripped.json") as file:
            data = json.load(file)
        print("Your info :\nName : {}\nHeight : {}cm\nWeight : {}kg\nAge : {}\n--------------------".format(self.name, self.height, self.weight, self.age))
        for day, plan in data[0].items():
            print("{} : {}".format(day, plan))
    def lose_weight(self):
        with open("lose_weight.json") as file:
            data = json.load(file)
        print("Your info :\nName : {}\nHeight : {}cm\nWeight : {}kg\nAge : {}\n--------------------".format(self.name, self.height, self.weight, self.age))
        for day, plan in data[0].items():
            print("{} : {}".format(day, plan))
    def prepare_for_competition(self):
        with open("prepare_for_competition.json") as file:
            data = json.load(file)
        print("Your info :\nName : {}\nHeight : {}cm\nWeight : {}kg\nAge : {}\n--------------------".format(self.name, self.height, self.weight, self.age))
        for day, plan in data[0].items():
            print("{} : {}".format(day, plan))

name = input("Enter your name : ")
height = input("Enter your height : ")
weight = input("Enter your weight : ")
age = input("Enter your age : ")
workout = Workout(name, height, weight, age)
option = input("Choose your goal :\n1)Get ripped\n2)Lose weight\n3)Prepare for competition\n>>> ")
if option == "1":
    workout.get_ripped()
elif option == "2":
    workout.lose_weight()
elif option == "3":
    workout.prepare_for_competition()
else:
    print("This option is not available")