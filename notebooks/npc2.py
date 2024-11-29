import tabula
import pandas as pd
from itertools import count


def myDropna(df: pd.DataFrame) -> pd.DataFrame:
    """Dropping NaNs from column with index 5.
    Created only for map purpose.
    Args:
        df (pd.DataFrame): DataFrame
    Returns:
        pd.DataFrame: DataFrame without NaNs
    """
    return df.dropna(subset = [5])


def extract_from_pdf(df: pd.DataFrame, i: int):
    """Extract data from pdf and save them to csv in a long format.
    Args:
        df (pd.DataFrame): DataFrame
        i (int): Counter for file naming convention
    Returns:
        pd.DataFrame: Final DataFrame
    """
    df[0] = df[0].fillna(method = 'ffill', axis = 0)
    df[3] = df[3].fillna(method = 'ffill', axis = 0)

    # long format
    df = df.melt(id_vars=[0, 3, 5],
                 value_vars=[6, 7, 8, 9, 10, 11, 12, 13, 14])

    df.columns = ['Exposure medium', 'Concentration (vol%)', 'Temperature (C)',
                  'Polymer', 'Qualitative result']

    df['Polymer'].replace({6: 'PVC', 7: 'CPVC', 8: 'HDPE', 9: 'Polypropylene',
                           10: 'PVDF', 11: 'ECTFE', 12: 'ETFE',
                           13: 'FEP', 14: 'PFA'}, inplace=True)

    df = df.assign(Trade_name=lambda dataframe:
                   dataframe['Polymer'].map(
                    lambda Polymer: 'PE 50' if Polymer == 'HDPE' else
                    ('Sygef' if Polymer == 'PVDF' else '')))

    df = df.rename(columns={'Trade_name': 'Trade name'})

    # these should be args to the function for every pdf
    # they are declared in __main__
    df['DP ID'] = '18'
    df['Note'] = ''
    df['Report no.'] = ''
    df['Report source'] = rep_source
    df['Report name'] = rep_name

    df = df[cols]

    df.to_csv(f'data2/dlfa_page{i}.csv', sep = ',')

    return df


if __name__ == "__main__":

    file = "DLFA_Chemical Resistance Thermoplastics.pdf"
    tables = tabula.read_pdf(file, pages = "all", multiple_tables = True, pandas_options = {'header': None})

    rep_name = file[5:]
    rep_source = 'DLFA'
    mats = ['PVC', 'CPVC', 'HDPE', 'Polypropylene', 'PVDF', 'ECTFE', 'ETFE',
            'FEP', 'PFA']
    trade_names = ['', '', 'PE 50', '', 'Sygef', '', '', '', '']

    cols = ['DP ID', 'Trade name', 'Polymer', 'Exposure medium',
            'Concentration (vol%)', 'Temperature (C)', 'Qualitative result',
            'Note', 'Report no.', 'Report source', 'Report name']
    measurments = [154, 297, 330, 442, 495, 530, 551, 574, 596, 621, 643, 665,
                   686, 709, 732]
    measurments_2 = [x+30 for x in measurments]
    dfs = tabula.read_pdf(file, columns = measurments_2,
                          guess = False, pages='6',
                          pandas_options = {'header': None},
                          area = [112, 27, 478, 770])

    dfs = dfs[5:138]
    dfs2 = list(map(myDropna, dfs))

    # i, l can be changed
    for i, l in zip(count(start = 138, step = 1), dfs2[138]):
        extract_from_pdf(l, i)
