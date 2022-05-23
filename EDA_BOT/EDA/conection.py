
import websockets,asyncio,json,time,sys
from random import randint

from bot import Botito
#import the board

 
 
 
async def start_the_connection(url):
 
    while True:
        try:
            async with websockets.connect(url) as ws:
            
                await check_the_data_received(ws)
 
        except Exception as e:
            print(f"connection error: {e}")
 
 
async def check_the_data_received(ws):
        while True:
            my_answer = ""
           
            try:
 
              
                print("waiting")
                request = await ws.recv()
                print("something came!")
 
              
                request_data =json.loads(request)
          
 
 
                #logic for acept a challenge
                if request_data['event'] == 'challenge':
                    my_answer = {
                                        'action': 'accept_challenge',
                                        'data': {
                                                'challenge_id': request_data['data']['challenge_id'] 
                                        }
                    }
                    await send_data(ws,my_answer)
 
                elif request_data['event'] == 'list_users':
                    print(f"users connected:::{request_data['data']['users']}:::")
 
 
                #logic for make a movement 
                elif request_data['event'] == 'your_turn':
                   
                    botito = Botito(request_data['data'])
                    botito.showTable()
                    botito.lookingforpawn()
                    botito.extraer_movimientos()
                    botito.choosemoves()
                    best = botito.bestmove
                    
                    # board= Board(request_data['data'])
                    # board.create_board()
                    # board.get_pawns()
                    # board.pool_all_posible_movements()
                    # board.choose_move()
                    # my_answer = board.make_movement()
                    print(f"BOARD :'{request_data['data']['board']}'")
                    await send_data(ws,best)
 
                  
                   
 
 
 
                elif request_data['event'] == 'game_over':
                    print(f"game over,ID: {request_data['data']['game_id']}")
                    pass
 
                elif request_data['event'] == 'update_user_list':
                    print(f"update:::{request_data['data']}:::")
                    pass
 
                #put this to see if there is any other data that i am receiving
                else:
                    print(request_data)
                    pass
 
 
 
            except Exception as e:
 
                print(f"Exception Fired:   {e}")
                print(f"BOARD :'{request_data['data']['board']}'")
                break
 
             
           
 
 
    #logic where i send the data to the server, where i accept a challenge or make a movement     
async def send_data(ws,my_answer):
 
        answer = json.dumps(
            {
                'action': my_answer['action'],
                'data': my_answer['data'],
 
        })
        print(f"what i send: {answer}")
        await ws.send(answer)
        my_answer = {}
 
 
 
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        auth_token = sys.argv[1]
        url= "wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token=" + auth_token
        asyncio.get_event_loop().run_until_complete(start_the_connection(url))
    else:
        print('please provide your auth_token')