def convert_to_celsius(x):
    celsius = (x-32)*5/9
    return celsius

for x in range(0,51,5):
    print(x,convert_to_celsius(x))