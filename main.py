from flask import Flask, render_template, request, redirect
app = Flask('app')

todos = [
  { 'title': 'Example 1',
    'complete': False
  },
  { 'title': 'Example 2', 
    'complete': True
  }
]

@app.route('/')
def index():
  return render_template(
    'index.html',
    todos=todos
  )

@app.route('/create', methods=['POST'])
def create():
  cat = request.form.get('category')
  title = request.form.get('title')
  todos.append({'title': title, 'complete': False, 'category': cat})
  return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  todos.pop(id)
  return redirect('/')

@app.route('/complete/<int:id>')
def complete(id):
  todos[id]['complete'] = True
  return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  title = request.form.get('title')
  todos[id]['title'] = title
  return redirect('/')

  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)