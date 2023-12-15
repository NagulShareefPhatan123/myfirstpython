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
