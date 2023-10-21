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


def my_unit_test(l,r,c):
    
    try:
        result = perform_arithmetic_operations(l)
        if result == r:
            print(f"La prueba se pasa  porque :{l} = {r}  con criterio {c}" )
        else:
            print(f"La prueba falla porque :{l} != {r}  con criterio {c}" )
    except Exception as e:
        print(f"cadena invalida: {e}")


data_list = [["11-5", 6, "pass"], ["11-5", 7, "fail"],["11-5-1-1", 4, "pass"],["a-b", 0, "fail"]]

input_string = "50-3-6-7"
result = perform_arithmetic_operations(input_string)
print(f"Result: {result*1.0}")



for i in range(len(data_list)):
    my_unit_test(data_list[i][0], data_list[i][1],data_list[i][2])
#print(data_list[0][2])
     
