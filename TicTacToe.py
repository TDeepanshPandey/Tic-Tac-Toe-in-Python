# -*- coding: utf-8 -*-
"""
Milestone Project Tic Tac Toe Game
"""

firstrow = [' ',' ',' '];
secondrow = [' ',' ',' '];
thirdrow = [' ',' ',' '];

def print_tictac():
    print ("\n");
    print ("\t\t\t\t{var1} | {var2} | {var3} ".format(var1=firstrow[0],var2=firstrow[1],var3=firstrow[2]));
    print ("\t\t\t\t----------");       
    print ("\t\t\t\t{var1} | {var2} | {var3} ".format(var1=secondrow[0],var2=secondrow[1],var3=secondrow[2]));
    print ("\t\t\t\t----------");        
    print ("\t\t\t\t{var1} | {var2} | {var3} ".format(var1=thirdrow[0],var2=thirdrow[1],var3=thirdrow[2]));
    print ("\n");       

def turn():
    value = 'X';
    if my_dict[name1] <= my_dict[name2]:
        #print('\nTurn Player1 : %s'%name1);
        my_dict[name1] += 1;
        value = 'X';
    else:
        #print('\nTurn Player2 : %s'%name2);
        my_dict[name2] += 1;
        value = 'O';
    return value;

def curr_player():
    if my_dict[name1] <= my_dict[name2]:
        print('\n\t\tTurn Player1 : %s'%name1);
    else:
        print('\n\t\tTurn Player2 : %s'%name2);
    return True;

def win():
    global winner;
    if firstrow.count('X') == 3 or secondrow.count('X') == 3 or thirdrow.count('X') == 3 :
        winner = name1;
        return False;
    elif firstrow.count('0') == 3 or secondrow.count('0') == 3 or thirdrow.count('0') == 3:
        winner = name2;
        return False;
    elif firstrow.count(' ') == 0 and secondrow.count(' ') == 0 and thirdrow.count(' ') == 0 :
        winner = "None";
        return False;
    elif (firstrow[0] == 'X' and secondrow[0] == 'X' and thirdrow[0] == 'X') or (firstrow[1] == 'X' and secondrow[1] == 'X' and thirdrow[1] == 'X') or (firstrow[2] == 'X' and secondrow[2] == 'X' and thirdrow[2] == 'X'):
        winner = name1;
        return False;
    elif (firstrow[0] == 'O' and secondrow[0] == 'O' and thirdrow[0] == 'O') or (firstrow[1] == 'O' and secondrow[1] == 'O' and thirdrow[1] == 'O') or (firstrow[2] == 'O' and secondrow[2] == 'O' and thirdrow[2] == 'O'):
        winner = name2;
        return False;
    elif (firstrow[0] == 'X' and secondrow[1] == 'X' and thirdrow[2] == 'X') or (firstrow[2] == 'X' and secondrow[1] == 'X' and thirdrow[0] == 'X'):
        winner = name1;
        return False;
    elif (firstrow[0] == 'O' and secondrow[1] == 'O' and thirdrow[2] == 'O') or (firstrow[2] == 'O' and secondrow[1] == 'O' and thirdrow[0] == 'O'):
        winner = name1;
        return False;
    else:
        print ();
    return True;

def play():
    curr_player();
    row = 20
    col = 20
    while(row > 3 and col > 3):
        row = int(input("\t\tEnter the row to input value - "));
        #print row;
        col = int(input("\t\tEnter the column to input value - "));
        #print col;
        if (row > 3 and col > 3):
            print ("\n\n\t\t\t\t\t\tSorry wrong input please try again")
    print ("\t\tYou have choose Row : %s and Column : %s"%(row,col));
    col -= 1;
    check = True;
    if check:
        if 0 < row < 4 and 0 <= col < 3:
            if row == 1 and firstrow[col] == ' ' :
                val = turn();
                firstrow[col] = val;
            elif row == 2  and secondrow[col] == ' ':
                #print 'inside';
                #print secondrow[col];
                val = turn();
                secondrow[col] = val;
            elif row == 3 and thirdrow[col] == ' ':
                val = turn();
                thirdrow[col] = val;
                
            else:
                print ("\n\n\t\t\t\t\t\tSorry the space is already occupied. Try Another Position");
        #if firstrow.count(' ') == 0  and secondrow.count(' ') == 0 and thirdrow.count(' ') == 0 :  
       #     return False;
    check = win();
    return check;
    #print 'Still in function'

#name1 ='Deep';
#name2 ='TDP';
print ("\n\t\t\t\t\t\tWelcome to Tic Tac Toe Game\n");    
user_play = True;
while user_play:
    name1 = input("\t\tEnter First User Name : ");
    name2 = input("\t\tEnter Second User Name : ");
    winner = "None";
    print ('\n\t\tPlayer1: %s \t \t Player2: %s \n'%(name1,name2));
    my_dict={name1:0,name2:0};
    print_tictac();
    print ("\t\t\tOkay, Let's Play\n")
    flag = True;
    while flag:
        flag = play();
        #print flag;
        #print my_dict;
        print_tictac();    
    
    if winner == "None":
        print ("\t\t\t\t\t\tThis Game is a Tie");
    else:
        print ("\t\t\t\t\t\tThe winner of this game is %s"%winner);
    
    ans = input("\t\tWould you like to play again (Y/N) ?  ");
    if (ans == "Yes" or ans == 'Y'):
        user_play = True;
    else:
        user_play = False;
