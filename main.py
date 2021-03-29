from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

def generateBoard():
    boards = []
    selects = []
    gos = []

    board0 = [["--", "wQ", "--", "--", "--", "--", "bR", "--"],
              ["--", "bp", "--", "bK", "--", "bQ", "bp", "--"],
              ["bp", "--", "bB", "wB", "--", "--", "--", "bp"],
              ["wp", "--", "--", "bp", "wp", "bp", "--", "--"],
              ["--", "wp", "--", "--", "--", "--", "--", "--"],
              ["--", "--", "--", "--", "--", "--", "wR", "wp"],
              ["--", "--", "--", "--", "--", "--", "wp", "--"],
              ["--", "--", "--", "--", "--", "--", "wK", "--"]]
    boards.append(board0);
    selects.append(2)
    gos.append(11)

    board1 = [["--", "bR", "--", "--", "bR", "--", "bK", "--"],
              ["--", "--", "bQ", "--", "bB", "--", "bp", "--"],
              ["bp", "--", "--", "--", "--", "--", "bp", "--"],
              ["--", "--", "--", "--", "bp", "bB", "--", "wp"],
              ["--", "bN", "--", "--", "--", "--", "--", "--"],
              ["--", "wN", "wN", "--", "--", "--", "--", "wB"],
              ["--", "wp", "wp", "--", "wQ", "--", "--", "--"],
              ["--", "wK", "--", "wR", "--", "--", "--", "wR"]]
    boards.append(board1);
    selects.append(32)
    gos.append(23)

    board2 = [["--", "--", "--", "--", "--", "bR", "--", "--"],
              ["--", "bp", "bQ", "--", "bK", "--", "bB", "--"],
              ["--", "--", "--", "wR", "bp", "--", "--", "bp"],
              ["--", "wB", "bp", "--", "--", "--", "bp", "--"],
              ["wp", "--", "bN", "--", "wp", "--", "--", "--"],
              ["--", "--", "wp", "--", "--", "--", "--", "--"],
              ["--", "wp", "--", "--", "wQ", "--", "wp", "wp"],
              ["--", "--", "--", "--", "--", "--", "wK", "--"]]
    boards.append(board2);
    selects.append(20)
    gos.append(12)

    randNum = random.randint(0, len(boards)-1)
    selectBoard = boards[randNum]
    selectSelect = selects[randNum]
    selectGo = gos[randNum]

    boardString =  ""
    for i in range(len(selectBoard)):
        for j in range(len(selectBoard[i])):
            boardString += selectBoard[i][j] + " "
        boardString += "|"

    return (boardString, selectSelect, selectGo)

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/game',methods = ['POST', 'GET'])
def game():
    tuple = generateBoard()
    board = tuple[0]
    select = tuple[1]
    go = tuple[2]
    return render_template("game.html", board=board, select=select, go=go)

if __name__ == "__main__":
    app.run(debug=True)