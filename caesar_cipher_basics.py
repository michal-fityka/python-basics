alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text,shift_number):
  lista = []
  for a in plain_text:
    if a in alphabet:
      if (alphabet.index(a) + shift_number) < len(alphabet):
        lista.append(alphabet[alphabet.index(a) + shift_number])
      else:
        lista.append(alphabet[alphabet.index(a) + shift_number - len(alphabet) ])
    else:
      lista.append(a)
  my_string = "".join(str(element) for element in lista)

  print(f"The encoded text is {my_string}")
  

#encrypt("zulu",5)

def decrypt(encrypted_text,shift_num):
  lista = []
  for a in encryp_text:
    if a in alphabet:
      if (alphabet.index(a) - shift_number) > 0:
        lista.append(alphabet[alphabet.index(a) - shift_number])
      else:
        lista.append(alphabet[alphabet.index(a) - shift_number + len(alphabet) ])
    else:
      lista.append(a)
  my_string = "".join(str(element) for element in lista)

  print(f"The decoded text is {my_string}")



#decrypt("alicja",5)

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == 'encode':
  encrypt(text,shift)
elif direction == 'decode':
  decrypt(text,shift)
