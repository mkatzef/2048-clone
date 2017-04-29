import random

class twenty48():
    def __init__(self, size, base):
        self.size = size
        self.base = base
        self.rows = [[0]*size for i in range(size)]
        self.status = 1
        self.highest = 0
        self.maxwidth = 0
        #self.gameloop()
        
        
    def right(self):
        for i in range(self.size):
            self.rows[i] = self.squish_right(self.rows[i])
    
    
    def left(self):
        for i in range(self.size):
            self.rows[i] = list(reversed(self.squish_right(list(reversed(self.rows[i])))))
    
    
    def down(self):
        columns = rotate(self.rows)
        for i in range(self.size):
            columns[i] = self.squish_right(columns[i])
        self.rows = rotate(columns)
    
    
    def up(self):
        columns = rotate(self.rows)
        for i in range(self.size):
            columns[i] = list(reversed(self.squish_right(list(reversed(columns[i])))))
        self.rows = rotate(columns)
    
    
    def put_rand(self):
        empties, slots = self.check()
        if self.status == 1:
            which_slot = random.randint(0, empties-1)
            slot = slots[which_slot]
            row = slot[0]
            column = slot[1]
            
            place_val = self.base ** random.randint(1,2)
            self.rows[row][column] = place_val


    def check(self):
        empties = 0
        slots = []
        for i in range(self.size):
            for j in range(self.size):
                if self.rows[i][j] == 0:
                    empties += 1
                    slots.append((i,j))
        
        if empties == 0:
            row_copy = deepcopy(self.rows)
            moves = ['right', 'left', 'up', 'down']
            
            nomoves = True
            for direction in moves:
                self.rows = deepcopy(row_copy)
                exec('self.{0}()'.format(direction))
                if self.rows != row_copy:
                    nomoves = False
                    self.rows = row_copy
                    break
            if nomoves:
                self.status = 0
                
        return empties, slots
    
    
    def get_board(self):
        row_list = []
        for row in self.rows:
            row_list += row
        return row_list
    
    
    #def gameloop(self):
        #self.put_rand()
        #self.printboard()
        
        #while self.status == 1:
            #move = input('\nMove: ')
            #old = deepcopy(self.rows)
            #letter = move[0].lower()
            #if letter == 'u':
                #self.up()
            #elif letter == 'd':
                #self.down()
            #elif letter == 'l':
                #self.left()
            #elif letter == 'r':
                #self.right()
            #else:
                #continue
            
            #self.check()
            #if not comp(old, self.rows):
                #self.put_rand()
            
        #print('You done goofed')
        

    def squish_right(self, row):
        length = len(row)
        pos = -1
        while abs(pos) < length:
            previous_list = row[:pos]
            previous = 0        
        
            while len(previous_list) > 0 and previous == 0:
                previous = previous_list.pop()
        
            if previous == row[pos]:
                row[pos] *= self.base
                if row[pos] > self.highest:
                    self.highest = row[pos]
                    self.maxwidth = len('{:.0f}'.format(self.highest))
                row[pos - 1] = -1
                pos = -(self.size - len(previous_list))
            else:
                pos -= 1

        ret_row = [value for value in row if value not in [-1, 0]]
        return [0] * (length - len(ret_row)) + ret_row


def deepcopy(array):
    ret = []
    for row in array:
        ret.append(row[:])
    return ret


def comp(a1, a2):
    if len(a1) != len(a2):
        return False
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            return False
    return True
    
    
def rotate(array):
    size = len(array)
    columns = []
    for i in range(size):
        cur_col = []
        for j in range(size):
            cur_col.append(array[j][i])
        columns.append(cur_col)
    return columns

