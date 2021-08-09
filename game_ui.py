from tkinter import *
from tkinter import ttk

import db_operations as db_op

window = Tk()
window.title("Welcome to Fantasy Cricket Game!!")
window.geometry('840x700')

##### GLOBAL VARIABLES##########
bat = StringVar()
bat.set('0')

bow = StringVar()
bow.set('0')

allr = StringVar()
allr.set('0')

wkeep = StringVar()
wkeep.set('0')

pts_a = StringVar()
pts_a.set('1000')

pts_u = StringVar()
pts_u.set('0')

pts = StringVar()
pts.set('0')

enter_team_name_var = StringVar()
team_name_var = StringVar()
team_players_list_var = StringVar()

player_selection_var = IntVar()
choose_player_list_var = StringVar()

evaluate_players_list_var = StringVar()
evaluate_points_list_var = StringVar()

team_combo = StringVar()
match_combo = StringVar()

team={
    'team_name':"",
    'players':"",
    'value':0
}
team_players =[]


####################################################################################################

def main_window(window):
        
    #################### TEAM MANAGEMENT MENU #########################


    menubar = Menu(window) 

    team_menu = Menu(menubar, tearoff=0) 

    team_menu.add_command(label="NEW Team", command=create_team_name)  
    team_menu.add_command(label="OPEN Team",command=lambda:[open_team_menu(team)])  
    team_menu.add_command(label="SAVE Team", command=lambda: [save_team(team)])
    select_team_options = db_op.select_team_options()  
    team_menu.add_command(label="EVALUATE Team", command=lambda: [evaluate_team_window(select_team_options)]) 

    menubar.add_cascade(label="Manage Teams", menu=team_menu)  
    window.config(menu=menubar)

    ############################################ SELECTIONS ################################################

    selections_frame = Frame(window, bg="#DBDBDB", width="780", height="100").place(x="25", y="15") 
    
    your_selections = Label(window, text = "Your Selections",bg="#DBDBDB",font=("Comic Sans MS", 12)).place(x = 30,y = 20)

    batsmen = Label(window, text = "Batsmen (BAT) ", bg="#DBDBDB", font=("Comic Sans MS", 10)).place(x = 30,y = 50)  
    bowlers = Label(window, text = "Bowlers (BOW) ", bg="#DBDBDB", font=("Comic Sans MS", 10)).place(x = 200,y = 50)  
    all_rounders = Label(window, text = "Allrounders (AR) ", bg="#DBDBDB", font=("Comic Sans MS", 10)).place(x = 400,y = 50)  
    wicket_keepers = Label(window, text = "Wicket-keeper (WK) ", bg="#DBDBDB", font=("Comic Sans MS", 10)).place(x = 600,y = 50)  

    num_of_batsmen = Label(window, textvariable = bat, fg="#3AB7BB", bg="#DBDBDB", font=("Comic Sans MS", 10)).place(x = 150,y = 50)  
    num_of_bowlers = Label(window, textvariable = bow, fg="#3AB7BB", bg="#DBDBDB",  font=("Comic Sans MS", 10)).place(x = 350,y = 50)  
    num_of_all_rounders = Label(window, textvariable = allr, fg="#3AB7BB", bg="#DBDBDB", font=("Comic Sans MS", 10)).place(x = 550,y = 50)  
    num_of_wicket_keepers = Label(window, textvariable = wkeep, fg="#3AB7BB", bg="#DBDBDB", font=("Comic Sans MS", 10)).place(x = 750,y = 50)  


    ############################################### POINTS #######################################
    points_available = Label(window, text = "Points Available ",  font=("Comic Sans MS", 15)).place(x = 45,y = 150)  
    points_used = Label(window, text = "Points Used ",  font=("Comic Sans MS", 15)).place(x = 425,y = 150) 

    num_of_pts_a = Label(window, textvariable = pts_a, fg="#3AB7BB",  font=("Comic Sans MS", 15)).place(x = 230,y = 150)  
    num_of_pts_u = Label(window, textvariable = pts_u, fg="#3AB7BB",   font=("Comic Sans MS", 15)).place(x = 575,y = 150)

    ################################### PLAYERS LIST BASED ON CATEGORY ########################

    choose_player_listbox = Listbox(window, width="60", height="25", listvariable=choose_player_list_var)
    choose_player_listbox.place(x="45", y="250")   
    choose_player_listbox.bind('<Double-1>', make_team)
    
    choose_bat = Radiobutton(window, text="BAT", font=("Comic Sans MS", 12), variable=player_selection_var, value=1, command=show_players).place(x="55", y="210")
    choose_bow = Radiobutton(window, text="BOW", font=("Comic Sans MS", 12), variable=player_selection_var, value=2,  command=show_players).place(x="125", y="210")
    choose_alr = Radiobutton(window, text="AR", font=("Comic Sans MS", 12), variable=player_selection_var, value=3,  command=show_players).place(x="205", y="210")
    choose_wkeep = Radiobutton(window, text="WK", font=("Comic Sans MS", 12), variable=player_selection_var, value=4, command=show_players).place(x="275", y="210")

   
    ############################## TEAMS ##########################################
    
    teams_listbox = Listbox(window, width="60", height="25", listvariable=team_players_list_var)
    teams_listbox.place(x="425", y="250")
    
    team_name_label = Label(window, text = "Team Name ", font=("Comic Sans MS", 12)).place(x = 425 ,y = 210) 
    team_name_val = Label(window, textvariable = team_name_var, fg="#3AB7BB", font=("Comic Sans MS", 12)).place(x = 530,y = 210)  
    

    ####################### MAKE TEAMS ##############################################
    

