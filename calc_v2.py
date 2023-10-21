def perform_arithmetic_operations(s):
    tokens = s.split('-')  # Split the string by '-' to get a list of numbers and '+' signs
    result = int(tokens[0])  # Initialize the result with the first number

    for token in tokens[1:]:
        if '+' in token:
            sub_tokens = token.split('+')  # Split the token by '+' to get individual numbers
            for sub_token in sub_tokens:
                result += int(sub_token)  # Add each number to the result
        else:
            result -= int(token)  # Subtract the number if there is no '+'

    return result

input_string = "50-3-6-7"
result = perform_arithmetic_operations(input_string)
print(f"Result: {result*1.0}")

def my_unit_test(l,r):
    test_data = l
    try:
        result = perform_arithmetic_operations(l)
        if result == r:
            print(f"La prueba se pasa con exito porque :{l} = {r}" )
        else:
            print(f"La prueba falla porque :{l} != {r}" )
    except Exception as e:
        print(f"cadena invalida: {e}")

my_unit_test('5 - 3-4', -3)
     
