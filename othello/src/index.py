from ui.tempui import TempUI
from board import Board


def main():
    board = Board()
    tempui = TempUI(board)

    tempui.start()


if __name__ == "__main__":
    main()
