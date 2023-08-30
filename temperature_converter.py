temperature= int(input("Enter Temperature in degress= "))

temp_type= input("Press C for Celsius and F for Fahrenheit= ").upper()


if temp_type== "C" or temp_type=="CELSIUS":
    celsius= (temperature * 9/5) +32
    print(f"Your Temperature in Celsius= {celsius}°")

elif temp_type== "F" or temp_type=="FAHRENHEIT":
    fahrenheit= (temperature - 32) * 9/5 
    print(f"Your Temperature in Fahrenheit= {fahrenheit}°")

