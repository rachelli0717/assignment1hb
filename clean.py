import pandas as pd
import os
import sys

def clean_data(input1, input2,output):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    df1 = df1.rename(columns={'respondent_id': 'id'})
    merge_df = pd.merge(df1, df2, on='id')
    cleaned_df = merge_df.dropna()
    s_df = cleaned_df[~cleaned_df['job'].str.contains('Insurance')]
    ss_df = s_df[~cleaned_df['job'].str.contains('insurance')]

    ss_df.to_csv(output, index=False)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python clean.py <input1> <input2> <output>")
        sys.exit(1)
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]

    clean_data(input1, input2, output)

    cleaned = pd.read_csv(output)

    print("Output file shape:", cleaned.shape)

