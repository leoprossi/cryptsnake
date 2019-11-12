def read(input_file):
    file = open(input_file, 'r')
    content = file.read()
    file.close()
    return content;

def write(content, output_file):
    file = open(output_file, 'w')
    file.write(str(content))
    file.close()