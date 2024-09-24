'''
The Todo List mini application
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

    def each(self, callback):
        for todos in self._todos:
            callback(todos)

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
    
    def all_done(self):
        return all(todo.done for todo in self._todos)
    
    def mark_all_done(self):
        for todos in self._todos:
            todos.done = True
    
    def mark_all_undone(self):
        for todos in self._todos:
            todos.done = False

    def mark_done_at(self, idx):
        self.todo_at(idx).done = True

    def mark_undone_at(self, idx):
        self.todo_at(idx).done = False

    def select(self, callback):
        new_list = TodoList(self._title)

        def choose(todo):
            if callback(todo):
                new_list.add(todo)
           
        self.each(choose)

        return new_list

    def remove_at(self, idx):
        self._todos.pop(idx)

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

    print('\n')

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

    print('\n')

def step_3():
    '''
    Get the Lenghts of a Todos
    '''
    print('--------------------------------- Step 3')
    todo_list = setup()

    print(len(todo_list))              # 3
    print(len(empty_todo_list))        # 0
    print('\n')

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

    print('\n')

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
    print('\n')

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
    print('\n')

def step_7():
    '''
    Mark Todo as Completed or Not Completed by Index Position
    '''
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

    print('\n')

def step_8():
    '''
    Mark all Todos as Completed or Not Completed
    '''
    print('--------------------------------- Step 8')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_all_done()
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [X] Go to gym

    todo_list.mark_all_undone()
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

    print('\n')

def step_9():
    '''
    Return True for all Completed Todos
    '''
    print('--------------------------------- Step 9')
    todo_list = setup()

    print(todo_list.all_done())         # False

    todo_list.mark_all_done()
    print(todo_list.all_done())         # True

    todo_list.mark_undone_at(1)
    print(todo_list.all_done())         # False

    print(empty_todo_list.all_done())   # True

    print('\n')

def step_10():
    '''
    Remove a Todo by Index
    '''
    print('--------------------------------- Step 10')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.remove_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Go to gym

    todo_list.remove_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk

    try:
        todo_list.remove_at(1)
    except IndexError:
        print('Expected IndexError: Got it!')

    todo_list.remove_at(0)
    print(todo_list)
    # ---- Today's Todos -----

    print('\n')

def step_11():
    '''
    Add a Generic Iteration Method to the TodoList
    '''
    print('--------------------------------- Step 11')
    todo_list = setup()

    todo_list.mark_all_undone()
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

    def done_if_y_in_title(todo):
        if 'y' in todo.title:
            todo.done = True

    todo_list.each(done_if_y_in_title)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [ ] Clean room
    # [X] Go to gym

    todo_list.each(lambda todo: print('>>>', todo))
    # >>> [X] Buy milk
    # >>> [ ] Clean room
    # >>> [X] Go to gym
    print('\n')

def step_12():
    '''
    Selecting Todos
    '''
    print('--------------------------------- Step 12')
    todo_list = setup()

    def y_in_title(todo):
        return 'y' in todo.title

    print(todo_list.select(lambda todo: y_in_title))
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Go to gym

    print(todo_list.select(lambda todo: todo.done))
    # ---- Today's Todos -----
    # [X] Clean room

    print('\n')

def main():
    step_1() 
    step_2()
    step_3()
    step_4()
    step_5()
    step_6()
    step_7()
    step_8()
    step_9()
    step_10()
    step_11()
    step_12()

main()