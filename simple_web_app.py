#! python
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

from flask import Flask
app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/fibonacci/<int:n>')
def fibo(n):
    return f"The {n}th Fibonacci number is {fibonacci(n)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)