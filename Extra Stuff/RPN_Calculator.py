# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:06:03 2019

Name: Shameen Shetty
ID : 1001429743
Date: 10/24/19
OS Version: 64-bit
"""

def RPN_Calculator(expression):
  tokens = expression.split() #This will split each individual sentence into
                              #tokens, by whitespace i.e "a_b" becomes [a,b]
                              #where _ is the whitespace separating them
  stack = [] #Will store the tokens
  
  operation = {  # Symbol table sort of, will find certain expressions and 
              # take operations based on which expression it is, e.g
              # '+' means a + b, for input a,b 
              # which is stated as - "+": (lambda a, b: a + b)
  "+": (lambda a, b: a + b), # addition operator
  "-": (lambda a, b: a - b), # subtraction operator
  "*": (lambda a, b: a * b), # multiply operator
  "/": (lambda a, b: a / b), # divide operator
  "%": (lambda a, b: a % b), # (extra credit) modulo operator
  "^": (lambda a, b: a ** b) # (extra credit) power operator
  }

  for token in tokens:  # define a var called token, which will get all the 
                  # tokens
    if token not in operation:
        stack.append(int(token)) #if it is not in the defined symbol-table then
        # it will be stored in stack e.g 2 & 3is not defined, hence it 
        # is stored in stack to become [2,3]
    else:
        arg2 = stack.pop()
        arg1 = stack.pop()
        result = operation[token](arg1, arg2)
        stack.append(result)

# The above lines will pop the results of the vars that are stored in stack
# to get two input var (arg1 and arg2), then they will become the input values
# of operation[token] meaning which operatation is being done, e.g if it is 
# '+' then it becomes arg1 + arg2.
# Then finally, you append the result of the operation into stack

  return stack.pop()

f = open("input_RPN.txt", "r")  #open file 'input_RPN.txt' and read from it (r)
contents = f.read()  #read from entire file and store it in one var.
lines = contents.split("\n")  #split entire file by newline to get 
# individual sentences e.g if (2 3 +) and (2 5 -) were on separate lines they
# are now individual tokens eg ["2 3 +", "2 5 -"]
for token in lines:
    print("RPN statement is : ", token) # Prints the statement
    print("result = ", str(RPN_Calculator(token)) + "\n") # Prints the result

# For the above lines (from for to last print) This means for each line,
# you are finding its value
f.close()  # we close the file