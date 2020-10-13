from flask import Flask, request
from operations import add, sub, mult, div

operations = {'add': add, 'sub': sub, 'mult': mult, 'div': div}

app = Flask(__name__)

@app.route('/add')
def return_sum():
    """add a and b parameters"""
    a = float(request.args['a'])
    b = float(request.args['b'])

    return str(add(a, b))

@app.route('/sub')
def return_difference():
    """subtract b parameter from a parameter"""
    a = float(request.args['a'])
    b = float(request.args['b'])

    return str(sub(a, b))

@app.route('/mult')
def return_product():
    """multiply a and b parameters"""
    a = float(request.args['a'])
    b = float(request.args['b'])

    return str(mult(a, b))

@app.route('/div')
def return_quotient():
    """divide a parameter by b parameter"""
    a = float(request.args['a'])
    b = float(request.args['b'])

    return str(div(a, b))

@app.route('/math/<operation>')
def return_result(operation):
    """perform operation specified by operation paramter on a and b parameters"""
    a = float(request.args['a'])
    b = float(request.args['b'])

    return str(operations[operation](a, b))
