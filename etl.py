import os
import glob
import psycopg2
import pandas as pd
import numpy as np
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Function Name = process_song_file(cur, filepath) 
    InputParameters
    cur: cursor to the database 
    filepath: name of the filepath
    This function loads data into dimension tables songs and artists
    """
    print(process_song_file.__doc__)
    # open song file
    #df =  pd.read_json(filepath, lines=True).replace({pd.np.nan: 0})
    df =  pd.read_json(filepath, lines=True).replace({np.nan: 0})

    # insert song record
    song_data = list(df[['song_id','title','artist_id','year','duration']].values[0])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = list(df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values[0])
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Function Name = process_log_file(cur, filepath) 
    InputParameters
    cur: cursor to the database 
    filepath: name of the filepath
    This function loads valid data into fact table songplays and in dimenstion tables time and users
    """
    # open log file
    #df = pd.read_json(filepath, lines=True).replace({pd.np.nan: 0})
    df = pd.read_json(filepath, lines=True).replace({np.nan: 0})

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    #time_data = pd.Series([t,t.dt.hour,t.dt.day,t.dt.week,t.dt.month,t.dt.year,t.dt.weekday_name]
    #               ,index=['timestamp','hour','day','week','month','year','weekday_name']).to_dict()
    #column_labels = (['timestamp','hour','day','week','month','year','weekday_name'])
    #time_data = [t, t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year, t.dt.dayofweek]
    time_data = [t, t.dt.hour, t.dt.day, t.dt.isocalendar().week, t.dt.month, t.dt.year, t.dt.dayofweek]
    column_labels = ['ts', 'hour', 'day', 'week', 'month', 'year', 'dayofweek']

    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]
    user_df = user_df.drop_duplicates()
    
    #Filter for content in user_df
    #print (user_df)
    #user_df = user_df[user_df['userId'] != '']
    #Change column header names
    user_df.columns = ['user_id', 'first_name', 'last_name', 'gender', 'level']

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        #print (row.song,'-', row.artist,'-', row.length)
        cur.execute(song_select, (row.song, row.artist, row.length))
       
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
            # insert songplay record
            #print ('results = ', results)
            songplay_data = (pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)                    
            cur.execute(songplay_table_insert, songplay_data)
        else:
            songid, artistid = None, None

        


def process_data(cur, conn, filepath, func):
    """ 
    Function Name = process_data(cur, conn, filepath, func) 
    Input Parameters
    cur: cursor to the connections
    conn: database connection
    filepath: path to either song_data or log_data file
    func: name of the function to process different files.
    function names are process_song_file and process_data_file
                    
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    #print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        #print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Main Procedure
    connects to sparkify databse and process song and file date
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()