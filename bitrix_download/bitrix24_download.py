import pandas as pd
from requests import get

# insert here the entity names (tables) you want to download
tables = ['crm_deal', 'crm_lead', 'crm_deal_uf']

def ta_bitrix(tables):
    # iterating of the variable "tables"
    for table in tables:
        # printing the table name
        print(f'Table: {table}')
        
        # request, replace # by the variable 
        req = get(f'https://##########.bitrix24.com.br/bitrix/tools/biconnector/pbi.php?token=############&table={table}')
        
        # transforming the JSON into a Pandas Data Frame
        df = pd.DataFrame(req.json())
        
        # renaming the columns using the first row
        df.columns = df.iloc[0]
        
        # dropping the first line, which was used to rename the columns
        df = df.drop(index=df.index[0], axis=0)

        # returning the table as csv
        df.to_csv(f'{table}.csv')

# execute the code
ta_bitrix(tables)