import pandas as pd
import csv
import logging
import sys
sys.path.append('../')


def transform_raw():
    """
        This function transforms the raw dataset extracted from the web into a form that can be easily loaded the database
        
        Returns: pd.DataFrame 
    """
    raw_data_df= pd.read_csv('../data/20181024_d1_0830_0900.csv')   #Reads the original data into a dataframe

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
    def save(df,filename):
        df.to_csv(filename)

#     def main(fetch_date):
#     data_json = import_data()
#     df = transform_data(data_json)
#     data_to_append = get_new_data(df, fetch_date)
#     save_new_data_to_csv(data_to_append, fetch_date)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--date", required=True, type=str)
#     args = parser.parse_args()
#     main(args.date)
        