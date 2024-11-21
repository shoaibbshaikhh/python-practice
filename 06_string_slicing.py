a='hello world'

b=a[::2]
c=a[::-1]
d=a[::-2]
e=a[3:]
f=a[:3]

print("String with alternate letters:",b)
print("String in reverse:",c)
print("String in reverse with alternate letters:",d)
print("String starting from 4th letter:",e)
print("String upto 4th letter:",e)


# Output:
# String with alternate letters: hlowrd
# String in reverse: dlrow olleh
# String in reverse with alternate letters: drwolh
# String starting from 4th letter: lo world
# String upto 4th letter: lo world


