import mysql.connector
import db_connection_config as config


insert_into_match_query = ("INSERT INTO match_data"
                            "(player, scored, faced, fours, sixes, bowled, maiden, given, wkts, catches, stumping, ro) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

insert_match_tb_val = [
  ('Kholi', 102,98,8,2,0,0,0,0,0,0,1),
  ('Yuvraj', 12,20,1,0,48,0,36,1,0,0,0),
  ('Rahane', 49,75,3,0,0,0,0,0,1,0,0),
  ('Dhawan', 32,35,4,0,0,0,0,0,0,0,0),
  ('Dhoni', 56,45,0,1,0,0,0,0,3,2,0),
  ('Axar', 8,4,2,0,48,2,35,1,0,0,0),
  ('Pandya',42,36,3,3,30,0,25,0,1,0,0),
  ('Jadeja', 18,10,1,1,60,3,50,2,1,0,1),
  ('Kedar', 65,60,7,0,24,0,24,0,0,0,0),
  ('Ashwin', 23,42,3,0,60,2,45,6,0,0,0),
  ('Umesh', 0,0,0,0,54,0,50,4,1,0,0),
  ('Bumrah', 0,0,0,0,60,2,49,1,0,0,0),
  ('Bhuwaneshwar', 15,12,2,0,60,1,46,2,0,0,0),
  ('Rohit', 46,65,5,1,0,0,0,0,1,0,0),
  ('Kartick', 29,42,3,0,0,0,0,0,2,0,1)
]

insert_into_stats_query = ("INSERT INTO stats"
                            "(player,value, matches, runs, 100s, 50s, ctg) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)")

insert_stats_tb_val = [
  ('Kholi', 120, 189,8257,28,43,'BAT'),
  ('Yuvraj', 100,86,3589,10,21,'BAT'),
  ('Rahane', 100,158, 5435,11,31,'BAT'),
  ('Dhawan', 85,25,565,2,1,'AR'),
  ('Dhoni', 75,18,2573,3,19,'BAT'),
  ('Axar', 100,67,208,0,0,'BWL'),
  ('Pandya',75,70,77,0,0,'BWL'),
  ('Jadeja', 85,16,1,0,0,'BWL'),
  ('Kedar',90,111,675,0,1,'BWL'),
  ('Ashwin', 100,136,1914,0,10,'AR'),
  ('Umesh',110, 296,6496,10,64,'WK'),
  ('Bumrah', 60,76,1365,0,8,'WK'),
  ('Bhuwaneshwar', 75,17,289,0,2,'AR'),
  ('Rohit', 85,304,8701,14,52,'BAT'),
  ('Kartick', 75,11,111,0,0,'AR')
]



try:
    cnx = mysql.connector.connect(**config.config)
    cursor = cnx.cursor()
    print("Connected to the DATABASE!")

    # EXECUTE INSERT INTO match
    cursor.executemany(insert_into_match_query, insert_match_tb_val)
    cnx.commit()
    print(cursor.rowcount, " rows inserted !")

    # EXECUTE INSERT INTO stats
    cursor.executemany(insert_into_stats_query, insert_stats_tb_val)
    cnx.commit()
    print(cursor.rowcount, " rows inserted !")

except mysql.connector.Error as err:  
    print(err)
else:
    cursor.close()
    cnx.close()
