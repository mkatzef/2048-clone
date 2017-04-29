import twenty48
from tkinter import *
from tkinter.ttk import *
import math

class Twenty48gui:
    def __init__(self, window):
        self.window = window
        self.board_var = StringVar()
        self.size = 4
        self.base_var = StringVar()
        self.base_var.set('2')
        self.size_var = StringVar()
        self.size_var.set('4')
        self.board_size = int(self.size_var.get())
        self.last_board_size = 0
        self.status = 0
        self.colours = [('EEE4DA', '000000'), ('EDE0C8', '000000'), \
                        ('F2B179', 'FFFFFF'), ('F59563', 'FFFFFF'), \
                        ('F67C5F', 'FFFFFF'), ('F65E3B', 'FFFFFF'), \
                        ('EDCF72', 'FFFFFF'), ('EDCC61', 'FFFFFF'), \
                        ('EDCC61', 'FFFFFF'), ('EDCC61', 'FFFFFF'), \
                        ('EDCC61', 'FFFFFF')] #Gets to 256 with unique colours, then sticks there till 2048, then repeats
        
        
        
        self.board_frame = Frame(window)
        self.board_frame.grid(row=2, column=0, columnspan=4)
        
        self.place_board(self.board_frame)
        
        help_label = Label(window, text='Use arrow keys to move the tiles.')
        help_label.grid(row=3, column=0, columnspan=4, pady=10)
        
        parameter_row = Frame(window)
                
        size_label = Label(parameter_row, text='Size:')
        size_label.grid(row=1, column=0)
        
        size_entry = Entry(parameter_row, textvariable=self.size_var, width=5)
        size_entry.grid(row=1, column=1)
        
        base_label = Label(parameter_row, text='Base:')
        base_label.grid(row=1, column=2)
        
        base_entry = Entry(parameter_row, textvariable=self.base_var, width=5)
        base_entry.grid(row=1, column=3)
        self.base_var.trace('w', self.rewrite_title)
        
        parameter_row.grid(row=4, column=0, columnspan=4)        
    
        self.new_button = Button(window, text='New Game', command=self.start_new)
        self.new_button.grid(row=5, column=0, columnspan=4, pady=10)

        window.bind('<Right>', lambda event: self.move('right'))
        window.bind('<Left>', lambda event: self.move('left'))
        window.bind('<Up>', lambda event: self.move('up'))
        window.bind('<Down>', lambda event: self.move('down'))
        self.start_new()
        
    
    def rewrite_title(self, *args):
        current_base = self.base_var.get()
        if current_base.isdigit():
            new_value = int(current_base) ** 11          
            self.window.title(str(new_value))            

    
    def place_board(self, window):
        board_size = int(self.size_var.get())
        template = 'self.label{0}.destroy()'
        for i in range(self.last_board_size ** 2):
            exec(template.format(i))
            
        window['height'] = board_size * 80
        window['width'] = board_size * 80


        template = """self.lab_var{0} = StringVar()
self.label{0} = Label(window, textvariable=self.lab_var{0}, font=('Arial', 16, 'bold'))
self.label{0}.place(relx={1}, rely={2}, anchor='center')"""            
        for i in range(board_size ** 2):
            column = i // board_size
            row = i % board_size
            
            exec(template.format(i, (row+1)/(board_size+1), (column+1)/(board_size+1)))
                
                
        
    def start_new(self):
        self.new_button['text'] = 'New Game'
        self.last_board_size = self.board_size
        self.board_size = int(self.size_var.get())
        base = int(self.base_var.get())
        self.place_board(self.board_frame)
        self.game = twenty48.twenty48(self.board_size, base)
        self.game.put_rand()
        self.refresh_board()
        self.status = 1
    
    
    def refresh_board(self):
        board = self.game.get_board()
        
        template = """self.lab_var{0}.set({1})"""
        for i in range(len(board)):
            exec(template.format(i, str(board[i])))
            
            value = eval('board[{}]'.format(i))
            if value == 0:
                colour_index = 0
            else:
                colour_index = max(0, -1 + int(math.log(value) / math.log(int(self.base_var.get())))) % len(self.colours)
            
            colour = self.colours[colour_index]
            bg_colour = colour[0]
            fg_colour = colour[1]
            
            exec("self.label{0}['background'] = '#{1:s}'".format(i, bg_colour))
            exec("self.label{0}['foreground'] = '#{1:s}'".format(i, fg_colour))            
    
    
    def move(self, direction):
        if self.check():
            copy1 = self.game.get_board()
            exec('self.game.{}()'.format(direction))
            copy2 = self.game.get_board()
            if copy1 != copy2:
                self.game.put_rand()
                self.refresh_board()                
        
        
    def check(self):
        still_ok = True
        self.game.check()
        if self.game.status == 0:
            self.new_button['text'] = 'Play Again'
            still_ok = False   
            
        return still_ok
    
    
def main():
    window = Tk()
    window.title('2048')
    window.resizable(width=False, height=False)
    Twenty48gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
        