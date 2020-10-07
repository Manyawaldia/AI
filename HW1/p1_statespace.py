import sys
import copy


def fill(state,max,which):
    #state copy to not manipulate original state
    state2 = copy.deepcopy(state)
    if which == 0 :
        state2[0] = max[0]
        state2[1] = state[1]
        return(state2)
    elif which == 1 :
        state2[0] = state[0]
        state2[1] = max[1]        
        return(state2)
    
def empty(state,max,which):
    #empty the jug
    state2 = copy.deepcopy(state)
    if which == 0 :
        state2[0] = 0
        return state2
    elif which == 1 :
        state2[1] = 0
        return(state2)

def xfer(state,max,source,dest):
    state2 = copy.deepcopy(state)
    #transfer from source to dest until dest is full or source is empty
    i = state2[dest]
    j = max[dest]
    while i < j:
        state2[dest] += 1
        state2[source] -= 1
        i += 1
                
    return(state2)

#def succ(state,max):
    
 #return myset
                                                                                                                                                                                                                                                                 