# TODO Sonderzeichen öäü etc.
"--- Ceasar Functions ---"
def ceasar_encrypt(text: str, key: int) -> str:
  """
  ceasar_encrypt does blah blah blah.

  :param text: describe about parameter p1
  :param key: describe about parameter p2
  :return: describe what it returns
  """   
  result = []
  for l in text:
    if l.isalpha(): 
      base = ord("A") if l.isupper() else ord("a") #Set the base letter, A is we start with an upper letter else a, we need a base because ASCII
      shift = (ord(l) - base + key) % 26 + base 
      result.append(chr(shift))
    else:
      result.append(l) #do not encrypt a character that is not alphabetical (e.g. .!?)
  return "".join(result)

def ceasar_decrypt(text: str, key: int) -> str:
  return ceasar_encrypt(text, -key) #literally just encrypt but reverse

"--- Vigenere Functions ---"
def vigenere_encrypt(text: str, key: str) -> str:
  return "".join(
    chr((ord(ch) - (ord("A") if ch.isupper() else ord("a")) + (ord(key[i % len(key)].upper()) - ord("A"))) %26 + (ord("A") if ch.isupper() else ord("a")))
    #(ch - base + shift) %26 + base
    if ch.isalpha() else ch
    for i, ch in enumerate(text)) 

def vigenere_decrypt(text:str, key:str) -> str:
    return "".join(
    chr((ord(ch) - (ord("A") if ch.isupper() else ord("a")) - (ord(key[i % len(key)].upper()) - ord("A"))) %26 + (ord("A") if ch.isupper() else ord("a")))
    #(ch - base - shift) %26 + base
    if ch.isalpha() else ch
    for i, ch in enumerate(text)) 

"--- OTP Functions ---"
def otp(text: str, key: str) -> str:
    if len(key) < len(text):
        raise ValueError("Key must be at least as long as text")
    return "".join(
        chr(ord(ch) ^ ord(key[i]))
        for i, ch in enumerate(text))

# These are more complex, need libraries and key gen
"--- AES Functions ---"

"--- RSA Functions ---"
