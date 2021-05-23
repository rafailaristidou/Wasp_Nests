
import math
import numpy as np
import random
import copy

def kill(n,d_max,d):
    k = (n * d_max)/((20*d)+0.00001)
    if k>n:
        return n
    return k

def distance(x1,x2,y1,y2):
    d = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return math.fabs(d)


    

def fitness_calculate(folies,population):
  
  #population
  for i in range (100):
   
    tempFolies = copy.deepcopy(folies)
    total_kill = 0 
    for z in [0,2,4]:
        for y in range (12):
            d[y] = distance(tempFolies[y][0],population[i][z],tempFolies[y][1],population[i][z+1])
            #poses exoun skotothi apo tin vomva mono aftin ti fora
            tmp_kill = kill(tempFolies[y][2],d_max,d[y])
            #poses exoun skotothi sinolika
            total_kill += tmp_kill
                
            
            #otan o arithmos ton thanatpn einai megaliteros apo ton arithmon ton sfikon vale sthn fwlia 0
            if((tempFolies[y][2]-tmp_kill)>=0):
                tempFolies[y][2] -= tmp_kill
            else:
                tempFolies[y][2] = 0
                    
        #enimerosi tou total sfikes_kill_total
        sfikes_kill_total[i][0] = total_kill
        sfikes_kill_total[i][z+1] = population[i][z]
        sfikes_kill_total[i][z+2] = population[i][z+1]

  return sfikes_kill_total

def select_individual_by_tournament(population):
    #dimiourgia 50 tixeon population afxanontas tes pithanotites na epilexthoun me vasi ton kills tous
    best_population=np.zeros((50,7))
    best_population_size = int(len(best_population))
    population = np.random.randint(1,100,size=(100,7),dtype=int)
    x=population[:,[0]]
    best_population=random.choices(population, weights = x, k = 50)
    # dialegoume tous dio gonis
    fighter_1 = random.randint(0, best_population_size-1)
    fighter_2 = random.randint(0, best_population_size-1)
    
    # to score gia ton kathe 1
    fighter_1_fitness = best_population[fighter_1][0]
    fighter_2_fitness = best_population[fighter_2][0]
    
    
    if fighter_1_fitness >= fighter_2_fitness:
        winner = fighter_1
    else:
        winner = fighter_2
    
    # epistrefoume ton kalitero
    return population[winner]

def breed_by_crossover(indA,indB):
    
    
    
    
    
    x=np.zeros(6)
    newChild1 = np.zeros(7)
    newChild2 = np.zeros(7)
    for i in range(6):
        x[i]=random.choice([1,2])
        
    #Uniform Crossover
    '''for i in range(1,7):
        
        if(x[i-1]==1):
            newChild1[i] = indA[i]
            newChild2[i] = indB[i]
        else:
            newChild1[i] = indB[i]
            newChild2[i] = indA[i]'''
    
    #two point crossover
    firsPoint = random.choice([1,2])
    secontPoint=random.choice([1,2])
    thirdPoind=random.choice([1,2])
    for i in range(1,3):
        if(firsPoint==1):
            newChild1[i] = indA[i]
            newChild2[i] = indB[i]
        else:
            newChild1[i]= indB[i]
            newChild2[i] = indA[i]
            
    for i in range(3,5):
        if(secontPoint==1):
            newChild1[i] = indA[i]
            newChild2[i] = indB[i]
        else:
            newChild1[i] = indB[i]
            newChild2[i] = indA[i]
            
    for i in range(5,7):
        if(thirdPoind==1):
            newChild1[i] = indA[i]
            newChild2[i] = indB[i]
        else:
            newChild1[i] = indB[i]
            newChild2[i] = indA[i] 
            
    return newChild1,newChild2


def randomly_mutate_population(population, mutation_probability):
    
    # dimiourgoume tixeo mutation
        random_mutation_array = np.random.random(
            size=(population.shape))
        
        random_mutation_boolean = \
            random_mutation_array <= mutation_probability

        population[random_mutation_boolean] = \
        np.logical_not(population[random_mutation_boolean])
        
        # epistrefoume mutation population
        return population

