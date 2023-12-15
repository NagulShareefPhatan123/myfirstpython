
requirements.txt
Creating a simple REST API in Python can be a great project to understand the basics of web development and API design. Here's an example project where we'll create a basic To-Do list API using the Flask framework:

Install Flask:
Make sure you have Flask installed. You can install it using the following command:

bash
Copy code
pip install Flask
Create the project structure:
Create a new directory for your project and create the following files:

app.py: The main script for your Flask application.
requirements.txt: List of dependencies for your project.
Write the code:

python
Copy code
# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for the To-Do list
todo_list = [
    {"id": 1, "task": "Buy groceries", "done": False},
    {"id": 2, "task": "Finish project", "done": True},
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"todos": todo_list})

@app.route('/todos', methods=['POST'])
def add_todo():
    if not request.json or 'task' not in request.json:
        return jsonify({"error": "Invalid request"}), 400

    new_todo = {
        "id": len(todo_list) + 1,
        "task": request.json['task'],
        "done": False
    }
    todo_list.append(new_todo)
    return jsonify({"todo": new_todo}), 201

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todos = [todo for todo in todo_list if todo['id'] == todo_id]
    if len(todos) == 0:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"todo": todos[0]})

if __name__ == '__main__':
    app.run(debug=True)
Run the application:
Navigate to your project directory and run the following command to start the Flask development server:

bash
Copy code
python app.py
Your API will be accessible at http://127.0.0.1:5000/.

Test the API:
You can use tools like curl, Postman, or your browser to interact with the API. For example:

To get the list of todos: GET http://127.0.0.1:5000/todos
To add a new todo: POST http://127.0.0.1:5000/todos with a JSON payload {"task": "New task"}
To get a specific todo: GET http://127.0.0.1:5000/todos/1
This is a simple example, and you can extend it by adding features like updating and deleting todos, user authentication, and more. Additionally, you can explore Flask extensions like Flask-RESTful to simplify API development further