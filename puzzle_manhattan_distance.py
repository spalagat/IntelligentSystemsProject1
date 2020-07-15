# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 15:50:03 2019

@author: sunny
"""
import numpy as np
import copy
from operator import itemgetter 
"""This is a class called node,The objects of this node class called node objects represents each puzzle
    in object form which stores the puzzle and its parent puzzle and the g(n) and f(n) value of that particular
    puzzle node"""
class node:
    def __init__(self,node_element,g,f,parent_node):
        self.node_element = node_element
        self.g = g
        self.f = f
        self.parent_node = parent_node
    # This method returns g(n) value of that particular puzzle node object.
    def get_g(self):
        return self.g
    
    # This method returns f(n) value of that particular puzzle node object.
    def get_f(self):
        return self.f
    # This method returns the puzzle related to the particular node object.
    def get_node_element(self):
        return self.node_element
    # This method returns the parent node object of particular node object.
    def get_parent(self):
        return self.parent_node

"""This method is used to find all the solutions for a particular puzzle by taking the position where the
Zero is and generating the possible solutions by swapping the adjacent elements"""
    
def solution(length,i,j,state):
    """This if condition is used to sort out whenever there is zero in the edges of the puzzle and finds the possible solutions for the puzzle
    Here we have two possible solutions for the edge elements"""
    if (i==j) and (i==0 or i==length-1):
        # deepcopy() is used to create the duplicates of the state puzzle
        s1=copy.deepcopy(state)
        s2 = copy.deepcopy(s1)
        if i==0:
            #swapping of the adjacent elements 
            temp1 = s1[i][j]
            s1[i][j] = s1[i][j+1]
            s1[i][j+1] = temp1
            
            temp2 = s2[i][j]
            s2[i][j] = s2[i+1][j]
            s2[i+1][j] = temp2
            return s1,s2
            
        elif i==length-1:
            #swapping of the adjacent elements 
            temp1 = s1[i][j]
            s1[i][j] = s1[i][j-1]
            s1[i][j-1] = temp1
            
            temp2 = s2[i][j]
            s2[i][j] = s2[i-1][j]
            s2[i-1][j] = temp2
            return s1,s2
    #This if condition is used to sort out the edges where the row,column positions are not equal to each other
    elif (i+j==length-1) and (i==0 or i==length-1):
        s1=copy.deepcopy(state)
        s2 = copy.deepcopy(s1)
        if i==0:
            #swapping of the adjacent elements 
            temp1 = s1[i][j]
            s1[i][j] = s1[i][j-1]
            s1[i][j-1] = temp1
            
            temp2 = s2[i][j]
            s2[i][j] = s2[i+1][j]
            s2[i+1][j] = temp2
            return s1,s2
        elif i==length-1:
            #swapping of the adjacent elements 
            temp1 = s1[i][j]
            s1[i][j] = s1[i-1][j]
            s1[i-1][j] = temp1
            
            temp2 = s2[i][j]
            s2[i][j] = s2[i][j+1]
            s2[i][j+1] = temp2
            return s1,s2
    # This if condition is used if the zero is in the border rows or columns not the edges
    elif (i>0 and j==length-1) or (i==length-1 and j>0) or(i>0 and j==0) or (i==0 and j>0):
        # This case have three possible solutions
        s1=copy.deepcopy(state)
        s2 = copy.deepcopy(s1)
        s3 = copy.deepcopy(s2)
        if i==0:
            #swapping of the adjacent elements 
            temp1 = s1[i][j]
            s1[i][j] = s1[i][j+1]
            s1[i][j+1] = temp1
            
            temp2 = s2[i][j]
            s2[i][j] = s2[i+1][j]
            s2[i+1][j] = temp2
    
            temp3 = s3[i][j]
            s3[i][j] = s3[i][j-1]
            
            s3[i][j-1] = temp3
            return s1,s2,s3
        elif j==0:
            #swapping of the adjacent elements 
            temp1 = s1[i][j]
            s1[i][j] = s1[i][j+1]
            s1[i][j+1] = temp1
                
            temp2 = s2[i][j]
            s2[i][j] = s2[i+1][j]
            s2[i+1][j] = temp2
            
            temp3 = s3[i][j]
            s3[i][j] = s3[i-1][j]
            s3[i-1][j] = temp3
            return s1,s2,s3
                
        elif j==length-1:
            #swapping of the adjacent elements 
            
            temp1 = s1[i][j]
            s1[i][j] = s1[i-1][j]
            s1[i-1][j] = temp1
                
            temp2 = s2[i][j]
            s2[i][j] = s2[i+1][j]
            s2[i+1][j] = temp2
                
            temp3 = s3[i][j]
            s3[i][j] = s3[i][j-1]
            s3[i][j-1] = temp3
            return s1,s2,s3
        elif i==length-1:
            #swapping of the adjacent elements 
            temp1 = s1[i][j]
            s1[i][j] = s1[i-1][j]
            s1[i-1][j] = temp1
                
            temp2 = s2[i][j]
            s2[i][j] = s2[i][j+1]
            s2[i][j+1] = temp2
        
            temp3 = s3[i][j]
            s3[i][j] = s3[i][j-1]
            s3[i][j-1] = temp3
            return s1,s2,s3
    # This if condition is whenever the zero is in middle of the puzzle.
    else:
        #It has Four Possible Solutions.
        s1=copy.deepcopy(state)
        s2 = copy.deepcopy(s1)
        s3 = copy.deepcopy(s2)
        s4 = copy.deepcopy(s3)
        
        #swapping of the adjacent elements
        temp1 = s1[i][j]
        s1[i][j] = s1[i][j-1]
        s1[i][j-1] = temp1
        
        temp2 = s2[i][j]
        s2[i][j] = s2[i+1][j]
        s2[i+1][j] = temp2
        
        temp3 = s3[i][j]
        s3[i][j] = s3[i-1][j]
        s3[i-1][j] = temp3
        
        temp4 = s4[i][j]
        s4[i][j] = s4[i][j+1]
        s4[i][j+1] = temp4
        return s1,s2,s3,s4
        
         
#This method is used to find  and returns the heuristic value h(n) of the puzzle.        
def manhattan_heuristic(state,goal_state):
    
    length = len(state)
    h=0
    #Here we are iterating through the puzzle to find the manhattan distance of the each tile from its goal_state.
    for i in range(length):
        for j in range(length):
            #Here In this if condition we are finding the elements which are different from its goal_state
            if state[i][j] != goal_state[i][j] and state[i][j]!=0:
                #Here The where method finds the respective position of states element in goalstate
                g = np.where(goal_state==state[i][j])
                #calculating the distance of element from its location in goal_state
                g1 = abs(g[0][0]-i)
                g2 = abs(g[1][0]-j)
                f = g1+g2
                
                h = h+f
    return h

                
#This Method returns the list of child nodes of the parent node.        
def possible_solution(parent_state,goal_state):
    
    state = parent_state.get_node_element()
    g_n = parent_state.get_g()
    g = g_n+1
    child_list = []
    length = len(state)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0: 
                if (i==0 or i==length-1) and (j==0 or j==length-1):
                    
                    s1,s2 = solution(length,i,j,state)
                    #here we are finding the heuristic values of the child_node
                    h1 = manhattan_heuristic(s1,goal_state)
                    h2 = manhattan_heuristic(s2,goal_state)
                    # here we are finding the f(n) values 
                    f1 = h1+g
                    f2 = h2+g
                    # child nodes of the parent node.
                    child1 = node(s1,g,f1,parent_state)
                    child2 = node(s2,g,f2,parent_state)
                    child_list = [child1,child2]
                    return child_list
                    
                elif (i>0 and j==length-1) or (i==length-1 and j>0) or(i>0 and j==0) or (i==0 and j>0):
                    s1,s2,s3 = solution(length,i,j,state)
                    #here we are finding the heuristic values of the child_node
                    h1 = manhattan_heuristic(s1,goal_state)
                    h2 = manhattan_heuristic(s2,goal_state)
                    h3 = manhattan_heuristic(s3,goal_state)
                    # here we are finding the f(n) values
                    f1 = h1+g
                    f2 = h2+g
                    f3 = h3+g
                    # child nodes of the parent node.
                    child1 = node(s1,g,f1,parent_state)
                    child2 = node(s2,g,f2,parent_state)
                    child3 = node(s3,g,f3,parent_state)
                    
                    child_list = [child1,child2,child3]
                    return child_list
                
                else:
                    s1,s2,s3,s4 = solution(length,i,j,state)
                    #here we are finding the heuristic values of the child_node
                    h1 = manhattan_heuristic(s1,goal_state)
                    h2 = manhattan_heuristic(s2,goal_state)
                    h3 = manhattan_heuristic(s3,goal_state)
                    h4 = manhattan_heuristic(s4,goal_state)
                    # here we are finding the f(n) values
                    f1 = h1+g
                    f2 = h2+g
                    f3 = h3+g
                    f4 = h4+g
                    
                    # child nodes of the parent node.
                    child1 = node(s1,g,f1,parent_state)
                    child2 = node(s2,g,f2,parent_state)
                    child3 = node(s3,g,f3,parent_state)
                    child4 = node(s4,g,f4,parent_state)
                    child_list = [child1,child2,child3,child4]
                    return child_list
                    
"""This Method is Used to Check the node which has to be expanded is already expanded or not."""                
def check_existing(expanded_nodes,state):
    element = state.get_node_element()
    for node in expanded_nodes:
        node_element = node.get_node_element()
        if np.all(node_element == element):
            return True
        
        
    
"This Method performs the complete A_star algorithm"        
def Input(state,goal_state):
    """This is dictionary which i use for storing the generated nodes where the key is the object address
       and the value is its f(n) value"""
    generated_nodes={}
    "This is a list called expanded nodes which we use to store the nodes that got expanded."
    expanded_nodes=[]
    "This is a list called all_generated nodes which we use to store the nodes that got generated."
    all_generated_nodes = []
    generated_nodes[state] = state.get_f()
    """generated_list is a list that carries a list of tuples(which has both nodes address and its f(n) value) in the increasing
    of its f(n) value,Its the priority queue """
    generated_list = sorted(generated_nodes.items(),key =itemgetter(1))
    
    
    while True:
        #Its the first node in the priority queue
        state = generated_list[0][0]
        parent = state.get_node_element()
        #Checking whether the current_state is the goal_State or not.
        if np.all(parent == goal_state):
            #If Yes,It returns the current_state puzzle,all the generated nodes count,expanded nodes count.
            return state,len(all_generated_nodes),len(expanded_nodes)
        else:
            #if not we expand the cuurent state.
            #Here we are checking the whether node to be expanded is already expanded or not 
            result = check_existing(expanded_nodes,state)
            #if the result is true, we remove the node from the priority queue 
            if result == True:
                #Removing the node from priority queue.
                top_element = generated_list.pop(0)
                del generated_nodes[top_element[0]]
                
            else:
                #Here we are finding the child nodes of the current_node
                child_nodes = possible_solution(state,goal_state)
                #Poping the current node element from the priority queue after expansion. 
                top_element = generated_list.pop(0)
                del generated_nodes[top_element[0]]
                #adding the expanded node to expanded nodes.
                expanded_nodes.append(top_element[0])
                # looping through all the child node and adding into priority queue
                for child in child_nodes:
                    generated_nodes[child] =child.get_f()
                    all_generated_nodes.append(child)
                #Sorting the generated_list based on the f(n) values of the nodes after adding the child nodes.      
                generated_list = sorted(generated_nodes.items(),key =itemgetter(1))
    
            
    
if __name__ == '__main__':
     puzzle_length = 3
     puzzle = []
     goal_puzzle = []
     #Entering the input elements.
     print("Enter the elements for input puzzle")
     for i in range(puzzle_length):
         l2 = []
         print("For "+str(i+1)+" Row")
         for j in range(puzzle_length):
             element = int(input("enter the "+str(j+1)+" element for "+str(i+1)+" row : "))
             l2.append(element)
         puzzle.append(l2)
     #Entering the elements to goal_State puzzle.
     print("Enter the elements for goal_state")
     for i in range(puzzle_length):
         l2 = []
         print("For "+str(i+1)+" Row")
         for j in range(puzzle_length):
             element = int(input("enter the "+str(j+1)+" element for "+str(i+1)+" row : "))
             l2.append(element)
         goal_puzzle.append(l2)
         
     intial_state = np.array(puzzle)    
     goal_state = np.array(goal_puzzle)
     #intial g(n) value.
     g=0
     #Finding the intial h(n) value.  
     h = manhattan_heuristic(intial_state,goal_state)
     f= g+h
     state = node(intial_state,g,f,None)
     print()
     print("Input :")
     print(str(state.get_node_element()))
     #Calling the Input() method
     output,generated_nodes_count,expanded_nodes_count = (Input(state,goal_state))
     print("Output :")
     print(output.get_node_element())
     print("generated_nodes : "+str(generated_nodes_count))
     print("expanded_nodes : "+str(expanded_nodes_count))
     print("Total path_cost :" +str(output.get_f()))
     print()
     parent_node = output
     l1=[parent_node.get_node_element()]
     for i in range(parent_node.get_g()):
         parent_node = parent_node.get_parent()
         l1.append(parent_node.get_node_element())
     print("Printing the path :")
     for i in range(output.get_g(),-1,-1):
         print(l1[i])
         print(" |")
         print(" |")
         print("\/")
         print()
    
         
     
     