def enter_team_name_popupwin():

    top_level_win = Toplevel(window)
    top_level_win.geometry("400x150")

    enter_name_lable = Label(top_level_win, text = "Enter your team name...", font=("Comic Sans MS", 10)).place(x = 120,y = 20) 
    enter_name_input = Entry(top_level_win, textvariable = enter_team_name_var).place(x = 130, y = 50)

    button= Button(top_level_win, text="Create Team", command=lambda: [get_team_name(), top_level_win.destroy()]).place(x = 150, y = 100)

    

def get_team_name():
    team_name = enter_team_name_var.get()
    team_name_var.set(team_name)
    

def create_team_name():
    team_name = enter_team_name_popupwin()    
    return team_name
 

db_bat, db_bow, db_ar, db_wk = db_op.select_players()

db_bat_list=db_bat
db_bow_list=db_bow
db_ar_list=db_ar
db_wk_list=db_wk

def show_players(): 
    global db_bat_list, db_bow_list, db_ar_list, db_wk_list   
    ctg_selection = player_selection_var.get() 
    if ctg_selection == 1 :
        choose_player_list_var.set(db_bat_list)
            
    elif ctg_selection == 2 :
        choose_player_list_var.set(db_bow_list)
       
    elif ctg_selection == 3 :
        choose_player_list_var.set(db_ar_list)
        
    elif ctg_selection == 4 :
        choose_player_list_var.set(db_wk_list)
        
count_selected_bat = 0
count_selected_bow = 0
count_selected_ar = 0
count_selected_wk = 0
points_A = 1000
points_U = 0

