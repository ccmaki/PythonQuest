name = input("Please, enter your full: ")

file = open('user_info.txt','a')

file.write(name+"\n")

file.close()
