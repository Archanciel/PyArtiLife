class World:
    def __init__(self, size_x, size_y):
        '''
        Initializes a World with a size_x x size_y matrix initialized with 0's
        (dead cells).
        '''
        self.lines = size_x
        self.cols = size_y
        self.matrix = [['.' for _ in range(self.lines)] for _ in range(self.cols)]

    def seed(self, liveCellList):
        '''
        Seeds the World with a list of live cells. liveCellList contains a list
        of 2 dimensional tuples denoting the 1 based li-co coordinates of each
        seeded live cell.
        '''
        for cell in liveCellList:
            self.matrix[cell[0] - 1][cell[1] - 1] = 'o'
            
    def displayWorld(self):
        '''
        Prints a representation of the World matrix
        '''
        self._printXAxis()
        
        l = 0
        line_nb = l
        
        for li in self.matrix:
            if l > 0 and l % 10 == 0:
                tenth = str(int(l / 10))
            else:
                tenth = " "
            if l < 9:
                line_nb = tenth + str(l % 9 + 1)
            elif l == 9:
                l += 1
                line_nb = tenth + "0"
            else:
                line_nb = tenth + str(l % 10)
            print("{}".format(line_nb), end='')
            self._printLine(li)
            l += 1

    def _printXAxis(self):
        for i in range(1, int(self.cols / 10) + 1):
            if i == 1:
                print("                    {}".format(i), end='')
            else:
                print("                   {}".format(i), end='')
            
        print()
        print("  ", end='')
        
        for j in range(self.lines):
            if j < 9:
                j = j % 9 + 1
            elif j == 9:
                continue
            else:
                j = j % 10
            print("{} ".format(j), end='')
            
        print("0")
            
    def _printLine(self, line):
        for cell in line:
            print("{} ".format(cell), end='')
            
        print()


w = World(40, 40)
w.seed([(5,5), (5,6)])
w.displayWorld()