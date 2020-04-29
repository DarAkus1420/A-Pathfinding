class Node:

    '''
    The node object contains all the properties that the node object
    should contain to perform the algorithm
    Is an object used for every node on the grid
    Args:
        x (int): The x position of the node wen instantiating it
        y (int): The y position of the node wen instantiating it
    
    Attributes:
        x (int): X position of the node
        y (int): Y position of the node
        father (Node): Parent node of current node
        f (int): Value of the equation f
        h (int): Cost of the path from the start node to this node
        g (int): Cost of the cheapest path from this node to the goal
        transitable (int): Defines if this node is passable
    '''

    def __init__(self, father, position):

        self.position = position
        self.father = father

        self._f = 0
        self._h = 0
        self._g = 0
        self._passable = None
    
    def __eq__(self, other_node):
        return self.position == other_node.position
    

    # Methods to get and set all the properties of the class

    @property
    def father(self):
        return self._father
    
    @father.setter
    def father(self, father):
        self._father = father

    @property
    def f(self):
        return self._f
    
    @f.setter
    def f(self, f):
        self._f = f

    @property
    def h(self):
        return self._h
    
    @h.setter
    def h(self, h):
        self._h = h
    
    @property
    def g(self):
        return self._g
    
    @g.setter
    def g(self, g):
        self._g = g

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position):
        self._position = position


    @staticmethod
    def is_equal(node_s, node_e):
        """ Method that evaluates if one node is 
            equal to another
            
            Args:
            node_s(Node)
            node_e(Node)

            Returns:
            boolean: Node_s equals node_e
        """
        if node_s.x == node_e.x and node_s.y == node_e.y:
            return True
        return False
