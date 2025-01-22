class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.next_token = None
        self.advance()

    def advance(self):
        """ Move to the next token """
        try:
            self.next_token = next(self.tokens)
        except StopIteration:
            self.next_token = None

    def parse(self):
        """ Start parsing tokens """
        while self.next_token:
            token_type, token_value = self.next_token
            print(f'Processing {token_type}: {token_value}')
            self.advance()

# Function to process inputs
def process_command(input_code):
    tokens = lex(input_code, TOKEN_SPECIFICATION)
    parser = Parser(tokens)
    parser.parse()

print('Enter your commands (type "exit" to quit):')
while True:
    user_input = input('> ')
    if user_input.lower() == 'exit':
        break
    process_command(user_input)
