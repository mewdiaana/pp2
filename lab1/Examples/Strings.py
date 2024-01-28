#1
print("Hello")
print('Hello')

#2
a = "Hello"
print(a)

#3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#5
a = "Hello, World!"
print(a[1])

#6
for x in "banana":
  print(x)

#7
a = "Hello, World!"
print(len(a))

#8
txt = "The best things in life are free!"
print("free" in txt)

#9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#10
txt = "The best things in life are free!"
print("expensive" not in txt)

#11
txt = "The best things in life are free!"
print("expensive" not in txt)

#12
b = "Hello, World!"
print(b[2:5])

#13
b = "Hello, World!"
print(b[:5])

#14
b = "Hello, World!"
print(b[2:])

#15
b = "Hello, World!"
print(b[-5:-2])

#16
a = "Hello, World!"
print(a.upper())

#17
a = "Hello, World!"
print(a.lower())

#18
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#19
a = "Hello, World!"
print(a.replace("H", "J"))

#20
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#21
a = "Hello"
b = "World"
c = a + b
print(c)

#21
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#22
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#23
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#24
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#25
txt = "We are the so-called \"Vikings\" from the north."

#26
txt = 'It\'s alright.'
print(txt) 

#27
txt = "This will insert one \\ (backslash)."
print(txt) 

#28
txt = "Hello\nWorld!"
print(txt) 

#29
txt = "Hello\rWorld!"
print(txt) 

#30
txt = "Hello\tWorld!"
print(txt) 

#31
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#32
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#33
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

#34
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
#out: Hello, and welcome to my world.

#35
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
#out: 
hello, and welcome to my world!

#36
