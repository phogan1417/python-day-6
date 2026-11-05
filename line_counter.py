line_counter = 0
empty_line_counter = 0
section_label_counter = 0


with open("lyrics.txt", "r") as file:
    for every_line in file:
         if every_line == "\n":
              empty_line_counter = empty_line_counter + 1
        else:
          line_counter = line_counter + 1


print("The number of lines is: ", line_counter)