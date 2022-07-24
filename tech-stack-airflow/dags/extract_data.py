import argparse
import os
import pandas as pd
import csv
import config
import sys
sys.path.append('../')


def transform_raw_data(filename):
    """
        This function transforms the raw dataset extracted from the web into a dataframe that can be easily loaded the database    
        Returns: pd.DataFrame 
    """
    filepath = os.path.join(config.CSV_FILE_DIR, filename)
    raw_data_df= pd.read_csv(filepath)   #Reads the original data into a dataframe
    #Create empty lists to hold data in each column
    track_ids = []
    vehicle_types = []
    traveled_d = []
    avg_speeds = []
    trajectories = []
    for r in range(len(raw_data_df)): 
        row = raw_data_df.iloc[r,:][0].split(";")
        row_p1 = row[:4]
        row_p2 = row[4:]
        trajectory = ','.join(row_p2)        
        track_ids.append(row_p1[0])
        vehicle_types.append(row_p1[1])
        traveled_d.append(row_p1[2])
        avg_speeds.append(row_p1[3])
        trajectories.append(trajectory[1:])    
    columns = raw_data_df.columns[0].split(";")[:4]
    columns.append("trajectory")
    columns[1] = "vehicle_types"
    for i in range(len(columns)):
        columns[i] = columns[i].strip()
    data_dict= {columns[0]:track_ids, columns[1]:vehicle_types, columns[2]:traveled_d, columns[3]:avg_speeds,columns[4]:trajectory}
    df= pd.DataFrame(data_dict)
    return df

def get_file_path(fetch_date):
    """
    This function constructs a filename to be used 
    Params:
        fetch_date: str
            The date the data was downloaded from the pNeuma API
    Returns:
        filepath: os.Path
            The path to the file
    """
    filename = "traffic_flow_{}.csv".format(fetch_date)
    return os.path.join(config.CSV_FILE_DIR, filename)


def save(data_to_append,fetch_date):
    """
    This function saves the data to a csv file
    Params:
        data_to_append: pd.DataFrame
            A pandas DataFrame containing the data to be saved to the csv
        fetch_date => str
            The date the data was downloaded. This is used to create the filepath
    """
    filename = get_file_path(fetch_date)
    if not data_to_append.empty:
        data_to_append.to_csv(filename, encoding='utf-8', index=False)

def main(filename, fetch_date):
    """
    The entry point to this module. This is the first function that will be called when this module is executed
    Params:
        filename => str
            The name of the file containing the raw data
        fetch_date: str
            The date the data was downloaded from the web
    """
    data_to_append = transform_raw_data(filename)
    save(data_to_append, fetch_date)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, type=str)
    parser.add_argument("--filename", required=True, type=str)
    args = parser.parse_args()
    main(args.filename, args.date)
        