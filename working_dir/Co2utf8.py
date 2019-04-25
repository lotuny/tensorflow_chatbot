import os.path as op

if __name__ == '__main__':
    file_path = op.join(op.abspath(op.dirname(op.abspath(__file__))), 'vocab20000.enc')

    try:
        file = open(file_path, mode='rb', encoding='utf-8')
        temp_file = ''
        for byte in file:
            try:
                decode = byte.decode()
                temp_file += decode
            except UnicodeDecodeError:
                print('%s will be ignored.' % byte)
        file.close()

        file = open(file_path, mode='w', encoding='utf-8')
        file.write(temp_file)
        file.close()
    except FileNotFoundError:
        print('File not found.')
    else:
        print('File found.')


