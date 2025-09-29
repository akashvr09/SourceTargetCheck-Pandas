import pandas as pd

set_options = {'display.max_columns': None, 'display.max_rows': None, 'display.width': 1000}
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

def file_read(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.parquet'):
        df = pd.read_parquet(file_path)
    else:
        raise ValueError("Unsupported file format")
    # print(df)
    return df


def count_check(source, target):
    source_df = file_read(source)
    target_df = file_read(target)
    source_count = source_df.shape[0]
    target_count = target_df.shape[0]
    if source_count == target_count:
        print('both source and target match')
    else:
        print('source and target do not match and difference is:', source_count - target_count)
        # raise ValueError('source and target do not match')
    return source_count, target_count

# Example usage:
source_path = input("Enter source file path: ")
target_path = input("Enter target file path: ")
count_check(source_path, target_path)


print("Source and Traget file  successfully read")

