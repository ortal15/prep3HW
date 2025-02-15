'''פצל את הטבלה שלעיל לכמה טבלאות שונות בצורה הטובה ביותר )מנורמלת(
'וכו NOT NULL ,UNIQUE ,PK FK -ב השתמש :רמז
כתוב שאילתת CREATE לכל טבלה'''

'''- כתוב שאילתות INSERT לכל טבלה בכדי להכניס את המידע'''


def create_table():
    import os
    import sqlite3

    if os.path.exists("prep3.db"):
        os.remove("prep3.db")
    else:
        print("The file does not exist")
    conn = sqlite3.connect('prep3.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY,       
    hosting_country TEXT NOT NULL,        
    country_language TEXT NOT NULL,         
    country_capital TEXT NOT NULL         
    );
    ''')
    cursor.execute('''CREATE TABLE eurovision_competitions (
    competition_id INTEGER PRIMARY KEY,  
    competition_year INTEGER NOT NULL,     
    hosting_country_id INTEGER NOT NULL,   
    winning_country_id INTEGER NOT NULL,   
    FOREIGN KEY (hosting_country_id) REFERENCES countries(country_id),   
    FOREIGN KEY (winning_country_id) REFERENCES countries(country_id)   
    );
    ''')
    cursor.execute('''CREATE TABLE eurovision_songs (
    song_id INTEGER PRIMARY KEY,         
    song_name TEXT NOT NULL,               
    song_language TEXT NOT NULL,           
    singer TEXT NOT NULL,                  
    competition_id INTEGER NOT NULL,       
    FOREIGN KEY (competition_id) REFERENCES eurovision_competitions(competition_id) 
    );
    ''')
    conn.commit()
    conn.close()


def insert_into():
    import sqlite3
    conn = sqlite3.connect('prep3.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO countries (hosting_country, country_language, country_capital) 
    VALUES 
    ('Sweden', 'Swedish', 'Stockholm'),
    ('United Kingdom', 'English', 'London'),
    ('Italy', 'Italian', 'Rome'),
    ('Netherlands', 'Dutch', 'Amsterdam'),
    ('Israel', 'Hebrew', 'Jerusalem'),
    ('Portugal', 'Portuguese', 'Lisbon'),
    ('Ukraine', 'Ukrainian', 'Kyiv'),
    ('Austria', 'German', 'Vienna'),
    ('Denmark', 'Danish', 'Copenhagen'),
    ('Azerbaijan', 'Azerbaijani', 'Baku');
    ''')
    cursor.execute('''INSERT INTO eurovision_competitions (competition_year, hosting_country_id, winning_country_id)
    VALUES 
    (2024, 1, 2),
    (2023, 2, 1),
    (2022, 3, 7),
    (2021, 4, 3),
    (2019, 5, 4),
    (2018, 6, 5),
    (2017, 7, 6),
    (2016, 1, 7),
    (2015, 8, 1),
    (2014, 9, 8),
    (2013, 1, 9),
    (2012, 10, 1);
    ''')
    cursor.execute('''
    INSERT INTO eurovision_songs (song_name, song_language, singer, competition_id)
    VALUES 
    ('The Code', 'English', 'Nemo', 1),
    ('Tattoo', 'English', 'Loreen', 2),
    ('Stefania', 'Ukrainian', 'Kalush Orchestra', 3),
    ('Zitti e buoni', 'Italian', 'Måneskin', 4),
    ('Arcade', 'English', 'Duncan Laurence', 5),
    ('Toy', 'English', 'Netta', 6),
    ('Amar pelos dois', 'Portuguese', 'Salvador Sobral', 7),
    ('1944', 'English/Ukrainian', 'Jamala', 8),
    ('Heroes', 'English', 'Måns Zelmerlöw', 9),
    ('Rise Like a Phoenix', 'English', 'Conchita Wurst', 10),
    ('Only Teardrops', 'English', 'Emmelie de Forest', 11),
    ('Euphoria', 'English', 'Loreen', 12);
    ''')
    conn.commit()
    conn.close()
