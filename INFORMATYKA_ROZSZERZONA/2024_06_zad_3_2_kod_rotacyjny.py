def code_with_letter_rotation(word, n, count, longest_special_word):
  text_after_rotation = ''
  ord_of_a = ord('a')
  ord_of_z = ord('z')
  for letter in word:
    new_letter_code = ord(letter) + n
    if new_letter_code > ord_of_z:
      new_letter_code -= ord_of_z
    # print(f"{letter}: {ord(letter)} ==> {new_letter_code}")
    text_after_rotation += chr(new_letter_code)
  if text_after_rotation == word[::-1]:
    count += 1
    # print(text, text_after_rotation, text[::-1])
    if len(word) > len(longest_special_word):
      longest_special_word = word
    print(f"{count}, word:{word}, rotated: {text_after_rotation}, longest: {longest_special_word}")
  return count, longest_special_word
    

with open(".\\dane\\slowa.txt", "r", encoding="utf") as file:
  count = 0
  longest_special_word = ''
  for line in file:
    # print(word.strip())
    word = line.strip()
    count, longest_special_word = code_with_letter_rotation(word=word, n=13, count=count, longest_special_word=longest_special_word)
  print(count, longest_special_word)
