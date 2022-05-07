import random
import shutil
import os.path

def strtoint(x):
    if x.isdigit():
        x = int(x)
    return(x)

def readLines(file):
    result = []
    f = open(file)
    for line in f:
        result.append(line.replace("\n", ""))
    f.close()
    return result

    
def readItems(file):
    result = []
    f = open(file)
    for line in f:
        t = line.replace("\n", "").split(':')
        result.append(t)
    f.close()
    return result

listeAgent = readLines("Agent/Agent.txt")
listeArme = readItems("Arme/Arme.txt")
for i in range(len(listeArme)):
    listeArme[i][1] = strtoint(listeArme[i][1])

listeBouclier = readItems("Bouclier/Bouclier.txt")
for i in range(len(listeBouclier)):
    listeBouclier[i][1] = strtoint(listeBouclier[i][1])

class Joueur:
    def __init__(self,nom,enableAgent):
        self.nom = nom
        self.enableAgent = enableAgent
        self.nbragent = len(enableAgent)
        self.argent = 800
        self.joueur = False
        self.myAgent = 0


class Competence:
    def __init__(self,nom,prix,baseCount,maxCount):
        self.nom = nom
        self.prix = prix
        self.baseCount = baseCount
        self.maxCount = maxCount
        
        self.enableComp = range((maxCount-baseCount)+1)
        self.enableCompPrix = []
        for i in self.enableComp:
            self.enableCompPrix.append(self.enableComp[i]*self.prix)
        

class Agent :
    def __init__(self,nomAgent):
        self.competence = []
        self.nomAgent = nomAgent
        
        nomCompetence = []
        prix = []
        baseCount = []
        maxCount = []
        Comp_numero = 0

        #Lire fichier config
        filin = open("Agent/" + nomAgent + "/" + nomAgent + ".txt", "r")
        lignes = filin.readlines()
        for ligne in lignes:
    
            if ligne[0] == '1' :
                Comp_numero = 0
            if ligne[0] == '2' :
                Comp_numero = 1
            if ligne[0] == '3' :
                Comp_numero = 2
    
            if ligne[0] == 'c':
                nomCompetence.append(ligne[12:-1])
        
            if ligne[0] == 'p':
                prix.append(strtoint(ligne[6:-1]))
                
            if ligne[0] == 'b':
                baseCount.append(strtoint(ligne[11]))
                
            if ligne[0] == 'm':
                maxCount.append(strtoint(ligne[10]))
                self.competence.append(Competence(nomCompetence[Comp_numero],prix[Comp_numero],baseCount[Comp_numero],maxCount[Comp_numero]))
                
        filin.close()


def randComp(player):
    nbrComp = []
    numComp = []
    random.shuffle(player.myAgent.competence)
    for i in range(len(player.myAgent.competence)):
        while True:
            a = random.choice(player.myAgent.competence[i].enableComp)
            if player.myAgent.competence[i].enableCompPrix[a] <= player.argent:
                player.argent -= player.myAgent.competence[i].enableCompPrix[a]
                numComp.append(i)
                nbrComp.append(player.myAgent.competence[i].enableComp[a])
                break

    return nbrComp,numComp


def randArme(player):

    len_arme = range(len(listeArme))
    while True :
        random_arme = random.choice(len_arme)
        if listeArme[random_arme][1] <= player.argent:
            player.argent -= listeArme[random_arme][1]
            break
    return random_arme


def randBouclier(player):

    len_bouclier = range(len(listeBouclier))
    while True :
        random_bouclier = random.choice(len_bouclier)
        if listeBouclier[random_bouclier][1] <= player.argent:
            player.argent -= listeBouclier[random_bouclier][1]
            break
    return random_bouclier

def profile(nom):
    path = "Profile/" + nom + ".txt"
    if  not os.path.exists(path):
        shutil.copyfile("Profile/Default.txt", path)
    return Joueur(nom,readLines(path))
    


separation = "-"*25
joueur = [profile("LeJeanBonUltime"),profile("LeJeanBonUltime2")]
selected_Agent = []
nbrjoueur = len(joueur)
avancement = 1
if avancement == 1:
    for numero_joueur in range(nbrjoueur):

        #Enleve les champions en plusieurs ou qui n'existent pas
        enableAgent = joueur[numero_joueur].enableAgent
        for i in enableAgent:
            if enableAgent.count(i) > 1:
                for g2 in range(enableAgent.count(i)-1):
                    enableAgent.remove(i)
            if not (i in listeAgent):
                enableAgent.remove(i)
                    
        #Enleve les champions deja selectionné par d'autres joueurs
        for i in selected_Agent:
            #Regarde si le personnage est debloqué
            if enableAgent.count(i) > 0:
                enableAgent.remove(i)
        
        print(separation)
        #Securité au cas ou il n'y a plus d'agent disponible
        if len(enableAgent) > 0:
            randAgent = random.choice(enableAgent)
            joueur[numero_joueur].myAgent = Agent(randAgent)
            print(joueur[numero_joueur].nom, " le jeu a selectionné " , joueur[numero_joueur].myAgent.nomAgent," comme personnage, bonne chance !")
            selected_Agent.append(randAgent)
        #Cas impossible
        else:
            print(joueur[numero_joueur].nom, " le jeu n'a pas pu selectionné de personnage :(")
        print(separation)

    avancement = 2


while avancement == 2:
    for numero_joueur in range(nbrjoueur):
        print(joueur[numero_joueur].nom," tu as ",joueur[numero_joueur].argent)
        tirage = [0,1,2]

        while len(tirage) !=0:
            
            random.shuffle(tirage)
            tir = tirage[0]
            
            if tir == 2:
                random_competence = randComp(joueur[numero_joueur])
                print(joueur[numero_joueur].myAgent.nomAgent, " doit acheter :")
                for b in range(len(random_competence[1])):
                    print(" - ", random_competence[0][b], joueur[numero_joueur].myAgent.competence[random_competence[1][b]].nom)
                print(separation)

            if tir == 1:
                random_arme = randArme(joueur[numero_joueur])
                if random_arme != 0:
                    print(joueur[numero_joueur].myAgent.nomAgent, " doit acheter ", listeArme[random_arme][0])
                else :
                    print(joueur[numero_joueur].myAgent.nomAgent,listeArme[random_arme][0])
                print(separation)
                    
            if tir == 0:
                random_bouclier = randBouclier(joueur[numero_joueur])
                if random_bouclier != 0:
                    print(joueur[numero_joueur].myAgent.nomAgent, " doit acheter un bouclier de ", listeBouclier[random_bouclier][0])
                else:
                    print(joueur[numero_joueur].myAgent.nomAgent,listeBouclier[random_bouclier][0])
                print(separation)
            del tirage[0]

    for numero_joueur in range(nbrjoueur):
        print(joueur[numero_joueur].nom, "combien as-tu maintenant ?")
        joueur[numero_joueur].argent = strtoint(input())

    print("voulez-vous continuer ?")
    avancement = strtoint(input())









            
