# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
    songplay_id serial PRIMARY KEY, 
    start_time time, 
    user_id int NOT NULL, 
    level text, 
    song_id text NOT NULL, 
    artist_id text NOT NULL, 
    session_id text, 
    location text, 
    user_agent text)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
    user_id int PRIMARY KEY, 
    first_name text, 
    last_name text,
    gender text, 
    level text)
""")


song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
    song_id text PRIMARY KEY, 
    title text, 
    artist_id text, 
    year int, 
    duration numeric)
""")



artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
    artist_id text PRIMARY KEY,
    name text,
    location text, 
    latitude numeric,
    longitude numeric)
""")

    
#I had to remove the primary key at start_time because there are multiple values for in this column.
time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
    start_time time,
    hour int, 
    day int, 
    week int,
    month int,
    year int,
    weekday text)
""")



# INSERT RECORDS

#SELECT song_id, artists.artist_id, duration FROM songs JOIN artists ON songs.artist_id = artists.artist_id
songplay_table_insert = ("""INSERT INTO songplays( start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                                            VALUES( %s, %s, %s, %s, %s, %s, %s, %s)ON CONFLICT (songplay_id) DO NOTHING """) 


user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level)VALUES(%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level""")

song_table_insert = ("""INSERT INTO songs(song_id,title,artist_id,year,duration)VALUES(%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING""")

artist_table_insert = ("""INSERT INTO artists(artist_id,name,location, latitude,longitude)VALUES(%s, %s, %s, %s, %s) ON CONFLICT(artist_id) DO NOTHING""")

time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday)VALUES(%s, %s, %s, %s,%s, %s, %s)""")

# FIND SONGS


#song_select = ("""SELECT song_id, artist_id FROM songs""")
# case 1: Select by song, artist, and duration
song_select = ("""
     SELECT s.song_id, s.artist_id
     FROM songs s 
         INNER JOIN artists a ON s.artist_id = a.artist_id
     WHERE s.title = %s AND a.name = %s AND s.duration = %s;
 """)
# case 2: Select by song and artist
# song_select = ("""
#     SELECT s.song_id, s.artist_id
#     FROM songs s 
#         INNER JOIN artists a ON s.artist_id = a.artist_id
#     WHERE s.title = %s AND a.name = %s;
# """)
# case 3: Select by song
# song_select = ("""
#     SELECT s.song_id
#     FROM songs s
#     WHERE s.title = %s;
# """)
# case 4: Select by artist
#song_select = ("""
#    SELECT a.artist_id
#    FROM artists a
#    WHERE a.name = %s;
#""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
insert_table_queries= [songplay_table_insert,user_table_insert,song_table_insert,artist_table_insert,time_table_insert]

