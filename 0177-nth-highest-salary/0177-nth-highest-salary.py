import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Extract distinct salaries in descending order
    sorted_unique = employee['salary'].sort_values(ascending=False).drop_duplicates()
    
    # Return None if N is out-of-range (<=0 or > distinct count)
    if N <= 0 or N > len(sorted_unique):
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    
    # Otherwise, pick the (N‑1)th item
    nth_value = sorted_unique.iloc[N - 1]
    return pd.DataFrame({f"getNthHighestSalary({N})": [nth_value]})
