def process_text(text):
    result = []
    buffer = []
    in_bracket = False

    for char in text:
        if char == '[':
            in_bracket = True
            buffer.insert(0, "")  
        elif char == ']':
            in_bracket = False
        elif in_bracket:
            buffer[0] += char  
        else:
            result.append(char)

    return "".join(buffer) + "".join(result)

input_text = str(input())
output_text = process_text(input_text)
print(output_text)
