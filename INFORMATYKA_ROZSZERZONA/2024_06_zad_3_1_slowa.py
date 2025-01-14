import re

def find_reg_exp_in_file_lines(file_name, reg_exp):
  counter = 0
  with open(file_name, "r") as file:
    for line in file:
      if re.search(reg_exp, line):
        counter += 1
        print(line.strip())
  return counter

def find_substring_in_file_lines(file_name, first_letter, last_letter):
  counter = 0
  with open(file_name, "r") as file:
    for line in file:
      for i in range(len(line) - 2):
        if line[i] == first_letter and line[i+2] == last_letter and line[i+1].isalpha():
          counter += 1
          print(line.strip())
          break
  return counter


# print(find_reg_exp_in_file_lines(".\\dane\\slowa.txt", r"k[a-zA-Z]t"))

print(find_substring_in_file_lines(".\\dane\\slowa.txt", "k", "t"))