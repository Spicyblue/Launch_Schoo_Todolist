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

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last(), "This is not the last todo")
    
    def test_all_done(self):
        self.assertFalse(self.todos.all_done(), "Some todos to be done")

    def test_add_invalid(self):
        with self.assertRaises(TypeError, msg= "This is not a todo object"):
            self.todos.add(123)
        with self.assertRaises(TypeError, msg= "This is not a todo object"):
            self.todos.add('Fix Computer')
        with self.assertRaises(TypeError, msg= "This is not a todo object"):
            self.todos.add(self.todos)

if __name__ == "__main__":
    print('Test starting')
    try:
        unittest.main()
    finally:
        print('Test ended')