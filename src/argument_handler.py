import argparse

class ArgumentHandler:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('MODE', type=str,help='Operation mode (encrypt = C, depcrypt = D or key = K)')
        self.parser.add_argument('INPUT', nargs='?', type=str, help='Input file for the command')
        self.parser.add_argument('OUTPUT', type=str, help='Output file for the command')
        self.parser.add_argument('KEY', type=str, help='If encrypt/decrypt, this arg should be the path to a valid encrypt key. If in key generator mode, this should be a word which is going to be used as seed for generating the key')
    
    def parse(self):
        return self.parser.parse_args();
