import sqlite3
from HWprep3_def import create_table, insert_into

create_table()
insert_into()

conn = sqlite3.connect('prep3.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

'''כעת כתוב שאילתת JOIN בין כל הטבלאות כדי לקבל את המידע המלא
)המידע המלא יכיל את כל העמודות כמו בטבלה המקורית ]ויותר[,
אך במקום שהכול יכתב בטבלה אחת, המידע יפוצל כראוי בין טבלאות('''

cursor.execute('''SELECT 
    ec.competition_year,               
    hc.hosting_country,                 
    hc.country_language AS hosting_language,
    hc.country_capital,                 
    wc.hosting_country AS winning_country,  
    wc.country_language AS winning_language, 
    wc.country_capital AS winning_capital,  
    es.song_name,                        
    es.song_language,                
    es.singer                           
FROM 
    eurovision_competitions ec
JOIN 
    countries hc ON ec.hosting_country_id = hc.country_id  
JOIN 
    countries wc ON ec.winning_country_id = wc.country_id 
JOIN 
    eurovision_songs es ON ec.competition_id = es.competition_id
ORDER BY 
    ec.competition_year DESC;  
''')

rows = cursor.fetchall()
for row in rows:
    print(dict(row))
