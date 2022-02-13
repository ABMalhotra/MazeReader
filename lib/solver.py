import numpy as np

class MazeSolver:

    def __init__(self,maze):
        self.maze     = maze
        self.solution = maze
        self.nrows,self.ncols = maze.shape[0],maze.shape[1]

        self.start  = self.startNode()
        self.visited= {}
        self.path   = []
        self.SolveMaze()

    def startNode(self):
        '''
        Identifies starting node (RGB = 100)
        Returns (row,col) of starting node
        '''
        startidx = np.where((self.maze[:,:,0]==1) & (self.maze[:,:,1]==0) & (self.maze[:,:,2]==0)) #RGB = (1,0,0)
        return (startidx[0][0],startidx[1][0])


    def getSuccessors(self,node):
        '''
        Given a node, returns all adjacent nodes within bounds of maze and not a wall.
        '''
        r,c = node
        potential = [(r,c+1),(r,c-1),(r+1,c), (r-1,c)]
        successors = []
        for successor in potential:
            if (successor[0]>=self.nrows or successor[0]<0 or successor[1]>=self.ncols or successor[1]<0):
                continue
            elif self.isWall(successor):
                continue
            successors.append(successor)
        return successors


    def isWall(self,node):
        '''
        Identifies if a given node is the wall.
        '''
        r, c = node
        if np.array_equal(self.maze[r,c], [0,0,0]):
            return True
        return False

    def isTarget(self,node):
        '''
        Identifies if a given node is the target
        '''
        r, c = node
        if np.array_equal(self.maze[r,c], [0,1,0]):
            return True
        return False

    def findShortestPath(self):
        '''
        Uses Breadth First Search to get to the nearest end node by the shortest path.
        '''
        queue = [(self.start,None)]
        while len(queue)>0:
            current,parent = queue.pop(0)

            if self.isTarget(current):
                self.visited[current] = parent
                break

            elif current in self.visited:
                continue

            else:
                self.visited[current] = parent
                successors = self.getSuccessors(current) #adding successors list to the back
                for successor in successors:
                    queue.append((successor,current))

        while parent is not None:
            self.path.append(parent)
            parent = self.visited[parent]

        self.path.pop() # pops the start node to keep it red

    def colorPath(self):
        '''
        Colors all path nodes blue
        '''
        for node in self.path:
            self.solution[node] = [0,0,1]

    def SolveMaze(self):
        '''
        Prints the solution as image
        '''
        self.findShortestPath()
        self.colorPath()
