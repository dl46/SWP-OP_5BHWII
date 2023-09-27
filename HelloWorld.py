def hallo(name):
    for i in range(5):      # erzeugt die Zahl 4
        print(f"Hallo {name}") # f ... formated String
    
    for i in range(0, 50, 5): # von 0 bis 50 in 5er-Schritten 
        print(f"Hallo {name}") 

    if name == "ege":
        print("Es wird geheiratet")

hallo("egger")
hallo("ege")
