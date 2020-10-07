
import heapq
from copy import deepcopy
import numpy as np

#possible successor states
def succ(state):
    state_copy = deepcopy(state)
    state_copy = np.array([state_copy])
    state_copy = state_copy.reshape(3,3)
    
    final_arr = [] 
    # final_arr.append(state)
    
    goal = np.array([1,2,3,4,5,6,7,8,0])
    goal = goal.reshape(3,3)
    
    state2 = deepcopy(state)
    state2 = np.array([state2])
    state2 = state2.reshape(3,3)
    
    state3 = deepcopy(state)
    state3 = np.array([state3])
    state3 = state3.reshape(3,3)
    
    state4 = deepcopy(state)
    state4 = np.array([state4])
    state4 = state4.reshape(3,3)
    
    state5 = deepcopy(state)
    state5 = np.array([state5])
    state5 = state5.reshape(3,3)
    
    zero_x = 0
    zero_y = 0
    
    #get the index of the 0 tile
    for i in range(3):
        for j in range(3):
            if(state_copy[i][j] == 0):
                zero_x = i
                zero_y = j

    #figure out the next move
    #if the tile below 0 is misplaced
    if(zero_x + 1 < 3 and state2[zero_x+1][zero_y] != 'null'):
       state2[zero_x][zero_y] = state2[zero_x+1][zero_y]
       state2[zero_x+1][zero_y] = 0
       add_arr = state2.flatten()
       final_arr.append(add_arr)
    #if the tile right of 0 is misplace
    if(zero_y + 1 < 3 and state3[zero_x][zero_y+1] != 'null'):
        # print("here")
        state3[zero_x][zero_y] = state3[zero_x][zero_y+1]
        state3[zero_x][zero_y+1] = 0
        add_arr = state3.flatten()
        final_arr.append(add_arr)
    if(zero_x - 1 >= 0 and state4[zero_x-1][zero_y] != 'null'):     
        state4[zero_x][zero_y] = state4[zero_x-1][zero_y]
        state4[zero_x-1][zero_y] = 0
        add_arr = state4.flatten()
        final_arr.append(add_arr)      
    if(zero_y-1 >= 0 and state5[zero_x][zero_y-1] != 'null'):     
        state5[zero_x][zero_y] = state5[zero_x][zero_y-1]
        state5[zero_x][zero_y-1] = 0
        add_arr = state5.flatten()
        final_arr.append(add_arr)

    return final_arr

def h(state):
    #deepcopy the state and turn it 2d
    state2 = deepcopy(state)
    state2 = np.array([state2])
    state2 = state2.reshape(3,3)
    distance = 0
    for i in range(len(state2)):
        for j in range(len(state2[i])):
            if(state2[i][j] == 0):
                continue
            else:
                #compare the current index to the 8 possibilities
                if(state2[i][j] == 1):
                    goal = [0,0]
                elif(state2[i][j] == 2):
                    goal = [0,1]
                elif(state2[i][j] == 3): 
                    goal = [0,2]
                elif(state2[i][j] == 4): 
                    goal = [1,0]
                elif(state2[i][j] == 5):
                    goal = [1,1]
                elif(state2[i][j] == 6): 
                    goal = [1,2]
                elif(state2[i][j] == 7):
                    goal = [2,0]
                elif(state2[i][j] == 8): 
                    goal = [2,1]
                elif(state2[i][j] == 9):
                    goal = [2,2]
                    
                add = manhattan([i,j], goal )
                distance = distance + add
    return distance

def manhattan(at, goal):
    x1 = at[0]
    y1 = at[1]
    x2 = goal[0]
    y2 = goal[1]
    dist = abs(x1-x2) + abs(y1-y2)
    return dist

# h = sum of mandist of each tile to its goal position
def print_succ(input_state):
    # print 'print_succ called'
    states = succ(input_state)
    for i in range(len(states)):
        states[i] = list(states[i])
    states = list(states)
    states = sorted(states)
    # print succ_states
    for i in range(len(states)):
        print(states[i], ' h=', h(states[i]))

#find the f score
# def f(state):
    # 

# #enqueue the successors
# def astar(state, openq, parents):
#     low_h = 0
#     hs = []
#     #find the successors for the current state
#     states = succ(state)
#     for i in range(len(states)):
#         states[i] = list(states[i])
#     states = list(states)
#     states = sorted(states)
    
#     # push successors to the openq
#     for i in range(len(states)):
#        hs.append( h(states[i]) )
#        heapq.heappush( openq, (hs[i], states[i], (0, hs[i], 0)) )
     
#     print(openq)
#     low_h = min(hs)
#     return low_h
    
#extract only the state 
# def get_state (heapq):
    
#     state = heapq[i][1]    
#     # print(state)
#     return state

#given a state of the puzzle, perform the A* search algorithm 
#and print the path from the current state to the goal state
# (g+h, state, (g,h,parent_index))
# g = total moves so far
def solve(state):
    parents = []
    parent = 0
    path= []
    #goal array 
    goal = np.array([1,2,3,4,5,6,7,8,0])
    goal = goal.reshape(3,3)
    #nodes that still need to be explored
    openq = []
    #nodes that don't need to be explored- but can pop off the last one as the parent for the openq
    closeq = []
    f = 0
  
    state_copy = deepcopy(state)
    curr = state_copy
    curr = np.array([curr])
    curr = curr.reshape(3,3)
    #1st push is the original state with no parent
    
    h_score = h(state_copy)
    # print(h_score)
    g = 0
    b = []
    heapq.heappush( closeq, (h_score, state_copy, (0, h_score, -1)) )
    heapq.heappush( b, (h_score, state_copy, (0, h_score, -1)) )

    # print(closeq[0][1])
    
    # b = heapq.heappop(openq)
    # b = [state_copy, h_score, g]
    # path.append(b)
    # print(path)
    #moves    
   
    f = 0
    states = succ(curr)
    # print(states)
    #run this loop till the final is achieved // fixme
    # while not(np.array_equal(curr, goal)):
    for i in range(100):
        #add to openq
        for i in range(len(states)):
            h_score = h(states[i])
            print("HSCORE", h_score)
            heapq.heappush( openq, (h_score + g, states[i], (g, h_score, parent)) )
        b = heapq.heappop(openq)  
        heapq.heappush(closeq, b)
        print(closeq)
        # heapq.heappush(closeq, b)
        parent += 1 #needed????
        g += 1
    # print(path)
        print(len(openq))
        states = openq[i][1]
   
    
    # for i in range(len(closeq)):
    #    # print(closeq[i][1], ' h=', closeq[i][2[1]], 'g=', closeq[i][2[0]])
    #    for j in i:
    #        for k in j:
    #            print()
        
        
    
    



