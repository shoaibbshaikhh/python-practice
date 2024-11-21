a='follow,shoaib|shaikh'


b=len(a)
c=a.upper()
d=a.lower()
e=a.swapcase()
f=a.isalpha()
g=a.isalnum()
h=a.isdigit()
i=a.replace("fol","kho")
j=a.index('ol')
k=a.rstrip()
l=a.split('|')

print("Length of a:",b)
print("Upper case of a:",c)
print("Lower case of a:",d)
print("Reverse case of a:",e)
print("Only alphabets of a:",f)
print("Only alphabets + numbers of a:",g)
print("Only digits of a:",h)
print("Replace fol with kho of a:",i)
print("Index of s in a:",j)
print("Strip in a:",k)
print("Split a:",l)


# Output:
# Length of a: 20
# Upper case of a: FOLLOW,SHOAIB|SHAIKH
# Lower case of a: follow,shoaib|shaikh
# Reverse case of a: FOLLOW,SHOAIB|SHAIKH
# Only alphabets of a: False
# Only alphabets + numbers of a: False
# Only digits of a: False
# Replace fol with kho of a: 1
# Index of s in a: kholow,shoaib|shaikh
# Strip in a: follow,shoaib|shaikh
# Split a: ['follow,shoaib', 'shaikh']
