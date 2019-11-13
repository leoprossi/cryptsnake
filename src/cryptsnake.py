from argument_handler import ArgumentHandler
from file_handler import read, write
from exceptions import MissingParameterException
import encryption

if __name__ == "__main__":
    args = ArgumentHandler().parse()

    if args.MODE == 'K':
        key = encryption.generateKey(args.KEY)
        write(key, args.OUTPUT)
    else:
        if args.INPUT == None:
            raise MissingParameterException('Missing input file')
        text = read(args.INPUT)
        key = read(args.KEY)
        proccessed_text = encryption.encrypt(text, key, reverse=(args.MODE == 'D'))
        write(proccessed_text, args.OUTPUT)
