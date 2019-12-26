filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    # contents = file_object.read()
    # print(contents)
    
    lines = file_object.readlines()
    pi_string = ''

    for line in lines:
        pi_string += line.strip()

        print(pi_string[:52] + '...')
        print(len(pi_string))