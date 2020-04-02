import pandas as pd
import numpy as np


def filter():

    while True:

        postal = input("Please indicate the postal code: ")
        room = input("Please indicate the number of rooms: ")
        break

    return postal, room



def load(postal, room):

    labels = {"Code service CH":float,"Reference document":float,"1 Articles CGI":float,"2 Articles CGI":float,"3 Articles CGI":float,"4 Articles CGI":float,"5 Articles CGI":float,"No disposition":int,"Date mutation":object,"Nature mutation":object,"Valeur fonciere":float,"No voie":float,"B/T/Q":object,"Type de voie":object,"Code voie":object,"Voie":object,"Code postal":float,"Commune":object,"Code departement":object,"Code commune":int,"Prefixe de section":float,"Section":object,"No plan":int,"No Volume":object,"1er lot":object,"Surface Carrez du 1er lot":float,"2eme lot":object,"Surface Carrez du 2eme lot":float,"3eme lot":object,"Surface Carrez du 3eme lot":float,"4eme lot":float,"Surface Carrez du 4eme lot":float,"5eme lot":float,"Surface Carrez du 5eme lot":float,"Nombre de lots":int,"Code type local":float,"Type local":object,"Identifiant local":float,"Surface reelle bati":float,"Nombre pieces principales":float,"Nature culture":object,"Nature culture speciale":object,"Surface terrain":float}
    df = pd.read_csv('/home/vincent/Python/Fonciers/valeursfoncieres-2019.txt', sep = '|', dtype=labels, thousands=',')
    df.drop_duplicates(inplace=True)

    df['Valeur'] = df.iloc[:,10].div(100)
    df['sq_meters'] = df.iloc[:,10].div(100) / df.iloc[:,38]
    df_clean =df.iloc[:,np.r_[8:10,16,11,13,15,17,38:40,43:45]]


    return df_clean[(df_clean.iloc[:,2]==postal)&(df_clean.iloc[:,8]==room)]


def stats(df):

    squared_meter = df['Valeur'].sum() / df['Surface reelle bati'].sum()

    return squared_meter

def chart(df):
    df.plot(x='Surface reelle bati',y='Valeur',kind='scatter',figsize=(10,10));

def nil_data(df):

    mean = df.mean()
    df.fillna(mean, inplace=True)

def main():

    postal, room = filter()
    df = load(postal, room)
    nil_data(df)
    squared_meter = stats(df)
    df.to_csv(r'/home/vincent/Python/Fonciers/result.csv', index = False)
    print (df.head())
    print ("Result file saved on the Fonciers folder")
    print ("The average squared meter is {}: ".format(squared_meter))
    chart(df)


if __name__ == "__main__":
    main()
