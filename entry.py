# one off code
# populates the emotion database
import sqlite3 as lite
import sys
import pickle

con = lite.connect('affect.db')

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS WordEmotions")
cur.execute("CREATE TABLE IF NOT EXISTS WordEmotions(Id integer PRIMARY KEY, wordName TEXT, emotionName TEXT$

with open('emo_dict','r') as f:
        d=pickle.load(f)
        id=0
        for emo in d:
                for w in d[emo]:
                        #print 'Entering data', w,'--',emo
                        cur.execute("INSERT INTO WordEmotions (wordName, emotionName) VALUES(?,?)", (w, emo))
        con.commit()
        print 'Entry complete..'


if con:
        con.close()

