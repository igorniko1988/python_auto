

def test_todos(app):
    app.todomvc.open('https://todomvc.com/examples/emberjs/')
    app.todomvc.add_todo('a', 'b')
    app.todomvc.todo_should_have('a', 'b')


def test_todos_another(app):
    app.todomvc.open('https://todomvc.com/examples/emberjs/')
    app.todomvc.add_todo('c', 'd')
    app.todomvc.todo_should_have('c', 'd')

