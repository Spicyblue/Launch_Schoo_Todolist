'''
The Todo class represents a single todo item for our TodoList. 
We'll need the following features:

Each Todo object should have state that consists of a title for the todo and 
a flag that indicates whether it has been completed.

Both state attributes should be defined as properties.
Both properties require a getter.
Only the Todo completion property requires a setter.
When printing Todo objects, they should be formatted as shown here:

[ ] Buy milk
[X] Clean room
[ ] Go to gym

In this format, [ ] indicates a Todo that hasn't been completed yet,
while [X] indicates a completed Todo.
We'll use a couple of class constants for the X and (blank) values.

The text on the right is the title text.
Two Todo objects are equal when they have the same values for the title and completion attributes.

Based on the above requirements, try to come up with your own Todo class.
The following code demonstrates how the Todo class works. You can use this code to test your class:

'''
class Todo:
    IS_DONE = 'X'
    IS_UNDONE = ' '

    def __init__(self, title):
        self.title = title
        self.done = False

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, done):
        self._done = done

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        
        return (self.title == other.title) and (self.done == other.done)

    def __str__(self):

        if self.done:
            return f"[{self.IS_DONE}] {self._title}"
        
        return f"[{self.IS_UNDONE}] {self._title}"
    
def test_todo():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')
    todo4 = Todo('Clean room')

    print(todo1)                  # [ ] Buy milk
    print(todo2)                  # [ ] Clean room
    print(todo3)                  # [ ] Go to gym
    print(todo4)                  # [ ] Clean room

    print(todo2 == todo4)         # True
    print(todo1 == todo2)         # False
    print(todo4.done)             # False

    todo1.done = True
    todo4.done = True
    print(todo4.done)             # True

    print(todo1)                  # [X] Buy milk
    print(todo2)                  # [ ] Clean room
    print(todo3)                  # [ ] Go to gym
    print(todo4)                  # [X] Clean room

    print(todo2 == todo4)         # False

    todo4.done = False
    print(todo4.done)             # False
    print(todo4)                  # [ ] Clean room

test_todo()