import sys
import time

def remove_new_line_char_when_line_longer_than(file_path, new_file_path):
  """removes new line character from lines longer than average length
  when the last character is not a sentence ending character
  and writes the new file to the new_file_path

  Args:
      file_path (.txt): input file path (e.g. converted from PDF with too many line breaks)
      new_file_path (.txt): output file path with smartly removed line breaks
  """
  with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    average_length = sum(len(line) for line in lines) // len(lines)
    with open(new_file_path, 'w', encoding='utf-8') as file:
      for line in lines:
        if len(line) > average_length and line[-2] not in {'.', '!', '?'}:
          line = line.replace('\n', '')
        file.write(line)
    print(f"SUCCESS: new file created: {new_file_path}")
  
if __name__ == "__main__":
  time_start = time.time()
  if len(sys.argv) != 3:
    print("Please provide the input file path and the output file")
    print("Usage: 'python smart_remove_NewLine_characters.py <input_file_path> <output_file_path>'")
  else:
    file_path = sys.argv[1]
    new_file_path = sys.argv[2]
    remove_new_line_char_when_line_longer_than(new_file_path=sys.argv[2], file_path=sys.argv[1])
    print(f"Time taken: {time.time() - time_start} seconds")