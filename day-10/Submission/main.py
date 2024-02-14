import json

name = input("Please, enter your name: ")
age = int(input("Please, enter your age: "))
food = input("Please, enter your favorite food: ")

info = [{"Name": name, "Age": age, "Favorite Food": food}]

with open('day-10\output.json','w') as outfile:
    json.dump(info, outfile, indent = 2)
