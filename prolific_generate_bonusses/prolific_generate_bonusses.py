"""This file downloads a given dataset from mongoDB, pulls the data, applies a function to the data that returns False/True on whether a participant is bonussed and spits out correctely formatted data to a csv file.

How to use this?
Simply call `get_bonuses_from_mongo`. It takes:
* `db`: the database to use
* `collection`: the collection to use
* `iteration`: the specific iteration of the experiment to use
* `bonus_function`: the function to use to generate the bonus. This is specific to your experiment. It takes an input the subset of the data corresponding to one game and returns `False` (or 0) if that game does not get a bonus or a dollar amount if it does.
* `bonus_function_params` (optional): a dictionary of named parameters to pass to the bonus function. E.g. `{'threshold':0.5,'bonus':2.34}`


Please make sure that you have a SSH tunnel to cogtoolslab.org by running `ssh -fNL 27017:127.0.0.1:27017 USERNAME@cogtoolslab.org` in your shell.

You will also need `auth.txt` with the password for mongoDB user `sketchloop` in the same directory as this file.
"""

import pymongo as pm
import pandas as pd
import numpy as np
import sys
import pyperclip # needed to copy directly to clipboard

def get_data(db, collection, iteration):
    try:
        # this auth.txt file contains the password for the sketchloop user
        auth = pd.read_csv('auth.txt', header=None)
    except FileNotFoundError:
        print('auth.txt not found. Please create a file named auth.txt with the password for the sketchloop user.')
        sys.exit()
    pswd = auth.values[0][0]
    user = 'sketchloop'
    host = 'cogtoolslab.org'  # experiment server ip address

    try:
        conn = pm.MongoClient('mongodb://sketchloop:' + pswd + '@127.0.0.1')
        db = conn[db]
    except:
        raise 'Could not connect to database. Try to set up ssh bridge to write to mongodb. Insert your username. If you dont have an SSH secret set yet, run `ssh -fNL 27017:127.0.0.1:27017 USERNAME@cogtoolslab.org` in your shell.'
    coll = db[collection]
    # might take a long time
    coll_df = pd.DataFrame(coll.find())
    # get iteration
    df = pd.DataFrame(coll_df[coll_df['iterationName'] == iteration])
    # since we use inconstistent naming for prolificID, gameID, we need to be smart about it
    global PROL_ID
    PROL_ID = 'prolificID'
    global GAME_ID
    GAME_ID = 'gameID'
    if "ProlificID" in df.columns:
        PROL_ID = 'ProlificID'
    elif "prolific_ID" in df.columns:
        PROL_ID = 'prolific_ID'
    if "GameID" in df.columns:
        GAME_ID = 'GameID'
    elif "game_ID" in df.columns:
        GAME_ID = 'game_ID'
    return df

def get_bonusses(df, bonus_function, bonus_function_params=()):
    """Given a dataframe, apply the bonus function to every participants"""
    bonusses = {}
    for game in df[GAME_ID].unique():
        try: 
            prolific_id = df[df[GAME_ID] == game][PROL_ID].values[0]
        except:
            print('No prolificID for game {}'.format(game))
            continue
        if prolific_id is not None and prolific_id is not np.nan: # skip missing prolific IDs
            bonus = bonus_function(df[df[GAME_ID] == game],**bonus_function_params)
            if bonus: bonusses[prolific_id] = bonus # don't save if False (ie. no bonus paid)
    return bonusses
    
def get_bonus_string(bonusses):
    """Convert a bonus to a string"""
    return '\n'.join(['{},{}'.format(k,v) for k,v in bonusses.items()])

def get_bonusses_from_mongo(db, collection, iteration, bonus_function, bonus_function_params={}):
    """Get bonusses from mongoDB"""
    df = get_data(db, collection, iteration)
    print('Downloaded {} participants'.format(df[PROL_ID].nunique()))
    bonusses = get_bonusses(df, bonus_function, bonus_function_params)
    bonus_string = get_bonus_string(bonusses)
    # save to clipboard
    pyperclip.copy(bonus_string)
    print('Bonusses copied to clipboard')
    # save to file
    filename = '_'.join([db, collection, iteration])+'_bonusses.csv'
    with open(filename, 'w') as f:
        f.write(get_bonus_string(bonusses))
    print('Bonusses saved to file under', filename)


def acc_bonus_function(participant_df,bonus=1.5,threshold=0.5):
    """Sample bonus function. Returns $1.5 if accuracy is above 50%"""
    assert participant_df[GAME_ID].nunique() == 1, "Not just 1 game passed"
    if participant_df.agg("correct").mean() > threshold:
        return bonus
    else:
        return False

def comprehension_bonus_function(participant_df,bonus=1.5):
    """Sample bonus function. Returns bonus if participant failed to complete the comprehension check"""
    assert participant_df[GAME_ID].nunique() == 1, "Not just 1 game passed"
    if 'training_trials' not in participant_df['eventType'].values:
        return bonus
    else:
        return False
