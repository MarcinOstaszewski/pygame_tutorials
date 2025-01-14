def  count_all_letters(word):
  letters_dict = {}
  letters = list(word.strip())
  for letter in letters:
    if letter in letters_dict:
      letters_dict[letter] += 1
    else:
      letters_dict[letter] = 1
  print(letters, letters_dict)
  most_common_letter = {}
  for l in letters_dict:
    if letters_dict[l] > most_common_letter_number:
      most_common_letter = l

with open(".\\dane\\slowa.txt", "r", encoding="utf") as file:
  x = 0
  for word in file:
    x += 1
    
count_all_letters('lokomotywowo')