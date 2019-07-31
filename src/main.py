from src.Go.gui.gui import GUI
from src.Chess.Game import Game
def main():
    print("输入 1 进行围棋，输入 2 进行国际象棋")
    choice = input("输入你的选择：")
    if choice =! 1:
        Game()

    else :
        GUI = GUI()
        while True:
            GUI.handle_events()
            GUI.draw()
if __name__ == '__main__':
    main()
