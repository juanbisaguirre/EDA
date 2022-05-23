from re import template



class Peon():
        def __init__(self,row, col, board, team):
            self.table = board
            self.team = team
            self.row = row
            self.col = col
            self.location = [row, col]
            self.direction = ' '
            self.mymoves =[]
            self.set_direction()
            self.foward()
            self.left_right()
            

        def set_direction(self):     #this is my direction
            if  'N' == self.team:
                self.direction = 1
            else:
                self.direction = -1

        def foward(self):                       #utilizamos la distancia para averiguar la posicion de la fila.
            distance = self.direction*2
        
            new_row = self.row + distance
            new_col = self.col

            new_coordinates = [new_row, new_col]
    
            foward_movement = [self.location, new_coordinates]

            self.mymoves.append(foward_movement)
            
          
        
        def left_right(self):
            distance = self.direction*2
        
            new_row = self.row
            new_col = self.col + distance

            new_coordinates = [new_row, new_col]
    
            left_movement = [self.location, new_coordinates]

            self.mymoves.append(left_movement)
                                       