def update_points(event,team_name,elem_selection, selection_value):  
        global count_selected_bat
        global count_selected_bow
        global count_selected_ar
        global count_selected_wk
        global points_A
        global points_U

        global db_bat_list, db_bow_list, db_ar_list, db_wk_list

        if(len(elem_selection)>=0 and points_A>0):       
            
            ctg_selection = player_selection_var.get() 
            player_points = db_op.select_players_points(selection_value[0]) 
           
            if ctg_selection==1 and  player_points[0][0]< points_A:

                count_selected_bat = count_selected_bat + 1
                points_A = points_A - player_points[0][0]
                points_U = points_U + player_points[0][0]

                #set value in UI 
                bat.set(count_selected_bat)
                pts_a.set(points_A)
                pts_u.set(points_U)

                #Remove from listbox                               
                db_bat_list.remove(selection_value)
                event.widget.delete(elem_selection)

                # Team Player list     
                team_players.append(selection_value)
                team_players_list_var.set(team_players)

                # Team Dict
                team['team_name'] = team_name
                team['players'] = team_players
                team['value'] = points_U

                event.widget.delete(elem_selection)

            elif ctg_selection==2 and player_points[0][0]< points_A:

                count_selected_bow = count_selected_bow + 1
                points_A = points_A - player_points[0][0]
                points_U = points_U + player_points[0][0]

                #set value in UI
                bow.set(count_selected_bow)
                pts_a.set(points_A)
                pts_u.set(points_U)

                #Remove from listbox                               
                db_bow_list.remove(selection_value)
                event.widget.delete(elem_selection)

                # Team Player list     
                team_players.append(selection_value)
                team_players_list_var.set(team_players)

                # Team Dict
                team['team_name'] = team_name
                team['players'] = team_players
                team['value'] = points_U


               

            elif ctg_selection==3 and player_points[0][0]< points_A:

                count_selected_ar = count_selected_ar + 1
                points_A = points_A - player_points[0][0]
                points_U = points_U + player_points[0][0]

                #set value in UI
                allr.set(count_selected_ar)
                pts_a.set(points_A)
                pts_u.set(points_U) 

                #Remove from listbox                               
                db_ar_list.remove(selection_value)
                event.widget.delete(elem_selection)

                # Team Player list     
                team_players.append(selection_value)
                team_players_list_var.set(team_players)

                # Team Dict
                team['team_name'] = team_name
                team['players'] = team_players
                team['value'] = points_U

                

            elif  ctg_selection==4 and player_points[0][0]< points_A:               

                if count_selected_wk < 1: 

                    count_selected_wk = count_selected_wk + 1                   
                    points_A = points_A - player_points[0][0]
                    points_U = points_U + player_points[0][0]

                    #set value in UI
                    wkeep.set(count_selected_wk)
                    pts_a.set(points_A)
                    pts_u.set(points_U)

                    #Remove from listbox                               
                    db_wk_list.remove(selection_value)
                    event.widget.delete(elem_selection)

                    # Team Player list     
                    team_players.append(selection_value)
                    team_players_list_var.set(team_players)

                    # Team Dict
                    team['team_name'] = team_name
                    team['players'] = team_players
                    team['value'] = points_U
                    
                else:
                    top_level_win = Toplevel(window)
                    top_level_win.geometry("350x60")  
                    enter_name_lable = Label(top_level_win, text = "You cannot select more than one Wicket-Keeper !", font=("Comic Sans MS", 10)).place(x = 40,y = 20)
            
                
                 

def make_team(event):
    team_name = team_name_var.get()

    if team_name!="":        
        elem_selection = event.widget.curselection()

        index = elem_selection[0]
        
        if(index>=0): 
            selection_value = event.widget.get(index)           

            update_points(event,team_name, elem_selection, selection_value)   


def save_team(team):
    player = []
    if len(team) != 0:        
        for value in team['players']:            
            for ele in value:               
                player.append(ele)

        players_joined_string = ",".join(player)

        print(players_joined_string)

        name=team['team_name']
        players=players_joined_string
        value=team['value']

        # INSERT INTO teams DB Table 
        db_op.insert_into_teams_table(name, players, value)

        top_level_win = Toplevel(window)
        top_level_win.geometry("350x60")  
        enter_name_lable = Label(top_level_win, text = "Your team is saved successfully !", font=("Comic Sans MS", 10)).place(x = 70,y = 20)
    else:
        top_level_win = Toplevel(window)
        top_level_win.geometry("350x60")  
        enter_name_lable = Label(top_level_win, text = "There is NO Team to save !", font=("Comic Sans MS", 10)).place(x = 70,y = 20)

# db_team = db_op.select_team(team_name)


