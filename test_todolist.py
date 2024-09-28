import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos), "Not exactly 3 todos in your list")

    def test_to_list(self):
        todo_list = [self.todo1, self.todo2, self.todo3]
        self.assertEqual(todo_list, self.todos.to_list(), "List objects are not equall")

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first(), "This is not the first todo")

if __name__ == "__main__":
    print('Test starting')
    try:
        unittest.main()
    finally:
        print('Test ended')