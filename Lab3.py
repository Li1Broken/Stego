def text_to_binary(text):
    binary_string = ""
    for char in text:
        binary_char = bin(ord(char))[2:]
        binary_char = binary_char.zfill(6)
        binary_string += binary_char
    return binary_string


filename = "input.txt"
output_filename = "output.txt"

with open(filename, 'r', encoding='utf-8') as file, open(output_filename, 'w', encoding='utf-8') as output_file:
    for line in file:
        line = line.rstrip()
        number = text_to_binary(line)
        has_six_zeros = '000000' in number
        output_file.write(f"Строка:\n {line}\n")
        output_file.write(f"Двоичное представление: {number}\n")
        if has_six_zeros:
            output_file.write('Нет - в строке встречается шесть нулей подряд\n\n')
        else:
            output_file.write('Да - в строке не встречается шесть нулей подряд\n\n')
        # Также выводим на консоль
        print(f"Строка:\n {line}")
        print(f"Двоичное представление: {number}")
        if has_six_zeros:
            print('Нет - в строке встречается шесть нулей подряд\n')
        else:
            print('Да - в строке не встречается шесть нулей подряд\n')
