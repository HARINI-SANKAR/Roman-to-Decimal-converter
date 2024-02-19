def roman_to_decimal(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    
    for i in range(len(roman)):
        if i > 0 and roman_numerals[roman[i]] > roman_numerals[roman[i - 1]]:
            decimal += roman_numerals[roman[i]] - 2 * roman_numerals[roman[i - 1]]
        else:
            decimal += roman_numerals[roman[i]]
    
    return decimal

user_input = input("Enter a Roman numeral: ").upper()
result = roman_to_decimal(user_input)

print(f"The decimal equivalent of {user_input} is: {result}")