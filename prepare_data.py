import random
import sys


def gather_qapairs(file):
    questions = []
    answers = []

    line = file.readline()
    count = 1
    while line:
        if count % 10000 == 0:
            print("{0} lines are read.".format(count))
        if count % 2 != 0:
            questions.append(line)
        else:
            answers.append(line)
        count += 1
        line = file.readline()

    return questions, answers


def prepare_seq2seq_files(questions, answers, file_dir='', TESTSET_SIZE = 30000):

    # open files
    train_enc = open(file_dir + 'train.enc', 'w', encoding='utf-8', errors='ignore')
    train_dec = open(file_dir + 'train.dec', 'w', encoding='utf-8', errors='ignore')
    test_enc = open(file_dir + 'test.enc', 'w', encoding='utf-8', errors='ignore')
    test_dec = open(file_dir + 'test.dec', 'w', encoding='utf-8', errors='ignore')

    # choose 30,000 (TESTSET_SIZE) items to put into testset
    test_ids = random.sample([i for i in range(len(questions))], TESTSET_SIZE)

    for i in range(len(questions)):
        if i in test_ids:
            test_enc.write(questions[i])
            test_dec.write(answers[i])
        else:
            train_enc.write(questions[i])
            train_dec.write(answers[i])
        if i % 10000 == 0:
            print('\n>> written %d lines' % i)

    # close files
    train_enc.close()
    train_dec.close()
    test_enc.close()
    test_dec.close()


if __name__ == '__main__':
    if len(sys.argv) - 1:
        file_dir = "D:\\lotuny...learning\\@毕业设计\\ChatBot\\corpus\\"
        file_path = file_dir + sys.argv[1]

        file = open(file_path, 'r', encoding='utf-8', errors='ignore')
        questions, answers = gather_qapairs(file)
        print("Generating seq2seq_files...")
        prepare_seq2seq_files(questions, answers, file_dir)
    else:
        print("Usage: python read_file.py <file_path>")


