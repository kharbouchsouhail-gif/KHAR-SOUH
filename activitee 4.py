
with open("table_de_multiplication.txt", "w") as fichier:
   
    for i in range(1, 11):
        fichier.write(f"Table de {i} :\n")
        fichier.write("------------------\n")
        
        for j in range(1, 11):
            resultat = i * j
            fichier.write(f"{i} x {j} = {resultat}\n")
        fichier.write("\n") 


try:
    with open("table_de_multiplication.txt", "r") as fichier:
        contenu = fichier.read()   
        print(contenu)             
except FileNotFoundError:
    print(" Le fichier 'table_de_multiplication.txt' n'existe pas encore.")


