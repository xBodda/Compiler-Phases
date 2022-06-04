from app.tokenizer import Tokenize

tokenizer = Tokenize('''
double *Y^##a = 2.2
double a = 2.2
int b = 3
string c = "Hello"

''')
tokens =  tokenizer.tokenize()

for i in tokens:
    print(i)
