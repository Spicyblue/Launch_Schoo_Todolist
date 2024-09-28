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

    def test_todo_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0), "This is not the right value for the index")
        self.assertEqual(self.todo2, self.todos.todo_at(1), "This is not the right value for the index")
        self.assertEqual(self.todo3, self.todos.todo_at(2), "This is not the right value for the index")
        with self.assertRaises(TypeError, msg= "Enter an integer number"):
            self.todos.todo_at('One')
        with self.assertRaises(IndexError, msg= "This index is not accessible"):
            self.todos.todo_at(5)
    
    def test_mark_done_at(self):
        with self.assertRaises(TypeError, msg= "Enter an integer number"):
            self.todos.mark_done_at('One')
        with self.assertRaises(IndexError, msg= "This index is not accessible"):
            self.todos.mark_done_at(5)
        
        self.todos.mark_done_at(1)
        self.assertFalse(self.todo1.done, "This is True")
        self.assertTrue(self.todo2.done, "This is False")
        self.assertFalse(self.todo3.done, "This is True")

    def test_mark_undone_At(self):
        with self.assertRaises(TypeError, msg= "Enter an integer number"):
            self.todos.mark_undone_at('One')
        with self.assertRaises(IndexError, msg= "This index is not accessible"):
            self.todos.mark_undone_at(5)

        self.todo1.done = True
        self.todo2.done = True
        self.todo3.done = True
        
        self.todos.mark_undone_at(0)
        self.assertFalse(self.todo1.done, "This is True")
        self.assertTrue(self.todo2.done, "This is False")
        self.assertTrue(self.todo3.done, "This is False")

    def test_mark_all_done(self):
        self.todo1.done = False
        self.todo2.done = False
        self.todo3.done = False

        self.todos.mark_all_done()
        self.assertTrue(self.todo1.done, "This is False")
        self.assertTrue(self.todo2.done, "This is False")
        self.assertTrue(self.todo3.done, "This is False")
        self.assertTrue(self.todos.all_done())

    def test_remove_at(self):
        with self.assertRaises(TypeError, msg= "Enter an integer number"):
            self.todos.remove_at('One')
        with self.assertRaises(IndexError, msg= "This index is not accessible"):
            self.todos.remove_at(5)


        self.todos.remove_at(1)
        self.assertEqual(2, len(self.todos), "Not exactly 3 todos in your list")
        self.assertEqual([self.todo1, self.todo3], self.todos.to_list(), "This has more items in the todo list")

    
    def test_str(self):
        string = (
        "----- Today's Todos -----\n"
        "[ ] Buy milk\n"
        "[ ] Clean room\n"
        "[ ] Go to the gym"
        )
        self.assertEqual(string, str(self.todos))

    def test_str_done_todo(self):
        string = (
        "----- Today's Todos -----\n"
        "[ ] Buy milk\n"
        "[X] Clean room\n"
        "[ ] Go to the gym"
        )
        self.todos.mark_done_at(1)
        self.assertEqual(string, str(self.todos))

    

if __name__ == "__main__":
    print('Test starting')
    try:
        unittest.main()
    finally:
        print('Test ended')