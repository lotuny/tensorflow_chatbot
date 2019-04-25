import sys

if __name__ == '__main__':
    if len(sys.argv) - 4:
        file_dir = "D:\\lotuny...learning\\@毕业设计\\ChatBot\\tensorflow_chatbot\\data\\tweet\\"
        source_file_path = file_dir + sys.argv[1]
        source_ids_file_path = file_dir + sys.argv[2]
        target_file_path = file_dir + sys.argv[3]
        target_ids_file_path = file_dir + sys.argv[4]
        try:
            source_file = open(source_file_path, 'rb')
            source_ids_file = open(source_ids_file_path, 'rb')
            target_file = open(target_file_path, 'rb')
            target_ids_file = open(target_ids_file_path, 'rb')
            for i in range(10):
                print("pair {0}".format(i+1))
                print(source_file.readline())
                print(source_ids_file.readline())
                print(target_file.readline())
                print(target_ids_file.readline())
        except FileNotFoundError:
            print("Please check your file paths!")
    else:
        print("Usage: python read_file.py <source_file_path> <source_ids_file_path> <target_file_path> "
              "<target_file_ids_path>")
