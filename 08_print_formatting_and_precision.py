s='shoaib'
r='shaikh'
a=1000.4233746327847836723
#With format function


#r will be printed after s because of indexing
print('follow {1} {0}'.format(r,s))


#With f specifier (Python >=3.6)
print(f"follow {s} {r}")


#Precision and Width of floating point numbers
print(f"{a:1.3f}")
