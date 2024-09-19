import pandas as pd
from pandas import DataFrame


def check_and_replace_NaN(data: DataFrame):
    if data.isnull().values.any():
        print("NaN found, replacing NaN with 0.0 in DataFrame.")
        return data.fillna(0.0)
    print("No NaN found in DataFrame.")
    return data

def remove_all_NaN(data: DataFrame):
    if data.isnull().values.any():
        print("Removing all rows with NaN.")
        data_cleaned = data.dropna()
        print(f"DataFrame after removing all NaN rows\n{data_cleaned}")
    else:
      print("No NaN found in DataFrame.")

def sum_columns(data: DataFrame):
    if 'start station id' in data.columns and 'end station id' in data.columns:
        print(data[['start station id', 'end station id']])
        data['total'] = data['start station id'] + data['end station id']
        return data
    raise KeyError("Required columns 'start station id' or 'end station id' not found.")


def sampling_station_start(data: DataFrame):
    if 'start station id' in data.columns:
        duplicates_counts = data['start station id'].value_counts()
        return duplicates_counts[duplicates_counts > 1]
    raise KeyError("Column 'start station id' not found.")


def sampling_station_end(data: DataFrame):
    if 'end station id' in data.columns:
        duplicates_counts = data['end station id'].value_counts()
        return duplicates_counts[duplicates_counts > 1]
    raise KeyError("Column 'end station id' not found.")


def main():
    url = "https://raw.githubusercontent.com/d1mmm/lab1/master/201306-citibike-tripdata.csv"
    data = None
    try:
        data = pd.read_csv(url, encoding='latin-1')
        print(f"All dataframe\n{data}")
    except FileNotFoundError:
        print(f"File not found by {url}")
        return
    except pd.errors.EmptyDataError:
        print("File is empty")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    try:
        print("Remove all NaN data")
        remove_all_NaN(data)

        print("Check dataframe for NaN")
        data = check_and_replace_NaN(data)
        print(data)

        print("Summing start station id and end station id columns")
        data = sum_columns(data)
        print(data)

        print("Sampling of trips starting at the same station")
        counts_start = sampling_station_start(data)
        print(f"Counts of trips starting at the same station: {counts_start}")

        print("Sampling trips that end at the same station")
        counts_end = sampling_station_end(data)
        print(f"Counts of trips ending at the same station: {counts_end}")
    except KeyError as key:
        print(f"KeyError {key}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()