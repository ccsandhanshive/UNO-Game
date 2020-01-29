#shorturl.at/cmpuG
#shorturl.at/FGJ14
import random
import time
import sys

def Order(player,n,order,i,computer,tern):
    
    if i>n-1:
        i=0
    while chckWiner(i,n):					#if player is not win
        time.sleep(0.1)
        
        print("serve cards -> {}".format(serv_cards))
        print("player{}->{}".format(i,player[i]))
        if computer==1 and tern=='C':
            card_number=checkPresent(player,i,serv_cards,order,n,computer,tern)  #check matching card is present or not
            tern='H'
        elif computer==1 and tern=='H':
            card_number=int(input("Enter card no to serve"))
            tern='C'
        else:
            card_number=int(input("Enter card no to serve"))
        if card_number<0 or card_number>len(player[i])-1:
            print("invalid")
            player[i].append(random.choice(list(set(final_desk)-set(serv_cards)-set(player[i]))))
        elif len(serv_cards)==0 or checkMatchning(player[i][card_number],serv_cards[len(serv_cards)-1],player,n,order,i,card_number,computer,tern):
            serv_cards.append(player[i][card_number])            
            player[i].remove(player[i][card_number])
        else:
            print("invalid")
            player[i].append(random.choice(list(set(final_desk)-set(serv_cards))))
        
        
        if order==0 or order==10:
            if i>=n-1:
                i=0
            else:
                i=i+1
        elif order==1:
            if i<=0:
                i=n-1
            else:
                i=i-1
        #print("temp={}".format(len(temp_final)))
        
        #print("temp={}".format(len(temp_final)))
    else:
        print("Game Over")
        sys.exit()
        
def chckWiner(i,n):
    if i<0:
        i=n+i
    print(len(player[i]))
    if len(player[i])==0:
        print("player {} win".format(i))
        print("Game Over")
        sys.exit()
    return True


def removeFromFinal(final_desk,serv_cards):			#remove serv card from final set of cards
    final_desk=set(final_desk)-set(serv_cards)
    return 
            
def checkPresent(player,i,serv_cards,order,n,computer,tern):   #check matching card is present or not
    for card1_no in range(len(player[i])):
        if len(serv_cards)==0 or (checkMatchning(player[i][card1_no],serv_cards[len(serv_cards)-1],player,n,order,i,card1_no,computer,tern)):
            if len(serv_cards)!=0:
                card1_no=checkAnotherOption(serv_cards[len(serv_cards)-1],card1_no,player[i])
            return card1_no
    return -1



def checkAnotherOption(serv_card,card_no,List):				#choose most optimal option to win game(number checking)
    res0=serv_card.split('_')
    color=res0[0]
    for cno in range(len(List)):
        res=List[cno].split("_")
        if res[0]==color and res[1].isdigit():
            card_no=cno
    return card_no
    

def chooseColor(player,i):				#choose color by comp
    color=[]
    for cr in player[i]:
        res2=cr.split('_')
        color.append(res2[0])
        cl=most_frequent(color)
        print(cl)
        return cl

def most_frequent(List): 				#choose color which is most frequent
    counter = 0
    color = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            color = i 
    return color
  


    
def checkMatchning(card1,card2,player,n,order,i,card_number,computer,tern):  #card is matching or not
    res1=card1.split('_')
    res2=card2.split('_')
    if res1 == res2:
        return True
    elif res1[0]==res2[0]:
        checkAction(res1,order,i,player,n,card_number,computer,tern)
        return True
    elif res1[1]==res2[1]:
        checkAction(res1,order,i,player,n,card_number,computer,tern)
        return True
    else:
        return False




def drawTwo(player,i,n):
    if i>=n-1:												#if i points to last location
        player[0].append(random.choice(list(final_desk)))
        player[0].append(random.choice(list(final_desk)))
        print("2 card draw")
    else:
        player[i].append(random.choice(list(final_desk)))
        player[i].append(random.choice(list(final_desk)))
        print("2 card draw")


def wild(i,card_number,computer,tern,player):			#if wild card
    print("tern {}".format(tern))
    if tern=='H':
        print("choose color:")
        print("     R->RED")
        print("     Y->YELLOW")
        print("     G->GREEN")
        print("     B->.BLUE")
        color=input("Enter color")
    else:
        color=chooseColor(player,i)
        print("color= {}".format(color))
    player[i][card_number]='{}_wild'.format(color)

