from flask import Flask, jsonify, request, abort
from datetime import datetime

app = Flask(__name__)

# Fake database
todos = [
    {'id': 1, 'task': 'Learn Flask', 'done': False},
    {'id': 2, 'task': 'Build an API', 'done': False}
]

# GET all todos
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

# GET single todo
@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        abort(404)
    return jsonify({'todo': todo})

# POST new todo
@app.route('/api/todos', methods=['POST'])
def create_todo():
    if not request.json or 'task' not in request.json:
        abort(400)
    
    todo = {
        'id': len(todos) + 1,
        'task': request.json['task'],
        'done': False,
        'created_at': datetime.now().isoformat()
    }
    todos.append(todo)
    return jsonify({'todo': todo}), 201

# PUT update todo
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        abort(404)
    
    todo['task'] = request.json.get('task', todo['task'])
    todo['done'] = request.json.get('done', todo['done'])
    return jsonify({'todo': todo})

# DELETE todo
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        abort(404)
    
    todos.remove(todo)
    return jsonify({'result': True})

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

if __name__ == '__main__':
    app.run(debug=True)