#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Fadhar J. Castillo
# Simple game of dice tossing using Quantum Computer simulator

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
IBMQ.load_accounts(hub=None)
def bit_from_counts(counts):
    return [k for k, v in counts.items() if v == 1][0]

def random_Integer():
    bits = ''
    #Since we only need numbers from 1 to 6, we can fit 6 in 3 bits
    backend_sim = BasicAer.get_backend('qasm_simulator')
    shots = 1
    max_credits = 3
    for x in range(1,3):
        quantumRegister = QuantumRegister(x)
        classicalRegister = ClassicalRegister(x)
        quantumCircuit = QuantumCircuit(quantumRegister, classicalRegister)
        quantumCircuit.h(quantumRegister)
        quantumCircuit.measure(quantumRegister, classicalRegister)
        job_simulation = execute(quantumCircuit, backend_sim, shots=shots)
        sim_result = job_simulation.result()
        counts = sim_result.get_counts(quantumCircuit)
        bits+=bit_from_counts(counts)
    return int(bits,2)

def play():
    #Build the quantum gates
    print("Quantum Pig has started!")
    print("")
    done = False
    score = 0
    while not done:
        print("Score: "+str(score))
        print("Options:")
        print("1. Toss")
        print("2. Give Up")
        selectionStr = input()
        try:
            selection = int(selectionStr)
            if selection == 1:
                while True:
                    randomInt = random_Integer()
                    if randomInt != 0 and randomInt != 7:
                        break
                if randomInt != 1:
                    print("")
                    print("You've tossed a " + str(randomInt))
                    score = score + randomInt
                    if score >= 50:
                        print("WE HAVE A WINNER!")
                        done = True
                else:
                    print("")
                    print("You've tossed a 1!")
                    print("GAME OVER")
                    done = True
            elif selection == 2:
                print("")
                print("I'm a quitter! I don't deserve respect!")
                done = True
            else:
                print("Please make a valid selection")
        except ValueError:
            print("Please make a valid selection")
    
print("-----Welcome to Quantum Pig-----")
correctInput = False
while not correctInput:
    print("1. Rules")
    print("2. Play")
    selectionStr = input()
    try:
        selection = int(selectionStr)
        if selection == 1:
            print("This game uses a single dice where your goal is to get to 50 points without getting a 1")
            print("You are able to throw the dice as many times as you want, but if the dice lands with 1")
            print("you lose the game. Good luck!")
        elif selection == 2:
            play()
        else:
            print("Please make a valid selection")
            correctInput = False
    except ValueError:
        print("Please make a valid selection")


# In[ ]:





# In[ ]:




