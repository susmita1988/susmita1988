mystr=("harry is a good boy")
#print(mystr[2:20:-2])
print(mystr[11])

# string slicing
   # To print Harry

print(mystr[0:5])

# print length

print(len(mystr))

print(mystr[0:78])  # bt print(mystr[78]) will give errors
print(mystr[0:])
print(mystr[:5])
print(mystr[:])

print(mystr[::]) # same as print(mystr[0:19:1])

print(mystr[::-1])
print(mystr[::-2])

#functions
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("girl"))
print(mystr.count("b"))
print(mystr.capitalize())
print(mystr.find("boy"))
print(mystr.upper())
print(mystr.lower())
#print(mystr.replace("is","are"))



