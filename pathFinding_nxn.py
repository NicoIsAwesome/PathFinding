# pathFinding_nxn.py

try:
   import Queue
except ImportError:
   import queue as Queue
import math

########## Module Classes ##########

class PathFindingState:
    """
    0 = blank
    1 = obstacle
    2 = start point
    3 = goal point
    -----------------------------
    | 0 0 0 0 0 0 0 0 0 0 0 0 3 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 2 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 0 0 0 0 0 0 0 |
    -----------------------------
    """

    def __init__( self, numbers ):
        """
        initialize following variables
        self.cellsize
        self.cells
        self.currentLocation
        self.goalLocation
        """
        self.cells = []
        self.cells = numbers[:]
        self.cellsize = int(math.sqrt(len(self.cells)))
        for index in range( self.cellsize*self.cellsize ):
            if self.cells[index] == 2:
                    self.currentLocation = index
            if self.cells[index] == 3:
                    self.goalLocation = index           

    def isGoal( self ):
        """
          Checks to see if the puzzle is in its goal state.
        """
        if self.currentLocation != self.goalLocation:
            return False
         
        return True

    def legalMoves( self ):
        """
        Returns a list of legal moves from the current state.

        Moves consist of moving the current location up, down, left or right.
        These are encoded as 'up', 'down', 'left' and 'right' respectively.

        >>> PathFindingState(numbers).legalMoves() = ['up', 'down', 'left', 'right']
        top column can't go up
        bottom column can't go down
        left row can't go left
        right row can't go right
        """
        moves = []
        index = self.currentLocation
        if (index>=self.cellsize)  and (self.cells[index-self.cellsize]!=1):
            moves.append('up')
        if (index<(self.cellsize*(self.cellsize-1))) and (self.cells[index+self.cellsize]!=1):
            moves.append('down')
        if ((index%self.cellsize)!=0) and (self.cells[index-1]!=1):
            moves.append('left')
        if ((index%self.cellsize)!=(self.cellsize-1)) and (self.cells[index+1]!=1):
            moves.append('right')
        return moves

    def result(self, move):
        """
          Returns a new Puzzle (PathFindingState) with
        - newPuzzle.cells
        - newPuzzle.currentLocation
        - newPuzzle.goalLocation
        updated based on the provided move.

        The move should be a string drawn from a list returned by legalMoves.
        Illegal moves will raise an exception, which may be an array bounds
        exception.

        NOTE: This function *does not* change the current object.  Instead,
        it returns a new object.
        """
        index = self.currentLocation
        if(move == 'up'):
            new_index = index - self.cellsize
        elif(move == 'down'):
            new_index = index + self.cellsize
        elif(move == 'left'):
            new_index = index - 1
        elif(move == 'right'):
            new_index = index + 1
        else:
            raise "Illegal Move"

        # Create a copy of the current eightPuzzle
        newPuzzle = PathFindingState([0]*self.cellsize*self.cellsize)
        newPuzzle.cells = self.cells[:]
        # And update it to reflect the move
        newPuzzle.cells[index] = 0
        newPuzzle.cells[new_index] = 2
        newPuzzle.currentLocation = new_index
        newPuzzle.goalLocation = self.goalLocation

        return newPuzzle

    # Utilities for comparison and display
    def __eq__(self, other):
        """
            Overloads '==' such that two puzzles with the same puzzle.cells
          are equal.
        """
        if self.cells != other.cells:
            return False
        return True

    def __hash__(self):
        return hash(str(self.cells))

    def __getAsciiString(self):
        """
          Returns a display string for the maze
        """
        lines = []
        horizontalLine = ('-' * (self.cellsize*2 + 3))
        lines.append(horizontalLine)
        for n in range(self.cellsize):
            rowLine = '|'
            for col in self.cells[self.cellsize*n:self.cellsize*(n+1)]:
                if col == 0:
                    col = ' '
                elif col == 1:
                    col = 'X'
                elif col == 2:
                    col = 'S'
                elif col == 3:
                    col = 'G'
                rowLine = rowLine + ' ' + col.__str__()
            rowLine = rowLine + ' |'
            lines.append(rowLine)
        lines.append(horizontalLine)

        return '\n'.join(lines)

    def __str__(self):
        return self.__getAsciiString()

