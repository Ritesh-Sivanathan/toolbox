
class Function:

    def __init__(self, function):
        self.function = function

    def show(self):
        return self.function
    
    def substitute(self, **kwargs): # basic substitution on very basic functions (for now)
        
        values = {}

        for key, val in kwargs.items():
            values[key] = val
        
        "f(x)=3x+2" # basic linear function

        # fill in all variables with corresponding (val), then evaluate using + / - / * / /