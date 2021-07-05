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
s_points = pm[csi[0]][csi[1]]
s_games = [0,0]
s_sets = [0,0]

# initialise players list
players = ["M. Berrettini", "G. Pella"]
#print(players[0] + " vs " + players[1])

# coin toss
server = random.choice(players)
server_index = players.index(server)
#print (server + " to serve")
sr = [players[server_index],players[1-server_index]]

i_set = 1
i_game = 1
i_point = 1

#initialise score log
sl_points = [[[s_points]]]
sl_games = [[s_games]]
sl_sets = [s_sets]

# false match over
match_over = False

# play a match
while True:

    if match_over == True:
            break
    
    # play a set of games
    while True:

        if match_over == True:
            break
        
        # play one game
        while True:
            # simulate a 50/50 single point
            winner = random.choice(players)
            winner_index = players.index(winner)

            # move in score array
            if (s_points == ["A",40] and winner_index != server_index) or (s_points == [40,"A"] and winner_index == server_index):
                csi=[3,3]
            elif winner_index == server_index:
                csi[0]+=1
            elif winner_index != server_index:
                csi[1]+=1

            # get + log new score
            s_points = pm[csi[0]][csi[1]]
            sl_points[i_set-1][i_game-1].append(s_points)

            #print("point to " + winner + ": ", points_score)
            i_point += 1

            if str(s_points[0]) == "W" or str(s_points[1]) == "W":
                # reset 
                i_point = 1
                csi = [0,0]
                break

        # grow log array
        sl_points[i_set-1].append([[0,0]])

        # who won that game
        game_winner = sr[s_points.index("W")]
        #print ("set ", set_i, ", game ", game_i, " goes to ", game_winner, ":", points_score)

        # iterate game
        i_game += 1

        # swap servers
        sr.reverse()

        # games score
        if game_winner == players[0]:
            s_games[0] += 1
        elif game_winner == players[1]:
            s_games[1] += 1

        # end of set check
        if s_games[0] == s_games[1] == 6:
            # tiebreak
            if s_sets==[2,2]:
                # 5th set tie break
                #print("Tiebreak to 10")
                pass
            else:
                # regular set tiebreak
                #print("Tiebreak to 7")
                pass
            break
        elif (s_games[0] >= 6 and s_games[1] <= 5) or (s_games[1] >= 6 and s_games[0] <= 5):
            set_winner = players[s_games.index(max(s_games))]
            s_games = [0,0]
            #print("set to " + set_winner)
            
            # add score to sets
            if set_winner == players[0]:
                s_sets[0] += 1
            elif set_winner == players[1]:
                s_sets[1] += 1
            #print("match score in sets: ",set_score)

            # log arrays increase size
            sl_points.append([[]])

            # increment set
            i_set += 1
            i_game = 1

            # at the end of a set check for the end of match
            if s_sets == [3,0] or s_sets == [0,3]:
                match_over = True
                break
            elif s_sets == [3,1] or s_sets == [1,3]:
                match_over = True
                break
            elif s_sets == [3,2] or s_sets == [2,3]:
                match_over = True
                break

            continue

        #print("games score in this set ", games_score)
        #input("Press Enter to continue...")

# print results
m_winner = players[s_sets.index(max(s_sets))]
print("match to ", m_winner)
print("set score ", s_sets)
pass