#1.Write a program to reverse a user-entered number.l
n=int(input('Enter number:'))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)

#2.Write a program that reverses a number and prints both the original and reversed number.

n=int(input('Enter number'))
orginal=n
reverse=0
while n>0:
	digit=n%10
	reverse=reverse*10+digit
	n=n//10
print('orginal number',orginal)
print('reversed number',reverse)

#3.Check whether the user-entered number is a palindrome or not.
n=int(input('Enter number'))
orginal=n
reverse=0
while n>0:
	digit=n%10
	reverse=reverse*10+digit
	n=n//10
if orginal==reverse:
	print('Palindrome')
else:
	print('Not a Palindrome')

#4.Test Question 2 (Difficult)
'''User kitte oru number vangunga.
Number reverse pannanum.
Original number print pannanum.
Reversed number print pannanum.
Adhu palindrome aa illa ya nu check pannanum.'''
n=int(input('Enter number'))
original=n
reverse=0
while n>0:
	digit=n%10
	reverse=reverse*10+digit
	n=n//10
print('original number',original)
print('reversed number',reverse)
if original==reverse:
	print('Palindrome')
else:
	print('Not a Palindrome')
  
#5.check whether the user entered number is prime number or not
n=int(input('Enter a number:'))
count=0
for i in range(2,n+1):
	if n%i==0:
		count+=1
if count==0:
	print('prime number')
else:
	print('Not a prime number')

#6.Write a program to count the factors of a number and print whether it is Prime or Not Prime.

n=int(input('Enter a number:'))
count=0
for i in range(2,n+1):
	if n%i==0:
		count+=1
if count==0:
	print('prime number')
else:
	print('Not a prime number')

#7.Write a program that:
'''Takes a number from the user.
Finds how many factors the number has.
Prints the factor count.
Prints whether it is Prime or Not Prime.'''

n=int(input('Enter a number:'))
count=0
for i in range(1,n+1):
	if n%i==0:
		count+=1
print('factor count',count)
if count==2:
	print('prime number')
else:
	print('Not a prime number')


  
