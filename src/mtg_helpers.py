import pandas as pd
import psycopg2 as psy
from psycopg2 import sql
from io import StringIO
import sqlalchemy
from sqlalchemy import create_engine
import sys

def dict_peek(dict, types):
    """
    Overview:
        quick function for printing out high level details of nested-collections  
    Parameters:
        dict = dictionary for summarizing
        types = list of scalar (non-colection) types to print out values for.  non-listed types will print out collection summary stats

    Returns:
        print out overview of what's in the provided dictionary
    """
    for k, v in dict.items():
        if type(v) in types or v == None:
            length = 'value of ' + str(v)
        else:
            length = 'length of ' + str(len(v))
        print(f'Key {k} has values of {type(v)} type with a {length}')
    
def check_column_completeness(pre_defined_fields, data_set_fields):
    """
    Overview:
        checks the fields within a file being processed against the database schema and returns the status and any identified fields in disconnect.
    Parameters:
        pre_defined_fields: set
            set of columns already defined in the data model for processing a given mtg file type
        data_set_fields: set 
            set of columns in the file being processed

    Returns
        result: string
            either 'missing', 'novel', or 'complete to indicate if the file being processed is missing fields, introduces novel fields, or is complete relative to the existing data model
        result: set
            set of the fields that are different between the file being processed and the existing data model
    """
    pre_d_cols = len(pre_defined_fields)
    data_set_cols = len(data_set_fields)
    if pre_d_cols - data_set_cols > 0:
        print('WARNING - THERE ARE FIELDS MISSING FROM THE CURRENT CARD DATA SET.')
        return 'missing', pre_defined_fields - data_set_fields
    elif pre_d_cols - data_set_cols < 0:
        print('WARNING - THERE ARE NOVEL FIELDS IN THE CURRENT CARD DATA SET.')
        return 'novel', data_set_fields - pre_defined_fields        
    else:
        return 'complete', set()    

def build_combo_data(all_fields, dict_fields, source_df):
    """
    Overview:
        Function for preparing dataframe for loading to sql that contains unused data elements that are not compatible with existing postgresql schema. Simply converts the element to string for no-loss storage to enable future use if needed.
    Parameters:
        all_fields: list
            list of all columns for the given output
        dict_fields: list
            list of all columns for the given output containing the incompatible formats to be converted to string
        source_df: dataframe
            master dataframe containing all data to use the field list parameters to select out of

    Return:
        output_df: dataframe that contains all fields needed for the given table query, with incompatible data element converted to string

    """
    output_df = source_df[all_fields]
    output_df[dict_fields] = output_df[dict_fields].astype(str)
    return output_df

def connect(connection_details):  
    """
    Overview:
        Establishes connection to PostgreSQL database
    Parameters:
        connection_details = dict  
    Returns:
        conn: connection
    """
    conn = None
    try:
        print('Connecting to PostgreSQL database...')
        conn = psy.connect(**connection_details)
    except (Exception, psy.DatabaseError) as error:
        print(f'Unable to connect to the database: {error}')
        sys.exit(1)
    print('Connection successful')
    return conn

def add_new_card_data(conn_details, card_inf_df, table, conn):
    """
    Overview:
        Add's data set from dataframe to table in connected database.  Rollsback if error in loading and prints the error and returns a value for error handling.
    Parameters:
        conn_details: dict
            Connection parameters for establishing sql engine connection
        card_inf_df: dataframe
            Dataset to add to table - assumes schema of dataframe is compatible with schema of target table
        table: str
            name of target table in connected database
        conn: connection
            Active database connection
    Returns:
        int if error, none if no error.
        prints status.
    """
    engine_path = "postgresql+psycopg2://" + conn_details['user'] + ":" + conn_details['password']  
    engine_path +='@localhost:5432/' +conn_details['dbname']
    engine = create_engine(engine_path)
    try:
        card_inf_df.to_sql(table, engine, index=False, if_exists='append')
    except (Exception, psy.DatabaseError) as error:
        print(f'Error: {error}')
        conn.rollback()
        return 1
    conn.commit()
    print(f'Successful updating of {table}')

def add_uuid_to_deck(deck_df, conn, df_name_field):
    """
    Overview
        Looks up uuid from card data set and returns updated deck list dataframe with uuid inserted.
    Parameters
        deck_df: dataframe
            Dataframe containing the deck data without uuid present
        conn: connection
            active connection to the postgresql database
        df_name_field: str
            column name for the decklist dataframe containing the card name for use in matching and uuid retrieval from the postgresql database
    """
    query = sql.SQL("""
        WITH newestsetdate AS (
            SELECT name, MAX(setreleasedate) as max_date
            FROM core
            JOIN setdetails ON "setCode" = "setcode"
            GROUP BY name
            ),
            newestset AS (
            SELECT name, setcode
            FROM newestsetdate
            JOIN setdetails ON newestsetdate.max_date = setdetails.setreleasedate
            )

            SELECT core.uuid, newestset.name
            FROM core
            INNER JOIN newestset ON newestset.name = core.name AND newestset.setcode = core."setCode";""")
    name_id_df = pd.read_sql(query, conn).groupby("name").max() 
    return deck_df.merge(name_id_df, how = 'left', left_on=df_name_field, right_on="name")

    

if __name__ == "__main__":
    pass