def evaluate_team_window(select_team_options):
    
    top_level_win = Toplevel(window)
    top_level_win.geometry("780x550")

    # widow label
    evaluate_label = Label(top_level_win, text = "Evaluate the performance of your Fantasy Team", font=("Comic Sans MS", 10)).place(x = 250,y = 20)

    select_team = ttk.Combobox(top_level_win, width = 27, textvariable = team_combo)
    select_team.place(x = 75, y = 60)

    team_name_options=[]
    for i in select_team_options:
        team_name_options.append(i[0])

    
    # Adding combobox drop down list for teams    
    select_team['values'] = team_name_options        
    
    select_team.current(0)

    select_team.bind('<<ComboboxSelected>>', show_team_players)

    # Adding combobox drop down list for teams
    select_match = ttk.Combobox(top_level_win, width = 27, textvariable = match_combo)
    select_match.place(x = 475, y = 60)

    # Adding combobox drop down list
    select_match['values'] = ['Match 1']    
    
    select_match.current(0)

    select_match.bind('<<ComboboxSelected>>', select_match)

    # separator
    separator = ttk.Separator(top_level_win, orient='horizontal')
    separator.place(relx=0.1, rely=0.2, relwidth=0.75, relheight=0.8)

    #labels
    evaluate_players_label = Label(top_level_win, text = "Players ",  font=("Comic Sans MS", 12)).place(x = 45,y = 120)  
    evaluate_points_label = Label(top_level_win, text = "Points ",  font=("Comic Sans MS", 12)).place(x = 400,y = 120) 

    points = Label(top_level_win, textvariable = pts, fg="#3AB7BB",  font=("Comic Sans MS", 12)).place(x = 500,y = 120)  
    
    # players listbox  
    evaluate_players_listbox = Listbox(top_level_win, width="50", height="20", listvariable=evaluate_players_list_var)
    evaluate_players_listbox.place(x="45", y="150")   

    # points listbox
    evaluate_points_listbox = Listbox(top_level_win, width="50", height="20", listvariable=evaluate_points_list_var)
    evaluate_points_listbox.place(x="400", y="150")

    # calculate score
    button= Button(top_level_win, text="Calculate Score", command=lambda: [cal_score()]).place(x = 345, y = 500)


players=[]
players_points=[]
batting_points = 0
bowling_points = 0
fielding_points = 0
total_player_points = 0
total_team_points = 0


def select_match(event):
    global selected_match
    match_combo.set(event.widget.get())

def show_team_players(event):
    print(match_combo)

    if match_combo!="":

        selected_team = event.widget.get()
        team_players_to_evaluate = db_op.select_team_players_to_evaluate(selected_team)

        # team players
        for player in team_players_to_evaluate[0]:        
            players.append(player.split(","))

        evaluate_players_list_var.set(players[0]) 
    

def cal_score():
    global players
    global players_points

    evaluate_player_point_list =[]

    evaluate_player_point={
        'player_name':"",
        'total_points':0
    }

    global batting_points
    global bowling_points
    global fielding_points
    global total_player_points
    global total_team_points

    #respective team player point
    for player_name in players[0]:  

        player_match_data = db_op.select_match_data(player_name)
        player_stats_data = db_op.select_stats_data(player_name)

        scored, faced, fours, sixes, bowled, maiden, given, wkts, catches, stumping, ro = player_match_data[0]
        value, matches, runs, hundreds, fifties = player_stats_data[0]

        batting_points = batting_points + 0.5*scored 

        if(fifties>0):
            batting_points = batting_points + 5
        if(hundreds>0):
            batting_points = batting_points + 5
        if (scored>80 and scored<100) or (faced>80 or faced<100):
            batting_points = batting_points + 2
        if(scored>100 or faced>100):
            batting_points = batting_points + 4
        if(fours>0):
            batting_points = batting_points + 1
        
        bowling_points = 10*wkts

        fielding_points = 10*(catches + stumping + ro)

        total_player_points = (batting_points + bowling_points + fielding_points)
        
        total_team_points = total_team_points + total_player_points
        
        players_points.append(total_team_points)

        evaluate_player_point['player_name']=player_name
        evaluate_player_point['total_points']= fielding_points

        evaluate_player_point_list.append(evaluate_player_point)

   
    evaluate_points_list_var.set(players_points)
    pts.set(total_team_points)


if __name__ == "__main__":
   
    main_window(window)
    window.mainloop()
