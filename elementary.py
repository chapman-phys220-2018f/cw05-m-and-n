    """Memoized version of the factorial of x: x!
       This stores the product of all positive integers less
       than or including x when called.
    
    Attributes:
    -----------
    data : {int : int}
        Stored results of factorial
    """
    
    def __init__(self):
        """Constructor for Factorial of x"""
        self.data = dict()
    
    def __call__(self, x):
        """Compute factorial of x"""
        assert (type(x)==int and x >= 0), "Not a positive integer"
        if x not in self.data.keys():
            self.data[x] = ft.reduce(op.mul, range(1,x+1), 1)
        return self.data[x]

fac = Factorial() # replaces previous function definition

