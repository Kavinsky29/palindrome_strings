# Creating a program that tells if a word is a palindrome or not

word = input('Enter the name:')
l = len(word)
st = ""

for i in range(l-1,-1,-1):
    st += word[i]

print("Result is", st)

if(st==word):
    print("Is a Palindrome")

else:
    print("Is not a Palindrome")