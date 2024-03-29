import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

###Optimised approach
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   for letter in start_text:
#     position = alphabet.index(letter)
#     if cipher_direction == "decode":
#       shift_amount *= -1
#     new_position = position + shift_amount
#     new_letter = alphabet[new_position]
#     end_text += new_letter
#   print(f"The {cipher_direction}d text is {end_text}")
#caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

  def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    plain_text += new_letter
  print(f"The decoded text is {plain_text}")
 
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decode(cipher_text=text, shift_amount=shift)
else:
  print("Wrong choice! Exiting Cipher!")
