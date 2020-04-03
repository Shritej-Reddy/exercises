import sqlite3
import pandas as pd

conn = sqlite3.connect('cricket.db')
c = conn.cursor()



def table_entry():
    c.execute("""CREATE TABLE IF NOT EXISTS cricketers (
        Name text,
        Team text,
        Runs_scored integer,
        Wickets_taken integer
        )""")

    c.execute("INSERT INTO cricketers VALUES ('Sachin', 'India', 15000, 10)")
    c.execute("INSERT INTO cricketers VALUES ('Virat', 'India', 8000, 10)")
    c.execute("INSERT INTO cricketers VALUES ('Murali', 'Srilanka', 2000, 450)")
    c.execute("INSERT INTO cricketers VALUES ('Hayden', 'Australia', 10000, 10)")
    c.execute("INSERT INTO cricketers VALUES ('Kumble', 'India', 2000, 400)")
    c.execute("INSERT INTO cricketers VALUES ('Srinath', 'India', 1000, 300)")
    c.execute("INSERT INTO cricketers VALUES ('Shane', 'Australia', 15000, 400)")
    c.execute("INSERT INTO cricketers VALUES ('Jacques', 'SA', 11500, 200)")
    c.execute("INSERT INTO cricketers VALUES ('Jack', 'England', 5000, 50)")
    c.execute("INSERT INTO cricketers VALUES ('Sydney', 'England', 1000, 100)")
    conn.commit()

def bat_grade(new_runs, team):
    if new_runs > 20000:
        return "Grade A"
    else:
        return "Grade B"

def bowl_grade(new_wickets, team):    
    if new_wickets > 400:
        return "Grade A"
    else:
        return "Grade B"

def input_data():
    print("List of available team names : India, Srilanka, Australia, SA, England")
    team = input("Enter Team Name : ")
    return team

def grading(table_name, team):
    #table_entry()
    c.execute("SELECT Team FROM cricketers WHERE Team=?",(team,))
    a = c.fetchall()
    print(a)
    if not a:
       print("Team not  in table")
    else:
       print("Team in table")

    c.execute("SELECT SUM(DISTINCT Runs_scored) FROM cricketers WHERE TEAM=?",(team,))
    runs = c.fetchone()
    c.execute("SELECT SUM(DISTINCT Wickets_taken) FROM cricketers WHERE TEAM=?",(team,))
    wickets = c.fetchone()
    print(runs)
    print(wickets)
    new_runs = int(''.join(map(str, runs))) 
    new_wickets = int(''.join(map(str, wickets))) 
    conn.close()

    g1 = bat_grade(new_runs, team)
    g2 = bowl_grade(new_wickets, team)
    
    if g1 == "Grade A" and g2 == "Grade A":
        print("Grade A+")
    elif g1 == "Grade A" and g2 == "Grade B" or g2 == "Grade A" and g1 == "Grade B":
        print("Grade A")
    else:
        print("Grade B")

team = input_data()
grading('abc', team)