from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def homepage():
     """A homepage with handy links for your convenience."""
     return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        <input type="submit" value="Submit!"><br/>
        WHat toppings do you want?
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">

    </form>
    """


@app.route('/froyo_results')
def show_froyo_results():
    
    context = {
        'users_froyo_flavor': request.args.get('flavor'),
        'users_froyo_top' : request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)



@app.route('/favorite')
def favorite():
    """Shows favorite things"""
    return """
    <form action="/favorite_results" method="GET">
        What is your favorite color, animal, and city? <br/>
        <input type="text" name="color"><br/>
        <input type="submit" value="Submit!">
        <input type="text" name="animal"><br/>
        <input type="submit" value="Submit!">
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!"
        </form>
    """

@app.route('/favorite_results')
def favorite_results():
    users_favorite_color = request.args.get('flavor')
    users_favorite_animal = request.args.get('color')
    users_favorite_city = request.args.get('city')
    return f'Wow, I didnt know {users_favorite_color} {users_favorite_animal}lives in {users_favorite_city}!'



@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        What is your secret message <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
        </form>
    """

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))



@app.route('/message_results', methods=['POST'])
def message_results():
    
    message = request.form.get('message')
    return sort_letters(message)

@app.route('/calculator')
def calculator():
     """Shows the user a form to enter 2 numbers and an operation."""
     return """
     <form action="/calculator_results" method="GET">
         Please enter 2 numbers and select an operator.<br/><br/>
         <input type="number" name="operand1">
         <select name="operation">
             <option value="add">+</option>
             <option value="subtract">-</option>
             <option value="multiply">*</option>
             <option value="divide">/</option>
         </select>
         <input type="number" name="operand2">
         <input type="submit" value="Submit!">
     </form>
     """

@app.route('/calculator_results')
def calculator_results():
    operand1 = int(request.args.get('operand1'))
    operand2 = int(request.args.get('operand2'))
    operation = request.args.get('operation')
    total = 0 

    if(operation == "add"):
        total = operand1 + operand2
    elif(operation == "subtract"):
        total = operand1 + operand2
    elif(operation == "multiply"):
        total = operand1 + operand2
    elif(operation == "divide"):
        total = operand1 + operand2
    context = {
        'operand1': int(request.args.get('operand1')),
        'operand2': int(request.args.get('operand2')),
        'operation': request.args.get('operation'),
        'total': total
    }

    return render_template('calculator_results.html', **context)

     

if __name__ == '__main__':
    app.run(debug=True)
