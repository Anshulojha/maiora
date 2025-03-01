import pandas as pd
import sqlite3

def extract_data(file_path):
    return pd.read_csv(file_path)

# Function to transform data
def transform_data(df, region):
    df['total_sales'] = df['QuantityOrdered'] * df['ItemPrice']
    df['region'] = region
    df['net_sale'] = df['total_sales'] - df['PromotionDiscount']
    df = df.drop_duplicates(subset='OrderId')
    df = df[df['net_sale'] > 0]
    return df

# Function to load data into SQLite database
def load_data(df, db_name='sales_data.db'):
    conn = sqlite3.connect(db_name)
    df.to_sql('sales_data', conn, if_exists='replace', index=False)
    conn.close()

# Main ETL process
def etl_process():
    # Extract
    df_a = extract_data('sales_region_a.csv')
    df_b = extract_data('sales_region_b.csv')
    
    # Transform
    df_a = transform_data(df_a, 'A')
    df_b = transform_data(df_b, 'B')
    
    # Combine data
    df_combined = pd.concat([df_a, df_b], ignore_index=True)
    
    # Load
    load_data(df_combined)

# Run the ETL process
etl_process()
