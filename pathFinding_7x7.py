try:
   import Queue
except ImportError:
   import queue as Queue
import math

### Part 1: define search state
class PathFindingState:
    """
    0 = blank
    1 = obstacle
    2 = start point
    3 = goal point
    ----------------
    | 0 0 0 0 0 0 0|
    | 0 0 0 0 0 0 0|
    | 0 2 0 0 1 0 0|
    | 0 0 0 0 0 0 0|
    | 0 1 0 0 1 0 0|
    | 0 0 0 0 1 3 0|
    | 0 0 0 0 0 0 0|
    ----------------
    """
    def __init__(self, numberList):
        self.cells = []
        self.cells = numberList[:]
        self.cellsize = int(math.sqrt(len(self.cells)))
        for index in range( self.cellsize*self.cellsize ):
            if self.cells[index] == 2:
                    self.currentLocation = index
            if self.cells[index] == 3:
                    self.goalLocation = index           

    def goalState(self):
        if self.currentLocation == self.goalLocation:
            return True
        return False

    def nextActions(self):
        actions = []
        index = self.currentLocation
        if (index>=self.cellsize)  and (self.cells[index-self.cellsize]!=1):
            actions.append('up')
        if (index<(self.cellsize*(self.cellsize-1))) and (self.cells[index+self.cellsize]!=1):
            actions.append('down')
        if ((index%self.cellsize)!=0) and (self.cells[index-1]!=1):
            actions.append('left')
        if ((index%self.cellsize)!=(self.cellsize-1)) and (self.cells[index+1]!=1):
            actions.append('right')
        return actions

    def nextState(self, action):
        index = self.currentLocation
        if(action == 'up'):
            new_index = index - self.cellsize
        elif(action == 'down'):
            new_index = index + self.cellsize
        elif(action == 'left'):
            new_index = index - 1
        elif(action == 'right'):
            new_index = index + 1
        newState = PathFindingState([0]*49)
        newState.cells = self.cells[:]
        newState.cells[index] = 0
        newState.cells[new_index] = 2
        newState.currentLocation = new_index
        newState.goalLocation = self.goalLocation
        return newState

    def __str__(self):
        lines = []
        dashLine = '-' * (self.cellsize*2 + 3)
        lines.append(dashLine)
        for n in range(self.cellsize):
            newLine = '|'
            for cell in self.cells[self.cellsize*n:self.cellsize*(n+1)]:
                if cell == 0:
                    newLine += ' '
                elif cell == 1:
                    newLine += 'X'
                elif cell == 2:
                    newLine += 'S'
                elif cell == 3:
                    newLine += 'G'
            newLine += '|'
            newLine = ' '.join(newLine)
            lines.append(newLine)
        lines.append(dashLine)
        lines = '\n'.join(lines)
        return lines

    def __eq__(self, other):
        return (self.cells == other.cells)

    def __hash__(self):
        return hash(str(self.cells))

### Part 2: define seacrh problem
class searchProblem:
    def __init__(self, state):
        self.state = state

    def currentState(self):
        return self.state

    def nextStates(self, state):
        next = []
        for action in state.nextActions():
            next.append((state.nextState(action), action, 1))
        return next

    def theEnd(self, state):
        return state.goalState()


### Part 3: define seacrh method
def depthFirstSearch(problem):
    fringeQueue = Queue.LifoQueue()       
    visited = set([])
    path = ()
    node = problem.currentState()
    fringeQueue.put((node, path))
    while (fringeQueue):
        (node, path) = fringeQueue.get()
        if problem.theEnd(node):
            return path
            break
        if node not in visited:
            successors = problem.nextStates(node)
            visited.add(node)
        else:
            successors = []
        for successor in successors:
            if successor[0] not in visited:
                fringeQueue.put(( successor[0], path+(successor[1],) ))

def breadthFirstSearch(problem):
    fringeQueue = Queue.Queue()       
    visited = set([])
    path = ()
    node = problem.currentState()
    fringeQueue.put((node, path))
    while (fringeQueue):
        (node, path) = fringeQueue.get()
        if problem.theEnd(node):
            return path
            break
        if node not in visited:
            successors = problem.nextStates(node)
            visited.add(node)
        else:
            successors = []
        for successor in successors:
            if successor[0] not in visited:
                fringeQueue.put(( successor[0], path+(successor[1],) ))

def manDistance(state):
    cx = state.currentLocation%7
    cy = state.currentLocation//7
    gx = state.goalLocation%7
    gy = state.goalLocation//7
    return ( abs(gx-cx) + abs(gy-cy) )

def greedySearch(problem):
    fringeQueue = Queue.PriorityQueue()       
    visited = set([])
    priority_number = 0
    path = ()
    node = problem.currentState()
    fringeQueue.put(( priority_number, (node, path) ))
    while (fringeQueue):
        (priority_number, (node, path)) = fringeQueue.get()
        if problem.theEnd(node):
            return path
            break
        if node not in visited:
            successors = problem.nextStates(node)
            visited.add(node)
        else:
            successors = []
        for successor in successors:
            if successor[0] not in visited:
                priority_number = manDistance(successor[0])
                fringeQueue.put(( priority_number, ( successor[0], path+(successor[1],) ) ))

def aStarSearch(problem):
    fringeQueue = Queue.PriorityQueue()       
    visited = set([])
    priority_number = 0
    path = ()
    node = problem.currentState()
    fringeQueue.put(( priority_number, (node, path) ))
    while (fringeQueue):
        (priority_number, (node, path)) = fringeQueue.get()
        if problem.theEnd(node):
            return path
            break
        if node not in visited:
            successors = problem.nextStates(node)
            visited.add(node)
        else:
            successors = []
        for successor in successors:
            if successor[0] not in visited:
                priority_number = len(path) + manDistance(successor[0])
                fringeQueue.put(( priority_number, ( successor[0], path+(successor[1],) ) ))

### Part 4: main program
if __name__ == '__main__':
    numberList = [  0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, \
                    0, 2, 0, 0, 1, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, \
                    0, 1, 0, 0, 1, 0, 0, \
                    0, 0, 0, 0, 1, 3, 0, \
                    0, 0, 0, 0, 0, 0, 0  ]
    state = PathFindingState(numberList)
    problem = searchProblem(state)
    path = depthFirstSearch(problem)
    # path = breadthFirstSearch(problem)
    # path = greedySearch(problem)
    # path = aStarSearch(problem)

    print('========================================')
    print('Need %d moves to solve this puzzle: %s' % (len(path), str(path)))
    print('========================================')
    print(state)
    i = 1
    for action in path:
        state = state.nextState(action)
        print('move#%d: %s' % (i, action))
        print(state)
        i += 1
