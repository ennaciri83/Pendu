# jeu pendu

import random
from tkinter import *

aa = """                                     
  ____    _____   ______   _   _  __      __  ______   _   _   _    _   ______   
 |  _ \  |_   _| |  ____| | \ | | \ \    / / |  ____| | \ | | | |  | | |  ____|  
 | |_) |   | |   | |__    |  \| |  \ \  / /  | |__    |  \| | | |  | | | |__     
 |  _ <    | |   |  __|   | . ` |   \ \/ /   |  __|   | . ` | | |  | | |  __|    
 | |_) |  _| |_  | |____  | |\  |    \  /    | |____  | |\  | | |__| | | |____   
 |____/  |_____| |______| |_| \_|     \/     |______| |_| \_|  \____/  |______|  


  _____    ______  __      __   ____    _____     _____                          
 |  __ \  |  ____| \ \    / /  / __ \  |  __ \   / ____|                         
 | |  | | | |__     \ \  / /  | |  | | | |__) | | (___                           
 | |  | | |  __|     \ \/ /   | |  | | |  ___/   \___ \                          
 | |__| | | |____     \  /    | |__| | | |       ____) |                         
 |_____/  |______|     \/      \____/  |_|      |_____/      """

print(aa)


fh = open("d:\mots pendu.txt", "r")
words = fh.read()
print(words)
fh.close()

class Jeu_pendu(object):

    pendu = []
    pendu.append(' +---+')
    pendu.append(' |   |')
    pendu.append('     |')
    pendu.append('     |')
    pendu.append('     |')
    pendu.append('     |')
    pendu.append('=======')

    homme = {}
    homme[0] = [' 0   |']
    homme[1] = [' 0   |', ' |   |']
    homme[2] = [' 0   |', '/|   |']
    homme[3] = [' 0   |', '/|\\  |']
    homme[4] = [' 0   |', '/|\\  |', '/    |']
    homme[5] = [' 0   |', '/|\\  |', '/ \\  |']

    dessins = []

    words = words.split()

    infStr = """╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"""

    def __init__(self, *args, **kwargs):
        i, j = 2, 0
        print(i)
        #print(type(homme))

        self.dessins.append(self.pendu[:])
        for ls in self.homme.values():
            dessin, j = self.pendu[:], 0
            for m in ls:
                dessin[i + j] = m
                j += 1
            self.dessins.append(dessin)

    def mot_Aleatoire(self):
        Mot_aleat=(self.words[random.randint(0, len(self.words) - 1)]).upper()
        print("mot aleatoire cest"+Mot_aleat)
        return Mot_aleat

    def dessiner_homme(self, idx, wordLen):
        for line in self.dessins[idx]:
            print(line)

    def verifier_valeur_entrer(self, mot_chercher, resultat, caracteres_incorrectes):
        valeur_entrer = (input()).upper()
        while valeur_entrer not in ("azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN") or valeur_entrer == ""or len(valeur_entrer) != 1 :
            valeur_entrer = input("Entrer un seul caractere pas de mot ni chiffres svp :")


        if ( valeur_entrer in caracteres_incorrectes):
            return None, False

        i = 0
        caracetre_correct = valeur_entrer in mot_chercher
        for c in mot_chercher:
            if c == valeur_entrer:
                resultat[i] = c
            i += 1
        return valeur_entrer, caracetre_correct

    def info(self, info):
        ln = len(self.infStr)
        print(self.infStr[:-3])
        print(info)
        print(self.infStr[3:])

    def start(self):
        print('Bienvenue au jeu de Pendu !')
        Mot_aleatoire = list(self.mot_Aleatoire())
        result = list('*' * len(Mot_aleatoire))
        print('''Le Mot ce compose de {} lettres: '''.format(len(Mot_aleatoire)), result)
        trouver, i, perdu = False, 0, []
        while i < len(self.dessins) - 1:
            print('Entrer un caractere SVP : ', end='')
            caractere_saisie, right = self.verifier_valeur_entrer(Mot_aleatoire, result, perdu)
            if caractere_saisie == None:
                print('Vous avez déja entrer cette lettre ,essais encors  ')
                continue
            print(''.join(result))
            if result == Mot_aleatoire:

                self.info('''                                                      \ \   / /  / __ \  | |  | |     
                                                       \ \_/ /  | |  | | | |  | |     
                                                        \   /   | |  | | | |  | |     
                                                         | |    | |__| | | |__| |     
                                                         |_|     \____/   \____/      


                                                      __          __  _____   _   _   
                                                      \ \        / / |_   _| | \ | |  
                                                       \ \  /\  / /    | |   |  \| |     ☺ :AVEC  {} FAUTE(S) . 
                                                        \ \/  \/ /     | |   | . ` |     ♥ : ET {}  ESSAIS .
                                                         \  /\  /     _| |_  | |\  |  
                                                          \/  \/     |_____| |_| \_|                                     '''.format(len(perdu),(len(perdu)+len(result))))
                trouver = True
                break
            if not right:
                perdu.append(caractere_saisie)
                i += 1
            self.dessiner_homme(i, len(Mot_aleatoire))
            print('les caractères incorrects ', perdu)

        if not trouver:
            self.info('Le mot été  \'' + ''.join(Mot_aleatoire) + '\' ! Vous avez Perdu  !!!!')


a = Jeu_pendu().start()
