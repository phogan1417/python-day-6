line_number = 3

with open("logs.txt", "r") as file:
    for each_line in file:
          if "password" in each_line:
            print(each_line)
            print("The line number is: ", line_number)
