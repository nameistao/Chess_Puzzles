from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

def generateBoard():
    boards = []

    board0 = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
              ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
              ["--", "--", "--", "--", "--", "--", "--", "--"],
              ["--", "--", "--", "--", "--", "--", "--", "--"],
              ["--", "--", "--", "--", "--", "--", "--", "--"],
              ["--", "--", "--", "--", "--", "--", "--", "--"],
              ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
              ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
    boards.append(board0);

    selectBoard = boards[random.randint(0,len(boards)-1)]

    boardString =  ""
    for i in range(len(selectBoard)):
        for j in range(len(selectBoard[i])):
            boardString += selectBoard[i][j] + " "
        boardString += "|"

    return boardString

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/game',methods = ['POST', 'GET'])
def game():
    return render_template("game.html", board=generateBoard())

if __name__ == "__main__":
    app.run(debug=True)