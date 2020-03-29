import pandas as pd


def filter():

    while True:

        postal = input("Please indicate the postal code: ")
        room = input("Please indicate the number of rooms: ")
        break

    return postal, room



def load(postal, room):

    df = pd.read_csv('/home/vincent/Python/Fonciers/valeursfoncieres-2019.txt', sep = '|', thousands=',')

    df_clean = df[['Date mutation','Nature mutation','Valeur fonciere','Code postal','No voie','Type de voie','Voie','Commune','Surface reelle bati','Nombre pieces principales']]
    df_clean['Valeur'] = df['Valeur fonciere'].div(100)
    df_clean['sq_meters'] = df['Valeur fonciere'].div(100) / df['Surface reelle bati']

    df_clean.drop(['Valeur fonciere'],axis=1,inplace=True)
    return df_clean[(df_clean['Code postal'] == postal) & (df_clean['Nombre pieces principales'] == room)]

def stats(df):

    squared_meter = df['Valeur'].sum() / df['Surface reelle bati'].sum()

    return squared_meter

def main():

    postal, room = filter()
    df = load(postal, room)
    squared_meter = stats(df)
    df.to_csv(r'/home/vincent/Python/Fonciers/result.csv', index = False)
    print (df.head())
    print ("Result file saved on the Fonciers folder")
    print ("The average squared meter is {}: ".format(squared_meter))


if __name__ == "__main__":
    main()
