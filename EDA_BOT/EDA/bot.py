from peon import Peon
import random
class Botito():

    def __init__(self,data):
        self.player_1 = data["player_1"]
        self.player_2 = data['player_2']
        self.walls = data['walls']
        self.remaining_moves = data['remaining_moves']
        self.score_1 = data['score_1']
        self.score_2 = data['score_2']
        self.side = data['side']
        self.turn_token = data['turn_token']
        self.game_id = data['game_id']
        self.board  = data ['board']
        self.matriz = ''
        self.pawn = []
        self.movements = []
        self.bestmove=''


    def showTable (self):
        tabledolist = list(self.board)
        matriz = [tabledolist[i:i+17] for i in range(0, len(tabledolist), 17)]#crea una matriz con el string
        for row in matriz:

            print(row)
    
        self.matriz = matriz    

    def lookingforpawn (self): # i es la columna y x es la fila 
        for i, row in enumerate(self.matriz):
            for x, pieza in enumerate(row):
                if  self.side == pieza:
                    print('hola peonsito')
                    print (i , x)
                    peonsito = Peon(x, i,self.matriz, self.side)
                    self.pawn.append(peonsito)

    def extraer_movimientos(self):
        for pawn in self.pawn:
            pawnmoves = pawn.mymoves
            self.movements.append(pawnmoves)

    def choosemoves(self): # tengo una lista de movimmientos posibles y elije uno random.
       
        
        bestmove = random.choice(self.movements)
        move = bestmove[0]
        origin = move[0]
        destiny = move[1]

        action = 'move'
        data = {'game_id': self.game_id, 'turn_token':self.turn_token, 'from_row': origin[0]/2, 'from_col': origin[1]/2, 'to_row': destiny[0]/2, 'to_col': destiny[1]/2}
        respuesta = {'action': action, 'data': data}

        self.bestmove = respuesta
        print(move)







if __name__== "__main__":
    data = {
        "board": '                   -- -- -- --  S       S   S                                 N                                                                                                                                                                   N   N          -- -- -*-                       ',
        "walls": 10.0,
	    "player_2": "ja.bisaguirrelivellara@gmail.com",
	    "remaining_moves": 195.0,
	    "score_2": -20.0,
	    "player_1": "levite@gmail.com",
	    "score_1": 9.0,
	    "side": "N",
	    "turn_token": "d54c5620-ba0d-4703-8858-bcf1146eadb2",
	    "game_id": "a27c7f1e-cd8c-11ec-aef0-7ecdf393f9cc"}

    botito = Botito(data)
    botito.showTable()
    botito.lookingforpawn()
    botito.extraer_movimientos()
    botito.choosemoves()
