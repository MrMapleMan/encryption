import random
import string

def ShiftChar(c, shift, ignore_non_ascii=False):
  if c not in string.ascii_letters:
      if ignore_non_ascii:
          return ''
      else:
          return c
  if c == c.upper():
      delta = ord('A')
  else:
      delta = ord('a')
  c_ord = ord(c)
  c_ord -= delta
  c_ord += shift
  c_ord %= 26
  c_ord += delta
  return chr(c_ord)

def Ceasar(s, shift, ignore_non_ascii=False):
    return ''.join([ShiftChar(i, shift, ignore_non_ascii) for i in s])

if __name__ == '__main__':
    shift = 2
    encrypted = Ceasar('a', shift, ignore_non_ascii=False)
    print(encrypted)
    decrypted = Ceasar(encrypted, -shift, ignore_non_ascii=False)
    print(decrypted)
