def decode(message_file):
    pyramid_lines = []
    
    with open(message_file, 'r') as file:
        for line in file:
            pyramid_lines.append(line.strip().split()[1])

    decoded_message = ' '.join(pyramid_lines)
    return decoded_message


message_file = './coding_qual_input.txt'
result = decode(message_file)
print(result)