#integer	מספר שלם
#float	מספר עשרוני
#string	מחרוזת (טקסט)	"hello world"
#boolean	ערך בוליאני אמת או שקר	True
#None	הדרך של פייתון לייצג כלום
#הערך שחוזר מהפונקציה input לעולם יהיה מחרוזת!

player_name = input('Hello, please insert your name')
board_size = int(input(f'Hello {player_name}, please enter the board size you will want'))
number_of_mines = int(input(f'For a board size {board_size}, choose how many mines you want'))

print(f'Ok {player_name}, you chose a board size {board_size}, with {number_of_mines} mines, have fun')
