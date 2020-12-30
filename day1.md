### Data Types
#### 1. Numbers
````python
decimal = 10 # value = 10
hexadecimal = 0x10 # value = 16
binary = 0b1011010 # value = 90
floatingpoint = 5.10
complexnumbers = 2 + 3j
````
Python integers does not have a maximum and minimum range unlike other languages like C++,Java.

#### 2. Strings
Strings can be enclosed in single quotes or double quotes.
In python strings are unicode.
````python
unicodeString = 'caf£'
byteString = b'sangharsh'
````
Strings starting with b' are byte strings.
Bytes can be decoded to get strings and strings can be encoded to get their bytes value.
````python
unicodeString = 'caf£'
byteString = b'caf\xc2\xa3'

print(unicodeString.encode('utf-8'))
Output::  b'caf\xc2\xa3'
print(byteString.decode('utf-8'))
Output:: 'caf£'
````
The default encoding in python3 is `UTF-8`.

Strings also supports operaitons like slicing and indexing.

#### 3. Boolean
Python3 provides two boolean objects from bool class `True` and `False`

***

### Basic I/O
Use `print()` function to print a value.This automatically adds a newline.
If you dont want the new line then use `sys.stdout.write()`.

Input to standard input can be given by using `input()` function.Remember to cast the input value to appropriate data type as `input()` always returns a string type i.e if you want to take an integer as input,
````python
num = int(input("Enter a number))
````

***
### Loops
`for` is used to iterate over data structures like lists, tuples etc.
````python
list = ['1',343,'afh']

for item in list:
    print(type(item))

Output:: <class 'str'>
         <class 'int'>
         <class 'str'>
````
`range()` can take different arguments.

`range(10)` will return a object that produces numbers from 0 to 9.

`range(0,10,2)` will generate numbers from 0 to 10 with a step of 2.
It can also be used to access lists and tuple elements.
````python

for i in range(len(list)):
    print(list[i])

Output:: 1 343 afh
````
`continue` can be used to skip rest of the iteration in a loop and `break` can be used to break out of the loop at current instant.

Other loops like while and do while are trivial as other languages.

***

### Control Flow

`If`, `elif` and `else` 
````python
val = 10

if val > 0:
    print('+ve')
elif val < 0:
    print('-ve')
else:
    print('0')
````
