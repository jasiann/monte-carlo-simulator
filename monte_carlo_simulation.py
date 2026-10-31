import math 
import random

def Simulate(coin, n): 
    success_count = 0
    
    for _ in range(n): 
        success_count += coin()
        
    p = success_count / n
    se = math.sqrt((p * (1 - p)) / n)
        
    return (p, se)

def coin(): 
    return random.randint(0, 1)

    
def play_set(probs):
    results = [random.random() < p for p in probs]
    return(results[0] and results[1]) or (results[1] and results[2])
    
def cfc_trial(): 
    return play_set([0.4, 0.8, 0.4])
def fcf_trial(): 
    return play_set([0.8, 0.4, 0.8])

    




    
        
        
    
        
    
    
    
    
    
     
    
    
