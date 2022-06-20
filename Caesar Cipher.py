import re
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(msg,shift_value,choice):
  convert = []
  for i in range(len(msg)):
    index = alphabet.index(msg[i])
    if choice == "encode":
      index += shift_value
    elif choice == "decode":
      index -= shift_value
    convert.append(alphabet[index])
  str=" "
  s1=str.join(convert)
  converted_text = re.sub(r'\s','',s1)
  if choice == "encode":
    print(f"The encoded text is {converted_text}")
  elif choice == "decode":
    print(f"The decoded text is {converted_text}")
  else:
    print("Invalid choice! You can either encode or decode.")

      #Another Way
# def caesar(msg,shift_value,choice):
#   end_text = ""
#   for letter in msg:
#     index = alphabet.index(letter)
#     if choice == "decode":
#       shift_value *= -1
#     index += shift_value
#     end_text += alphabet[index]
#   print(f"The {choice}d text is {end_text}")

caesar(text,shift,direction)
