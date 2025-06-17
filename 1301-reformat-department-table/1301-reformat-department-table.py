import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    department = department.pivot(columns='month',index = 'id',values='revenue')
    cols = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    department = department.reindex(columns = cols)
    department.rename(columns = lambda x: x+'_Revenue',inplace=True)
    return department.reset_index().rename(columns={'index':'id'})