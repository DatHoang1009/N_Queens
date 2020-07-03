# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:53:30 2020
@author: datho
"""
# -*- coding: utf-8 -*-
"""
//////////////////// ALL ASSIGNMENTS INCLUDE THIS SECTION /////////////////////
//
// Title: N-Queens
// Files: N_Queens.py
// Course: CS 540, Spring 2020
//
// Author: Dat Hoang
// Email: dthoang2@wisc.edu
//
///////////////////////////// CREDIT OUTSIDE HELP /////////////////////////////
//
/////////////////////////////// 80 COLUMNS WIDE ///////////////////////////////
"""
import random

"""
Check if block is a boulder a not

@param i: CorX of the block
@param j: CorY of the block
@param boulderX: CorX of the boulder
@param boulderY: Cofy of the boulder
@return 1 if block is the boulder
@return 0 if not
"""
def is_boulder(i,j,boulderX, boulderY):
    if i == boulderX:
        if j == boulderY:
            return 0
    return 1

"""
generate all successor states of the given state

@param state: state that generated
@param boulderX: CorX of the boulder
@param boulderY: Cofy of the boulder
@return list1: list1 of sorted successor states
"""
def succ_state_helper(state, boulderX, boulderY):
    list1 = []
    new_state =[]+ state
    for i in range(len(state)):
        for j in range(len(state)):
            if (is_boulder(i,j,boulderX,boulderY) == 1):
                new_state[i] = j
                temp = [] + new_state
                if (temp != state):
                    list1.append(temp)
                new_state = [] + state
    list1 = sorted(list1, reverse = True)
    return list1

"""
print out generate all successor states of the given state
in sorted order
@param state: state that generated
@param boulderX: CorX of the boulder
@param boulderY: Cofy of the boulder
"""
def succ(state, boulderX, boulderY):
    list1 = succ_state_helper(state, boulderX, boulderY)
    for i in range(len(list1)):
        if (i == 0):
            print("["+str(list1[i])+",")
        elif (i == (len(list1))):
            print(str(list1[i]) + "]")
        else:
            print(str(list1[i]) + ",")

"""
Check if block is line attacked
@corY: Cor-y of checked block
@corX: Cor-x of checked block
@param state: state that generated
@param boulderX: CorX of the boulder
@param boulderY: Cofy of the boulder
@return 1 if block is line attacked
@return 0 else
"""
def line_attack(corY, corX, state, boulderX, boulderY):
    count = 0
    if (corY == boulderY):
        if (corX < boulderX):
            for i in range(0,boulderX-1):
                if (state[i] == corY) and (i != corX):
                    return 1
        if (corX > boulderX):
            for j in range(boulderX+1,len(state)):
                if (state[j] == corY) and (j != corX):
                    return 1
    else:
        count =+ state.count(corY)
        if (count >= 2):
            return 1
    return 0

"""
Check if block is diagonal attacked
@corY: Cor-y of checked block
@corX: Cor-x of checked block
@param state: state that generated
@param boulderX: CorX of the boulder
@param boulderY: Cofy of the boulder
@return 1 if block is diagonal attacked
@return 0 else
"""
def diagonal_attack(corY, corX, state, boulderX, boulderY):
    if (abs(corX-boulderX) == abs(corY-boulderY)):
        if (corX < boulderX):
            for i in range(0,boulderX):
                if (abs(state[i]-corY) == abs(i-corX)) and (corX !=i):
                    return 1
        if (corX > boulderX):
            for j in range(boulderX, len(state)):
                if (abs(state[j]-corY) == abs(j-corX)) and (corX !=j):
                    return 1    
    else:
        for j in range(len(state)):
            if (abs(state[j]-corY) == abs(j-corX)) and (corX !=j):
                    return 1
    return 0
        
"""
count number of queen attacked in state
@param state: state that generated
@param boulderX: CorX of the boulder
@param boulderY: Cofy of the boulder
@return count: number of queen being attacked
"""   
def f(state, boulderX, boulderY):
    count = 0
    for i in range(len(state)):
        if (line_attack(state[i],i,state, boulderX, boulderY) == 1):
            count = count + 1
        if (diagonal_attack(state[i],i,state, boulderX, boulderY) == 1):
            count = count + 1
        if (line_attack(state[i],i,state, boulderX, boulderY) == 1) and \
        (diagonal_attack(state[i],i,state, boulderX, boulderY) == 1):
            count = count - 1
    return count

"""
choose the best next state from current state's successors
@param curr: current state
@param boulderX: CorX of the boulder
@param boulderY: Cofy of the boulder
@return state: choosen state
"""
def choose_next(curr, boulderX, boulderY):
    state = []
    temp = f(curr, boulderX, boulderY)
    list1 = succ_state_helper(curr, boulderX, boulderY)
    list1.append(curr)
    list1 = sorted(list1, reverse = True)
    for i in list1:
        if (temp >= f(i, boulderX, boulderY)):
            temp =+ f(i, boulderX, boulderY)
            state = [] + i
            if (temp == f(i, boulderX, boulderY)):
                if list1.index(curr) > list1.index(i):
                    state = [] + i                  
    if (state == curr):
        return None
    return state

"""
solve the problem until get smallest f 
@param initial_state: 1st state
@param boulderX: CorX of the boulder
@param boulderY: Cofy of the boulder
@return list1[len(list1)-1] the ffinal successor state that have smallest f
"""
def nqueens(initial_state, boulderX, boulderY):
    list1 = []
    state1 = initial_state
    list1.append(initial_state)
    while (f != 0):
        if choose_next(state1, boulderX, boulderY) is None:
            break
        temp = choose_next(state1, boulderX, boulderY)        
        list1.append(temp)
        state1 = [] + temp      
    for i in list1:
        print(str(i) + ' - f='+ str(f(i,boulderX,boulderY)))
    return list1[len(list1)-1]

"""
restart, randomly take another stage and solve to get result
if result state has f=0, stop, else run for k times and get the smallest f
stages in sorted order
@param n: size of chess board
@param k: number of time restart
@param boulderX: CorX of the boulder
@param boulderY: Cofy of the boulder
@return temp_state the final successor state that has f = 0
@return f(temp_state,x,y) f of the final state
"""
def nqueens_restart(n, k, boulderX, boulderY):
    x = boulderX
    y = boulderY
    list1 = []
    state = []
    result_state = []
    for i in range(1,k+1):
        print('Run' + str(i) + ':')
        for j in range(0,n):
            num = random.randint(0,n-1)
            while (j == boulderX) and (num == boulderY):
                num =+ random.randint(0,n)
            state.append(num) 
        temp_state =[] + nqueens(state, boulderX, boulderY)
        state = []
        if (f(temp_state, boulderX, boulderY) == 0):
            return print('Result is:\n' + str(temp_state)\
                         +' - f='+str(f(temp_state,x,y)))
        else:
            print('Gets stuck at f=' + str(f(temp_state,x,y)))
            print('')
        result_state.append(temp_state)     
    temp_f = n
    for m in result_state:
        if (temp_f > f(m,x,y)):
            temp_f =+ f(m,x,y)
    for m in result_state:
        if (f(m,x,y) == temp_f):
            list1.append(m)
    list1 = sorted(list1)
    print('Best Solutions:')
    for i in list1:
        print(str(i))
    
        
    
        
        