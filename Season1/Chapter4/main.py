
from flask import Flask
from time import sleep
import common as c

app = Flask(__name__)


prime_generatior = (n for n in range(10 ** 10) if c.is_prime(n))
def main():
    for i in range(10):
        print(next(prime_generatior))




@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/prime_number')
def prime_number():
    return str(next(prime_generatior))

if __name__ == '__main__':
    app.run()



