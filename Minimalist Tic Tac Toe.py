##########################################################
# Author : Frédéric Spataro                              #
# OS Windows 10, Python 3.7.1 32 bits                    #
# Title : Minimalist Tic Tac Toe (ft Yann & Theo)        #
# Licence GPL                                            #
##########################################################

#########################################
# Let's define few things

def constructionGrille():
    for nLigne in range(3):
        ligne=[]
        for nColonne in range(3):
            ligne.append('.')
        grille.append(ligne)

def conditionvictoire():
    if (grille[0][0]==grille[0][1]==grille[0][2] and grille[0][0]=='x') or (grille[1][0]==grille[1][1]==grille[1][2] and grille[1][0]=='x') or (grille[2][0]==grille[2][1]==grille[2][2] and grille[2][0]=='x') or (grille[0][0]==grille[1][0]==grille[2][0] and grille[0][0]=='x') or (grille[0][1]==grille[1][1]==grille[2][1] and grille[0][1]=='x') or (grille[0][2]==grille[1][2]==grille[2][2] and grille[0][2]=='x') or (grille[0][0]==grille[1][1]==grille[2][2] and grille[0][0]=='x') or (grille[0][2]==grille[1][1]==grille[2][0] and grille[1][1]=='x'):
        return 'j1'
    elif (grille[0][0]==grille[0][1]==grille[0][2] and grille[0][0]=='o') or (grille[1][0]==grille[1][1]==grille[1][2] and grille[1][0]=='o') or (grille[2][0]==grille[2][1]==grille[2][2] and grille[2][0]=='o') or (grille[0][0]==grille[1][0]==grille[2][0] and grille[0][0]=='o') or (grille[0][1]==grille[1][1]==grille[2][1] and grille[0][1]=='o') or (grille[0][2]==grille[1][2]==grille[2][2] and grille[0][2]=='o') or (grille[0][0]==grille[1][1]==grille[2][2] and grille[0][0]=='o') or (grille[0][2]==grille[1][1]==grille[2][0] and grille[1][1]=='o'):
    	return 'j2'
    elif grille[0].count('.')+grille[1].count('.')+grille[2].count('.')==0:
    	return 'null'
    else:
    	return '0'

def inexistante():
    print('This case doesnt exist.\nPlease try again.')
    afficheGrille()

def occupee():
    print('This case is already filled.\nPlease try again.')
    afficheGrille()

v1=0
v2=0

def scorejouer():
    if conditionvictoire()=='j1':
        print('Player 1 won.')
        global v1
        v1=v1+1
    elif conditionvictoire()=='j2':
        print('Player 2 won.')
        global v2
        v2=v2+1
    elif conditionvictoire()=='null':
        print("It's a tie, no one won.")
    if conditionvictoire()!='0':
        print('Score:\nPlayer 1:',v1,'\nPlayer 2:',v2)
        a=input('Do you want to play again? Y/N:')
        if a=='Y' or a=='y':
            for i in range (3):
                for j in range (3):
                    grille[i][j]='.'
            afficheGrille()
        else:
            print("Thanks for playing!")

def joueur1(ligne,colonne):
    x='x'
    if ligne in [0,1,2]:
        if colonne in [0,1,2]:
            if grille[ligne][colonne]!='.':
                occupee()
            else:
                grille[ligne][colonne]=x
                afficheGrille()
                conditionvictoire()
                if conditionvictoire()=='0':
                    print("Player2's turn.")
                scorejouer()
        else:
            inexistante()
    else:
        inexistante()


def joueur2(ligne,colonne):
    o='o'
    if ligne in [0,1,2]:
        if colonne in [0,1,2]:
            if grille[ligne][colonne]!='.':
                occupee()
            else:
                grille[ligne][colonne]=o
                afficheGrille()
                conditionvictoire()
                if conditionvictoire()=='0':
                    print("Player1's turn.")
                scorejouer()
        else:
            inexistante()
    else:
        inexistante()

##############################################
# Let's launch that game

grille=[]
constructionGrille()
afficheGrille()
