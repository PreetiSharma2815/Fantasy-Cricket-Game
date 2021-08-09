import mysql.connector
import db_connection_config as config


def select_players():
    try:
        cnx = mysql.connector.connect(**config.config)
        cursor = cnx.cursor()
        print("Connected to the DATABASE!")

        #QUERY
        select_bat = ("SELECT player from stats where ctg='BAT'")
        select_bow= ("SELECT player from stats where ctg='BWL'")
        select_ar= ("SELECT player from stats where ctg='AR'")
        select_wk= ("SELECT player from stats where ctg='WK'")   

        # EXECUTE 
        cursor.execute(select_bat)
        bat = cursor.fetchall()

        cursor.execute(select_bow)
        bow = cursor.fetchall()

        cursor.execute(select_ar)
        ar = cursor.fetchall()

        cursor.execute(select_wk)
        wk = cursor.fetchall()

        return bat, bow, ar, wk        
       
    except mysql.connector.Error as err:  
        print(err)
    else:
        cursor.close()
        cnx.close()

def select_players_points(player_name):
    try:
        cnx = mysql.connector.connect(**config.config)
        cursor = cnx.cursor()
        print("Connected to the DATABASE!")
        # QUERY
        select_player_value= ("SELECT value from stats where player ='"+ player_name +"'")

        # EXECUTE 
        cursor.execute(select_player_value)
        player_points = cursor.fetchall()       

        return player_points       
       
    except mysql.connector.Error as err:  
        print(err)
    else:
        cursor.close()
        cnx.close()


def insert_into_teams_table(name, players, value):
    try:
        cnx = mysql.connector.connect(**config.config)
        cursor = cnx.cursor()
        print("Connected to the DATABASE!")

        insert_into_teams_query = ("INSERT INTO teams"
                            "(name, players, value) "
                            "VALUES (%s, %s, %s)")

        insert_teams_tb_val = [(name, players, value)]

        # EXECUTE INSERT INTO match
        cursor.executemany(insert_into_teams_query,insert_teams_tb_val)
        cnx.commit()
        print(cursor.rowcount, " row(s) inserted !")
        

    except mysql.connector.Error as err:  
        print(err)
    else:
        cursor.close()
        cnx.close()




def select_team_options():
    try:
        cnx = mysql.connector.connect(**config.config)
        cursor = cnx.cursor()
        print("Connected to the DATABASE!")
        # QUERY
        select_player_value= ("SELECT name from teams")

        # EXECUTE 
        cursor.execute(select_player_value)
        team_name_options = cursor.fetchall()       

        return team_name_options       
       
    except mysql.connector.Error as err:  
        print(err)
    else:
        cursor.close()
        cnx.close()


def select_team_players_to_evaluate(team_name):
    try:
        cnx = mysql.connector.connect(**config.config)
        cursor = cnx.cursor()
        print("Connected to the DATABASE!")
        # QUERY
        select_player_value= ("SELECT players from teams where name ='"+ team_name +"'")

        # EXECUTE 
        cursor.execute(select_player_value)
        team_players = cursor.fetchall()       

        return team_players       
       
    except mysql.connector.Error as err:  
        print(err)
    else:
        cursor.close()
        cnx.close()



def select_stats_data(player_name):
    try:
        cnx = mysql.connector.connect(**config.config)
        cursor = cnx.cursor()
        print("Connected to the DATABASE!")

        select_stats_field_value= ("SELECT value, matches, runs, 100s, 50s from stats where player ='"+ player_name +"'")

        # EXECUTE 
        cursor.execute(select_stats_field_value)
        stats_field_value = cursor.fetchall() 

        return stats_field_value        
       
    except mysql.connector.Error as err:  
        print(err)
    else:
        cursor.close()
        cnx.close()


def select_match_data(player_name):
    try:
        cnx = mysql.connector.connect(**config.config)
        cursor = cnx.cursor()
        print("Connected to the DATABASE!")

        select_match_field_value= ("SELECT scored, faced, fours, sixes, bowled, maiden, given, wkts, catches, stumping, ro from match_data where player ='"+ player_name +"'")
        
        # EXECUTE 
        cursor.execute(select_match_field_value)
        match_field_value = cursor.fetchall() 

        return match_field_value 
             
       
    except mysql.connector.Error as err:  
        print(err)
    else:
        cursor.close()
        cnx.close()