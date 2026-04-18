from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = []

@app.route('/')
def index():
    return render_template('todo.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todos.append({"id": len(todos)+1, "task": task, "done": False})
    return redirect(url_for('index'))

@app.route('/done/<int:task_id>')
def done(task_id):
    for todo in todos:
        if todo['id'] == task_id:
            todo['done'] = not todo['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    global todos
    todos = [t for t in todos if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
