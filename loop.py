# -*- coding: utf-8 -*-
"""loop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QvvJQG1aDrSPmLhqxvy8RvZ4gHnKs6RL
"""

i=1
while i<=10:
  print(i)
  i=i+1

"""fibonacchi"""

fib1=0
fib2=1
print(fib1)
print(fib2)
i=1
while i<=10:
  fib=fib1+fib2
  print(fib)
  fib1=fib2
  fib2=fib
  i=i+1

fib1,fib2=0,1

fib1,fib2=0,1
i=1
while i<=10:
  fib=fib1+fib2
  print(fib)
  fib1=fib2
  fib2=fib
  i=i+1

fib2

fib1,fib2=0,1
while fib2<20:
  fib=fib1+fib2
  print(fib)
  fib1,fib2=fib2,fib

fib1,fib2=0,1
while fib2<20:
  print(fib2)
  fib=fib1+fib2
  fib1,fib2=fib2,fib

fib1,fib2=0,1
while fib2<20:
  print(fib2)
  #fib=fib1+fib2
  fib1,fib2=fib2,fib1+fib2

fib1,fib2=0,1
while fib2<20:
  print(fib2)
  fib1,fib2=fib2,fib1+fib2

vowels=['a','e','i','o','u']

for ch in vowels:
  print(ch)

for i in range(0,10,1):
  print(i)

for i in range(0,10,1):
  print(i)
  if i>5:
    break

for i in range(10):
  
  if i<5:
    continue
  print(i)