def checkAction(res1,order,i,player,n,card_number,computer,tern):
    if res1[1]=="Reverse"  and (order==0 or order==10):				#if reverse card or reserse order going on
        if i==0:
            serv_cards.append(player[i][card_number])				#add card in serv card
            player[i].remove(player[i][card_number])				#remove card form player
            if tern=='H':											#human tern
                Order(player,n,1,n,computer,'H')
            elif tern=='C':											#computer tern
                Order(player,n,1,n,computer,'C')
            else:
                Order(player,n,1,n,computer,tern)    
        else:
            serv_cards.append(player[i][card_number])
            player[i].remove(player[i][card_number])
            if tern=='H':
                Order(player,n,1,i-1,computer,'H')
            elif tern=='C':
                Order(player,n,1,i-1,computer,'C')
            else:
                Order(player,n,1,i-1,computer,tern)
    elif res1[1]=="Reverse" and order==1:
        if i==n:
           serv_cards.append(player[i][card_number])
           player[i].remove(player[i][card_number])
           if tern=='H':
                Order(player,n,0,0,computer,'H')
           elif tern=='C':
                Order(player,n,0,0,computer,'C')
           else:
                Order(player,n,0,0,computer,tern)
        else:
            serv_cards.append(player[i][card_number])
            player[i].remove(player[i][card_number])
            if tern=='H':
                Order(player,n,1,i+1,computer,'H')
            elif tern=='C':
                Order(player,n,1,i+1,computer,'C')
            else:
                Order(player,n,1,i+1,computer,tern)
        
    elif res1[1]=="DrawTwo" and (order==0 or order==10):				#if draw 2 card
        drawTwo(player,i+1,n)
    elif res1[1]=="DrawTwo" and order==1:
        drawTwo(player,i-1,n)
    elif res1[1]=="Wild":
        if tern=='C':
            res1[0]=wild(i,card_number,computer,'H',player)
        else:
            res1[0]=wild(i,card_number,computer,'C',player)
    elif res1[1]=="WildDrawFour":
        
        if order==0 or order==10:
            drawTwo(player,i+1,n)
            drawTwo(player,i+1,n)
        elif order==1:
            drawTwo(player,i-1,n)
            drawTwo(player,i-1,n)
    elif res1[1]=="Skip":
        if i==0 and (order==0 or order==10): 
            serv_cards.append(player[i][card_number])
            player[i].remove(player[i][card_number])
            if tern=='H':
                Order(player,n,order,i+2,computer,'H')
            elif tern=='C':
                Order(player,n,order,i+2,computer,'C')
            else:
                Order(player,n,order,i+2,computer,tern)
        elif i==0 and order==1:
            serv_cards.append(player[i][card_number])
            player[i].remove(player[i][card_number])
            
            if tern=='H':
                Order(player,n,order,n-1,computer,'H')
            elif tern=='C':
                Order(player,n,order,n-1,computer,'C')
            else:
                Order(player,n,order,n-1,computer,tern)
        elif i==n and order==1:
            serv_cards.append(player[i][card_number])
            player[i].remove(player[i][card_number])
            
            
            if tern=='H':
                Order(player,n,order,n-2,computer,'H')
            elif tern=='C':
                Order(player,n,order,n-2,computer,'C')
            else:
                Order(player,n,order,n-2,computer,tern)
        elif i==n and (order==0 or order==10):
            serv_cards.append(player[i][card_number])
            player[i].remove(player[i][card_number])
            
            if tern=='H':
                Order(player,n,order,1,computer,'H')
            elif tern=='C':
                Order(player,n,order,1,computer,'C')
            else:
                Order(player,n,order,1,computer,tern)
        elif order==0 or order==10:
            serv_cards.append(player[i][card_number])
            player[i].remove(player[i][card_number])
            
            
            if tern=='H':
                Order(player,n,order,i+2,computer,'H')
            elif tern=='C':
                Order(player,n,order,i+2,computer,'C')
            else:
                Order(player,n,order,i+2,computer,tern)
        else :
            serv_cards.append(player[i][card_number])
            player[i].remove(player[i][card_number])
            
            if tern=='H':
                Order(player,n,order,i-2,computer,'H')
            elif tern=='C':
                Order(player,n,order,i-2,computer,'C')
            else:
                Order(player,n,order,i-2,computer,tern)
    return res1[0]

    
    
    
    

red_desk=(['R_1','R_2','R_3','R_4','R_5','R_6','R_7','R_8','R_9','R_Reverse','R_DrawTwo','R_Wild','R_WildDrawFour','R_Skip'])
yellow_desk=(['Y_1','Y_2','Y_3','Y_4','Y_5','Y_6','Y_7','Y_8','Y_9','Y_Reverse','Y_DrawTwo','Y_Wild','Y_WildDrawFour','Y_Skip'])
Green_desk=(['G_1','G_2','G_3','G_4','G_5','G_6','G_7','G_8','G_9','G_Reverse','G_DrawTwo','G_Wild','G_WildDrawFour','G_Skip'])
blue_desk=(['B_1','B_2','B_3','B_4','B_5','B_6','B_7','B_8','B_9','B_Reverse','B_DrawTwo','B_Wild','B_WildDrawFour','B_Skip'])

serv_cards=[]
final_desk= red_desk+yellow_desk+Green_desk+blue_desk			#add all the cards
print("                               .SYS                   ")
print("1.Play with human")
print("2.play with computer (only 2) ")
choice=int(input("Enter choice:"))
if choice==1:
    n=int(input("Enter no of player"))
    no_of_cards=int(input("enter initial number of cards"))
    player=[]
    for i in range(0,n):
        sample=random.sample(final_desk,no_of_cards)			#randomly select any card from set
        player.append(sample) 
    
    Order(player,n,10,0,0,'H')
else:
    no_of_cards=int(input("enter initial number of cards"))
    player=[]
    for i in range(0,2):
        final_desk=list(final_desk)
        sample=random.sample(final_desk,no_of_cards)
        final_desk=set(final_desk)-set(sample)
        player.append(list(sample)) 
    final_desk=Order(player,2,10,0,1,'C')
    
    

    