#Function for Binary to Decimal
def binToDec(word):
      x = 0
      x = int(word)
      count = 0
      dec = 0
      while (True):
            if (x == 0):
                  break
            else:
                  temp = x % 10
                  x = int(x / 10)
                  dec += temp * pow(2, count)
                  count = count + 1
      return dec

#Function for Decimal to Binary
def decToBin(num):
      val = int(num)
      rem = 0
      bin = ''
      while(True):
            if (val == 0):
                  break
            rem = val % 2
            val = int(val / 2)
            bin = str(rem) + bin
      return bin

#Function for Hexadecimal to Decimal
def hexToDec(s):
      _hexer = "0123456789ABCDEF"
      #Find returns the lowest index of the substring _hexer, Enumerate allows loop over s and have automatic counter
      #reverse allows a reversed iterator for the string s
      return sum([_hexer.find(var) * 16 ** i for i, var in enumerate(reversed(s.upper()))])


#Function for Decimal to Hexadecimal
#created a dictionary and mapped every key to its value
hexMap = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
def toHex(n):
      outcome = ""
      if n ==0:
            return '0'
      while n != 0:
            outcome += str(hexMap[(n % 16)])#Converted the dictionary to string
            n = n // 16 #Integer division
      return outcome[: : -1]

a = '1010'
b = "ABCDEF"
c = (11259375)
print(binToDec(a))
print(decToBin(10))
print(hexToDec(b))
print(toHex(c))
