import socket
from _thread import *
from chess.CHESS.chessboard import chessBoard
from chess.CHESS.chessconstants import WHITE, BLACK
import pickle
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "localhost"
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen()
print("[START] Waiting for a connection")

connections = 0

games = {0: chessBoard(8, 8)}

spectartor_ids = []
specs = 0


def read_specs():
    global spectartor_ids

    spectartor_ids = []
    try:
        with open("specs.txt", "r") as f:
            for line in f:
                spectartor_ids.append(line.strip())
    except:
        print("[ERROR] No specs.txt file found, creating one...")
        open("specs.txt", "w")


def threaded_client(conn, game, spec=False):
    global pos, games, currentId, connections, specs

    if not spec:
        name = None
        play = games[game]

        if connections % 2 == 0:
            currentId = WHITE
        else:
            currentId = BLACK

        play.start_user = currentId

        # Pickle the object and send it to the server
        data_string = pickle.dumps(play)

        if currentId == BLACK:
            play.ready = True
            play.startTime = time.time()

        conn.send(data_string)
        connections += 1

        while True:
            if game not in games:
                break

            try:
                d = conn.recv(8192 * 3)
                data = d.decode("utf-8")
                if not d:
                    break
                else:
                    if data.count("select") > 0:
                        all = data.split(" ")
                        col = int(all[1])
                        row = int(all[2])
                        color = all[3]
                        play.select(col, row, color)

                    if data == "winner b":
                        play.winner = BLACK
                        print("[GAME] Player b won in game", game)
                    if data == "winner w":
                        play.winner = WHITE
                        print("[GAME] Player w won in game", game)

                    if data == "update moves":
                        play.update_moves()

                    if data.count("name") == 1:
                        name = data.split(" ")[1]
                        if currentId == BLACK:
                            play.p2Name = name
                        elif currentId == WHITE:
                            BLACK.p1Name = name

                    # print("Recieved board from", currentId, "in game", game)

                    if play.ready:
                        if play.turn == WHITE:
                            play.time1 = 900 - (time.time() - play.startTime) - play.storedTime1
                        else:
                            play.time2 = 900 - (time.time() - play.startTime) - play.storedTime2

                    sendData = pickle.dumps(play)
                    # print("Sending board to player", currentId, "in game", game)

                conn.sendall(sendData)

            except Exception as e:
                print(e)

        connections -= 1
        try:
            del games[game]
            print("[GAME] Game", game, "ended")
        except:
            pass
        print("[DISCONNECT] Player", name, "left game", game)
        conn.close()

    else:
        available_games = list(games.keys())
        game_ind = 0
        play = games[available_games[game_ind]]
        play.start_user = "s"
        data_string = pickle.dumps(play)
        conn.send(data_string)

        while True:
            available_games = list(games.keys())
            play = games[available_games[game_ind]]
            try:
                d = conn.recv(128)
                data = d.decode("utf-8")
                if not d:
                    break
                else:
                    try:
                        if data == "forward":
                            print("[SPECTATOR] Moved Games forward")
                            game_ind += 1
                            if game_ind >= len(available_games):
                                game_ind = 0
                        elif data == "back":
                            print("[SPECTATOR] Moved Games back")
                            game_ind -= 1
                            if game_ind < 0:
                                game_ind = len(available_games) - 1

                        play = games[available_games[game_ind]]
                    except:
                        print("[ERROR] Invalid Game Recieved from Spectator")

                    sendData = pickle.dumps(play)
                    conn.sendall(sendData)

            except Exception as e:
                print(e)

        print("[DISCONNECT] Spectator left game", game)
        specs -= 1
        conn.close()


while True:
    read_specs()
    if connections < 6:
        conn, addr = s.accept()
        spec = False
        g = -1
        print("[CONNECT] New connection")

        for game in games.keys():
            if games[game].ready == False:
                g = game

        if g == -1:
            try:
                g = list(games.keys())[-1] + 1
                games[g] = chessBoard(8, 8)
            except:
                g = 0
                games[g] = chessBoard(8, 8)

        '''if addr[0] in spectartor_ids and specs == 0:
            spec = True
            print("[SPECTATOR DATA] Games to view: ")
            print("[SPECTATOR DATA]", games.keys())
            g = 0
            specs += 1'''

        print("[DATA] Number of Connections:", connections + 1)
        print("[DATA] Number of Games:", len(games))

        start_new_thread(threaded_client, (conn, g, spec))