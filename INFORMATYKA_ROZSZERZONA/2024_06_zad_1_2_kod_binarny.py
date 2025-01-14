def convert_decimal_n_to_binary(n, binary=""):
  if n == 0:
    return binary
  else:
    return convert_decimal_n_to_binary(n // 2, str(n % 2) + binary) 

def find_last_binary_digit_in_table(w, k, n):
  table_cells = w * k
  n_in_binary = convert_decimal_n_to_binary(n)
  last_rest = table_cells % len(n_in_binary)
  print(f"n: {n}, cells: {table_cells}, n_in_binary: {n_in_binary}, length: {len(n_in_binary)}, last_rest: {last_rest} ==> last digit: {n_in_binary[last_rest]}")

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

# Example usage
# print(decimal_to_binary(24))  # Output: 11000
  
# find_last_binary_digit_in_table(3, 3, 7)

# for x in range(3,20):
#   find_last_binary_digit_in_table(3, 5, x)

print(convert_decimal_n_to_binary(179))

