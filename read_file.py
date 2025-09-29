import pandas as pd

set_options = {'display.max_columns': None, 'display.max_rows': None, 'display.width': 1000}

def file_read(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.parquet'):
        df = pd.read_parquet(file_path)
    else:
        raise ValueError("Unsupported file format")
    return df

# Example usage:
file_path = input("Enter the file path: ")
# df = file_read('test_excel_file.xlsx')
print(f"{file_path} successfully read")
print(df)
