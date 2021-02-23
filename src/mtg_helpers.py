
def dict_peek(dict, types):
    """
    Overview
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

if __name__ == __main__
    pass