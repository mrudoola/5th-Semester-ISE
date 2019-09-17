def celToF():
	cel = float(input("Enter the temperature in celsius:"))
	f = (cel * 1.8) + 32
	print("%0.1f degree celsius is equal to %0.1f degree fahrenheit"%(cel,f))

def celToKelvin():
	cel = float(input("Enter the temperature in celsius:"))
	kelvin = (cel + 273)
	print("%0.1f degree celsius is equal to %0.1f degree kelvin"%(cel,kelvin))

while("true"):
	print("\nEnter 1 for celsius to fahrenheit conversion\nEnter 2 for celsius to kelvin conversion\nEnter -1 to exit\n");
	val = input("Enter the choice:")
	if val == "1": 
		celToF()
	elif val == "2":
		celToKelvin()
	elif val =="-1":
		break
	else:
		print("Enter a valid choice")
