import pandas as pd
import numpy as np


def create_example_df(low=100, high=50000, size=100):
    df = pd.DataFrame({'Customer': [f'Customer{i+1}' for i in range(size)],
                       'Value': np.random.randint(low=low, high=high, size=size)})

    return df


if __name__ == '__main__':
    df = create_example_df()
    print(df.head())
