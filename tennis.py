import random
from points_matrix import pm

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
sl_points = [[]]
sl_games = [[]]
sl_sets = []

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

        # grow log array
        sl_points[i_set-1].append([])
        
        # play one game
        while "W" not in s_points:
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
            sl_points[i_set-1][i_game-1].append(s_points.copy())

            #print("point to " + winner + ": ", points_score)
            i_point += 1

        # reset 
        i_point = 1
        csi = [0,0]

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

        # log games score
        sl_games[i_set-1].append(s_games.copy())

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

            # log set score
            sl_sets.append(s_sets.copy())

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

            # log arrays increase size
            sl_points.append([[]])
            sl_games.append([])

            continue


# print results
m_winner = players[s_sets.index(max(s_sets))]
print("match to ", m_winner)
print("set score ", s_sets)
pass