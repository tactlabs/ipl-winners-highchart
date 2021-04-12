import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['Teams'].tolist())

    Teams            = df['Teams'].tolist()

    Wins             = df['Wins'].tolist()

    # print(df['quebec'].tolist())

    result_dict = {
        'Teams'            : Teams,
        'Wins'             : Wins
    }

    print(result_dict)

    return result_dict

def add_row(Teams, Wins):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'Teams'       : Teams, 
        'Wins'        : Wins
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()