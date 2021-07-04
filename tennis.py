import random

# initialise possible score journey array
pm = [
        [
            [  0,0],
            [  0,15],
            [  0,30],
            [  0,40],
            [ 0,"W"]],
        [
            [ 15,0],
            [ 15,15],
            [ 15,30],
            [ 15,40],
            [15,"W"]],
        [
            [ 30,0],
            [ 30,15],
            [ 30,30],
            [ 30,40],
            [30,"W"]],
        [
            [ 40,0],
            [ 40,15],
            [ 40,30],
            [ 40,40],
            [40,"A"],
            [40,"W"]],
        [
            ["W",0],
            ["W",15],
            ["W",30],
            ["A",40]],
        [
            0,
            0,
            0,
            ["W",40]]
    ]

# current score index
csi = [0,0]
points_score = pm[csi[0]][csi[1]]
games_score = [0,0]
set_score = [0,0]

# initialise players list
players = ["M. Berrettini", "G. Pella"]
print(players[0] + " vs " + players[1])

# coin toss
server = random.choice(players)
server_index = players.index(server)
print (server + " to serve")
sr = [players[server_index],players[1-server_index]]

set_i = 1
game_i = 1
point_i = 1

#initialise score log
points_score_log = [[[points_score]]]
games_score_log = [[games_score]]

# play a set
while True:
    # play a game
    while True:
        # simulate a 50/50 single point
        winner = random.choice(players)
        winner_index = players.index(winner)

        # move in score array
        if points_score == ["A",40] and winner_index != server_index:
            csi=[3,3]
        elif points_score == [40,"A"] and winner_index == server_index:
            csi=[3,3]
        elif winner_index == server_index:
            csi[0]+=1
        elif winner_index != server_index:
            csi[1]+=1

        # get + log new score
        points_score = pm[csi[0]][csi[1]]
        points_score_log[set_i-1][game_i-1].append(points_score)

        #print("point to " + winner + ": ", points_score)

        point_i += 1

        if str(points_score[0]) == "W" or str(points_score[1]) == "W":
            point_i == 1
            csi = [0,0]
            break

    # who won that game
    print(points_score)
    game_winner = sr[points_score.index("W")]
    print ("set ", set_i, ", game ", game_i, " goes to ", game_winner, ":", points_score)

    # games score
    if game_winner == players[0]:
        games_score[0] += 1
    elif game_winner == players[1]:
        games_score[1] += 1

    print(games_score)
    input("Press Enter to continue...")

    if games_score[0] == games_score[1] == 6:
        print("Tiebreak to 7")
    elif (games_score[0] == 6 and games_score[1] <= 4) or (games_score[1] == 6 and games_score[0] <= 4):
        games_score = [0,0]
        break


#print(games_score)
#print(points_score_log)