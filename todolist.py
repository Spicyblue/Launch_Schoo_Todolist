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
        self._title = title
        self._done = False

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

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError('Can only add Todo Object ')
        
        self._todos.append(todo)

    def __len__(self):
        return len(self._todos)
    
    def first(self):
        return self._todos[0]
    
    def last(self):
        return self._todos[-1]
    
    def to_list(self):
        return list(self._todos)
    
    def todo_at(self, idx):
        if not isinstance(idx, int):
            raise TypeError('Please enter an number')
        
        return self._todos[idx]
    
    def mark_done_at(self, idx):
        self.todo_at(idx).done = True

    def mark_undone_at(self, idx):
        self.todo_at(idx).done = False

    def __str__(self):
        output_lines = [f'----- {self._title} -----']
        output_lines += [str(todo) for todo in self._todos]
        return '\n'.join(output_lines)

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list

empty_todo_list = TodoList('Nothing Doing')

def step_1():
    '''
    Adding Todo Objects to the TodoList.
    '''
    print('--------------------------------- Step 1')
    todo_list = setup()

    try:
        todo_list.add(1)
    except TypeError:
        print('TypeError detected')    # TypeError detected

    for todo in todo_list._todos:
        print(todo)

def step_2():
    '''
    Output Formatting.
    '''
    print('--------------------------------- Step 2')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

def step_3():
    '''
    In this step, you need to customize the behavior of the len function,
    which you can do with the __len__ magic method.
    '''
    print('--------------------------------- Step 3')
    todo_list = setup()

    print(len(todo_list))              # 3
    print(len(empty_todo_list))        # 0

def step_4():
    '''
    Retrieving the First and Last Todos.
    '''
    print('--------------------------------- Step 4')
    todo_list = setup()

    print(todo_list.first())           # [ ] Buy milk
    print(todo_list.last())            # [ ] Go to gym

    try:
        empty_todo_list.first()
    except IndexError:
        print('Expected IndexError: Got it!')

    try:
        empty_todo_list.last()
    except IndexError:
        print('Expected IndexError: Got it!')

def step_5():
    '''
    Obtaining Todos as a List.
    '''
    print('--------------------------------- Step 5')
    todo_list = setup()

    print(empty_todo_list.to_list())    # []

    todos = todo_list.to_list()
    print(type(todos).__name__)         # list

    for todo in todos:
        print(todo)                     # [ ] Buy milk
                                        # [X] Clean room
                                        # [ ] Go to gym

def step_6():
    '''
    Retrieve Todo by Index Position.
    '''
    print('--------------------------------- Step 6')
    todo_list = setup()

    print(todo_list.todo_at(0))        # [ ] Buy milk
    print(todo_list.todo_at(1))        # [X] Clean room
    print(todo_list.todo_at(2))        # [ ] Go to gym

    try:
        todo_list.todo_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    # Ensure we have a reference
    print(todo_list.todo_at(1) is todo_list.todo_at(1))  # True

def step_7():
    print('--------------------------------- Step 7')
    todo_list = setup()

    todo_list.mark_done_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_done_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_done_at(2)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [X] Go to gym

    try:
        todo_list.mark_done_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    todo_list.mark_undone_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [X] Go to gym

    todo_list.mark_undone_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [X] Go to gym

    todo_list.mark_undone_at(2)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

    try:
        todo_list.mark_undone_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

def main():
    step_1()
    step_2()
    step_3()
    step_4()
    step_5()
    step_6()
    step_7()

main()
