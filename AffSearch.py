import sqlite3 as lite
import sys

def get_emotions(word):

        con = lite.connect('affect.db')
        emoList=[]
        with con:
                print 'Searching word: ', word
                cur = con.cursor()
                cur.execute("SELECT emotionName FROM WordEmotions where wordName=?", (word,))
                rows = cur.fetchall()
                for row in rows:
                        emoList.append(row[0])
        return emoList