# TODO: Implement The methods in this class

class PathFindingProblem:
    """
      Implementation of a PathFindingProblem for the search algorithms
    """
    def __init__(self,puzzle):
        "Creates a new EightPuzzleSearchProblem which stores search information."
        self.puzzle = puzzle

    def getStartState(self):
        return puzzle

    def isGoalState(self,state):
        return state.isGoal()

    def getSuccessors(self,state):
        """
          Returns list of (successor, action, stepCost) pairs where
          each succesor is either left, right, up, or down
          from the original state and the cost is 1.0 for each
        """
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 1))
        return succ

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return len(actions)


########## Search Module ##########
"""
q = Queue.Queue()           # FIFO
q = Queue.LifoQueue()       # Stack
q = Queue.PriorityQueue()   # Priority Queue

q.put(obj), q.put((number, obj))
q.get(obj)
while not q.empty():

Priority Queue
The lowest valued entries are retrieved first
A typical pattern for entries is a tuple in the form: (priority_number, data)
"""

def distHeuristic(state, problem=None):
    xy1 = [state.currentLocation%state.cellsize, state.currentLocation//state.cellsize]
    xy2 = [state.goalLocation%state.cellsize, state.goalLocation//state.cellsize]
    heur = abs(xy1[0]-xy2[0]) + abs(xy1[1]-xy2[1])
    return heur

def xfsSearch(problem, algo='bfs'):
    """ Search the deepest nodes in the search tree first."""
    if algo == 'dfs':
        fringeQueue = Queue.LifoQueue()     # dfs = LIFO, Stack
    else:
        fringeQueue = Queue.Queue()         # bfs = FIFO, Queue       
    visited = set([])       # set = set([1, 2, 3, 4, 5 ])
    path = ()               # tuple = (1, 2, 3, 4, 5 )
    node = problem.getStartState()
    fringeQueue.put((node, path))    # fringeQueue = [tup1, tip2, ...]
    while (fringeQueue):
        # print(len(visited))
        (node, path) = fringeQueue.get()   # pop()=dfs
        if problem.isGoalState(node):
            return path
            break
        if node not in visited:
            successors = problem.getSuccessors(node)
            visited.add(node)
        else:
            successors = []
        for successor in successors:
            if successor[0] not in visited:
                # print(successor[0], path+(successor[1],))
                fringeQueue.put(( successor[0], path+(successor[1],) ))

def aStarSearch(problem, heuristic=distHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringeQueue = Queue.PriorityQueue()
    visited = set([])
    path = ()
    cost = 0
    heur = 0
    node = problem.getStartState()
    fringeQueue.put( (heur, (node, path, cost)) )
    # while not fringeQueue.empty():
    while (fringeQueue):
        # print(len(visited))
        (heur, (node, path, cost)) = fringeQueue.get()      
        if problem.isGoalState(node):
            return path
            break
        if node not in visited:
            successors = problem.getSuccessors(node) # tuple = (next_node, action, cost)
            visited.add(node)
        else:
            successors = []
        for successor in successors: # successor[0]=next_node, successor[1]=action, successor[2]=cost
            if successor[0] not in visited:
                heur = cost+successor[2]+heuristic(successor[0],problem)
                # print((heur, (successor[0], path+(successor[1],), cost+successor[2])))
                fringeQueue.put( (heur, (successor[0], path+(successor[1],), cost+successor[2])) )
      

########## Main Program ##########

if __name__ == '__main__':
    # <=== must update here
    numberList = [ \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, \
        0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, \
        0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, \
        0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, \
        0, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 1, 0, \
        0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0  ]

    puzzle = PathFindingState(numberList)
    problem = PathFindingProblem(puzzle)

    # path = xfsSearch(problem, 'bfs')    # 'bfs' or 'dfs'
    path = aStarSearch(problem, distHeuristic)

    print('Found a path of %d moves: %s' % (len(path), str(path)))
    curr = puzzle
    i = 1
    for a in path:
        curr = curr.result(a)
        print('After %d move%s: %s' % (i, ("", "s")[i>1], a))
        print(curr)
        # raw_input("Press return for the next state...")   # wait for key stroke
        i += 1
