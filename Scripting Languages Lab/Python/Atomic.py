dictionary={"He":"Helium","Li":"Lithium","H":"Hydrogen","O":"Oxygen","C":"Carbon","Na":"Sodium","Fe":"Iron","Si":"Silicon","Ca":"Calcium","Ne":"Neon"}
print(dictionary)

num = len(dictionary)
print("\nThe number of elements present in the dictionary is:",num)

while("true"):
	print("Enter an element you want to add to the dictionary:")
	value=input()
	print("Enter the symbol of the element:") 
	key=input()
	dictionary[key]=value
	print(dictionary)
	break

print("Enter the key value of the element you want to search for:")
search=input()
if search in dictionary.keys():
	print("Present")
else:
	print("Not Present")

