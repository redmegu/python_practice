def is_palindrome(input_string):
    lower_input_string = input_string.lower()
    new_string = lower_input_string.replace(" ","")
    reverse_string = new_string[::-1]
    
    if new_string == reverse_string:
        return True
    else: return False

print(is_palindrome(input("Input a word: ")))