d = np.zeros(12)
d_max=141.42
best_score=np.zeros((100,7))

folies=np.array([[25,65,100],[23,8,200],[7,13,327],[95,53,440],
            [3,3,450],[54,56,639],[67,78,650],[32,4,678],
            [24,76,750],[66,89,801],[84,4,945],[34,23,967]])
sort_total=[]
sfikes_kill_total=np.zeros((100,7))
# dimiourgoume tixeo population

population = np.random.randint(1,100,size=(100,6),dtype=int)

sfikes_kill_total=fitness_calculate(folies,population)
sfikes_kill_total=np.array(sorted(sfikes_kill_total, key=lambda kills: kills[0],reverse=True))
best_bombs_1x=sfikes_kill_total[0][1]
best_bombs_1y=sfikes_kill_total[0][2]
best_bombs_2x=sfikes_kill_total[0][3]
best_bombs_2y=sfikes_kill_total[0][4]
best_bombs_3x=sfikes_kill_total[0][5]
best_bombs_3y=sfikes_kill_total[0][6]
score=sfikes_kill_total[0][0]

for i in range(7):
    best_score[0][i]=score
    best_score[0][i]=best_bombs_1x
    best_score[0][i]=best_bombs_1y
    best_score[0][i]=best_bombs_2x
    best_score[0][i]=best_bombs_2y
    best_score[0][i]=best_bombs_3x
    best_score[0][i]=best_bombs_3y

half_population_size=int(len(population)/2)
for generation in range(100):
    
    new_population=[]
    

    # gemizoume neo population me 2 pedia kathe fora
    for i in range(half_population_size):
        
        parent_1 = select_individual_by_tournament(sfikes_kill_total)
        parent_2 = select_individual_by_tournament(sfikes_kill_total)
        child_1,child_2 = breed_by_crossover(parent_1, parent_2)
        new_population.append(child_1)
        new_population.append(child_2)

        
        
    x =np.array(new_population)
    population=x[:,[1,2,3,4,5,6]]
    #kanoume to mutation
    mutation_rate = 0.2
    population = randomly_mutate_population(population, mutation_rate)
    
    # vriskoume to fitness
    sfikes_kill_total=fitness_calculate(folies,population)
    #vriskoyme ta kalitera
    sfikes_kill_total_sort=np.array(sorted(sfikes_kill_total, key=lambda kills: kills[0],reverse=True))
    best_bombs_1x=sfikes_kill_total_sort[0][1]
    best_bombs_1y=sfikes_kill_total_sort[0][2]
    best_bombs_2x=sfikes_kill_total_sort[0][3]
    best_bombs_2y=sfikes_kill_total_sort[0][4]
    best_bombs_3x=sfikes_kill_total_sort[0][5]
    best_bombs_3y=sfikes_kill_total_sort[0][6]
    score=sfikes_kill_total_sort[0][0]
    best_score[generation]=[score,best_bombs_1x,best_bombs_1y,best_bombs_2x,best_bombs_2y,best_bombs_3x,best_bombs_3y]

for i in range(len(best_score)):
    print("Generation: {}   ".format(i+1))
    print("Kills:{} \nBomb1 X:{},Bomb1 Y:{} \nBomb2 X:{},Bomb2 Y:{} \nBomb3 X:{},Bomb3 Y:{}".format(best_score[i][0],
                                                                                                  best_score[i][1],
                                                                                                  best_score[i][2],
                                                                                                  best_score[i][3],
                                                                                                  best_score[i][4],
                                                                                                  best_score[i][5],
                                                                                                  best_score[i][6]))

best_score=np.array(sorted(best_score, key=lambda kills: kills[0],reverse=True))
print("Best Generation:    ")
print("Kills:{} \nBomb1 X:{},Bomb1 Y:{} \nBomb2 X:{},Bomb2 Y:{} \nBomb3 X:{},Bomb3 Y:{}".format(best_score[0][0],
                                                                                                  best_score[0][1],
                                                                                                  best_score[0][2],
                                                                                                  best_score[0][3],
                                                                                                  best_score[0][4],
                                                                                                  best_score[0][5],
                                                                                                  best_score[0][6]))
    