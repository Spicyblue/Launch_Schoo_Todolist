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