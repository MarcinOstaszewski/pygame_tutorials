def count_all_characters_in_file(file_path):
  total_characters = 0
  with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding
    for line in file:
      total_characters += len(line)
  return total_characters
  
def count_characters_per_line(file_path):
  line_characters = {}
  with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding
    for line_number, line in enumerate(file, start=1):
      line_characters[line_number] = len(line)
  return line_characters

def count_character_frequency(file_path):
  frequency = {}
  with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding
    for line in file:
      line_length = len(line)
      if line_length in frequency:
        frequency[line_length] += 1
      else:
        frequency[line_length] = 1
  return frequency

def count_average_longest_line_length_with_frequency(file_path):
  frequency = count_character_frequency(file_path)
  sorted_lengths = sorted(frequency.items(), key=lambda item: item[0], reverse=True)
  
  total_lines = sum(frequency.values())
  top_10_percent_count = max(1, total_lines // 10)
  
  count = 0
  total_length = 0
  for length, freq in sorted_lengths:
    if count + freq <= top_10_percent_count:
      total_length += length * freq
      count += freq
    else:
      remaining = top_10_percent_count - count
      total_length += length * remaining
      break
  
  average_length = total_length / top_10_percent_count
  return average_length

def sort_frequency_keys_by_value_desc(frequency):
  sorted_keys = sorted(frequency, key=frequency.get, reverse=True)
  return sorted_keys

def sort_frequency_items_by_value_desc(frequency):
  sorted_items = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
  return sorted_items

def count_average_longest_line_length(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines.sort(key=len, reverse=True)
    top_10_percent = lines[:max(1, len(lines) // 10)]
    average_length = sum(len(line) for line in top_10_percent) / len(top_10_percent)
  return average_length

def get_shortest_and_longest_of_top_10_percent(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines[3][len(lines[3])-1], lines[3])
    char_code = ord(lines[3][-1])
    print(f"Character code of the last character in the 3rd line: {char_code}")
    sorted_lines = sorted(lines, key=len, reverse=True)
    top_10_percent = sorted_lines[:max(1, len(sorted_lines) // 10)]
    shortest_length = len(min(top_10_percent, key=len))
    longest_length = len(max(top_10_percent, key=len))
    print(shortest_length, longest_length)
  return shortest_length, longest_length

def remove_new_line_char_when_line_longer_than(file_path, new_file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    average_length = sum(len(line) for line in lines) // len(lines)
    longest_length = max(len(line) for line in lines)
    print(f"Average length: {average_length}", f"Longest length: {longest_length}")
    with open(new_file_path, 'w', encoding='utf-8') as file:
      for line in lines:
        if len(line) > average_length and line[-2] not in {'.', '!', '?'}:
          line = line.replace('\n', '')
        file.write(line)
  
if __name__ == "__main__":
  file_path = '.\\data\\sample.txt'
  
  remove_new_line_char_when_line_longer_than(file_path, '.\\data\\sample_new.txt')
  # total_characters = count_all_characters_in_file(file_path)
  # print(f"Total number of characters in {file_path}: {total_characters}")
  
  # frequency = count_character_frequency(file_path)
  # print(f"Frequency of line lengths in {file_path}: {frequency}")

  # sorted_keys = sort_frequency_keys_by_value_desc(frequency)
  # print("===============================================")
  # print(f"Sorted line lengths by frequency in {file_path}: {sorted_keys}")
  
  # sorted_values = sort_frequency_items_by_value_desc(frequency)
  # print("===============================================")
  # print(f"Sorted line lengths by frequency in {file_path}: {sorted_values}")
  
  # avarage_longest_line_length = count_average_longest_line_length(file_path)
  # print("===============================================")
  # print(f"Average length of the longest 10% of lines in {file_path}: {avarage_longest_line_length}")
  
  # avarage_longest_line = count_average_longest_line_length_with_frequency(file_path)
  # print(f"Average length of the longest 10% of lines in {file_path}: {avarage_longest_line}")
  
  # get_shortest_and_longest_of_top_10_percent(file_path)