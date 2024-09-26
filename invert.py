
def reverse_bits_in_bytes(string):
  """Reverses the bits within each byte of a given string.
  Args:
    string: The input string.
  Returns:
    The string with reversed bits within each byte.
  """
  reversed_string = ""
  for i in range(0, len(string), 8):
    byte = string[i:i+8]
    reversed_byte = ""
    for bit in reversed(byte):
      reversed_byte += bit
    reversed_string += reversed_byte
  return reversed_string
# Example usage:
string = "01111100100000101111001001100010110010100111001011110010111010010101100100101010001011100010101010100011001000111100"
reversed_string = reverse_bits_in_bytes(string)
print(reversed_string)
