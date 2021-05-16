from gameEntry import GameEntry
from scoreboard import Scoreboard


def main():
    BOARD = Scoreboard(5)
    firstEntry = GameEntry('Jon', 98)
    BOARD.add(firstEntry)
    entry = GameEntry('Mag', 95)
    BOARD.add(entry)
    entry = GameEntry('App', 92)
    BOARD.add(entry)
    entry = GameEntry('Lie', 94)
    BOARD.add(entry)
    entry = GameEntry('Messi', 50)
    BOARD.add(entry)
    print(BOARD)
    entry = GameEntry('Neymar', 99)
    BOARD.add(entry)
    print(BOARD)

if __name__ == '__main__':
    main()
