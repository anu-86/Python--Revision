#1.Take a number from the user. Reverse the number and print it.
n=int(input())
reverse=0
while n>0:
	digit=n%10
	n=n//10
	reverse=reverse*10+digit
print(reverse)

#2.Take a number from the user. Print both the original number and the reversed number.
n=int(input())
reverse=0
original=n
while n>0:
	digit=n%10
	n=n//10
	reverse=reverse*10+digit
print('original number:',original)
print('reverse number:',reverse)

#3.Take a number from the user. Find the reversed number and check whether the reversed number is Even or Odd.

n=int(input())
reverse=0
while n>0:
	digit=n%10
	n=n//10
	reverse=reverse*10+digit
print('reverse no:',reverse)
if reverse%2==0:
	print('odd')
else:
	print('Even')

#4.Take a number from the user and find the sum of digits of the reversed number.
n=int(input())
sum_digits = 0
reverse=0
while n>0:
	digit=n%10
	sum_digits = sum_digits + digit
	n=n//10
	reverse=reverse*10+digit
print(reverse)
print(sum_digits)

#5.
'''Print:
Plain text
* * *
* * *
* * *
using nested loops.'''

for i in range(3):
	for j in range(3):
		print('*',end=" ")
	print()

#6.
'''Print:
Plain text
* * * *
* * * *
(2 rows, 4 columns)'''

for i in range(2):
	for j in range(4):
		print('*',end=" ")
	print()

#7.Print:
'''Plain text
1 1 1
1 1 1
1 1 1
using nested loops.'''
for i in range(3):
	for j in range(3):
		print('1',end=" ")
	print()

#8.
'''Print:
Plain text
*
* *
* * *
* * *'''
for i in range(1,5):
	for j in range(i):
		print('*',end=" ")
	print()

#9.
'''Print:
Plain text
*
* *
* * *
* * * *
* * * * *
* * * * * *'''
for i in range(1,7):
	for j in range(i):
		print('*',end=" ")
	print()

#10.Print numbers instead of stars:
'''Plain text
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1'''
for i in range(1,6):
	for j in range(i):
		print('1',end=" ")
	print()
