import random
from random import randint

        
def ziehung():  #Methode zum Ziehen von 6 aus 45 Lottozahlen
    gezogen = []    #Liste mit den gezogenen Lotto-Zahlen
    
    while len(gezogen) < 6:
        lottozahl = random.randint(1, 45)
        if lottozahl not in gezogen:
            gezogen.append(lottozahl)    
    
    gezogen.sort()                  
    
    return gezogen
    
    
    
if __name__ == "__main__":
    stats = {}  #Dictionary für die Statistik
    zaehler = 0
    
    for i in range(999):    #1000 Ziehungen (-1 weil 0 auch mitgezählt wird)
        gezogen = ziehung()
        for lottozahl in gezogen:
            if lottozahl in stats:
                stats[lottozahl] += 1
            else:
                stats[lottozahl] = 1
    
    for x, y in sorted(stats.items()):
        print(f"Zahl: {x} Haeufigkeit: {y}")









