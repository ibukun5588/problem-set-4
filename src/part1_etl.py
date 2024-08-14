'''
PART 1: ETL
- This code sets up the datasets for Problem Set 4
- NOTE: You will update this code for PART 4: CATEGORICAL PLOTS
'''

import pandas as pd

def extract_transform():
    """
    Extracts and transforms data from arrest records for analysis

    Returns:
        - `pred_universe`: The dataframe containing prediction-related data for individuals
        - `arrest_events`: The dataframe containing arrest event data
        - `charge_counts`: A dataframe with counts of charges aggregated by charge degree
        - `charge_counts_by_offense`: A dataframe with counts of charges aggregated by both charge degree and offense category
    """
    # Extracts arrest data CSVs into dataframes
    pred_universe = pd.read_csv('https://www.dropbox.com/scl/fi/a2tpqpvkdc8n6advvkpt7/universe_lab9.csv?rlkey=839vsc25njgfftzakr34w2070&dl=1')
    arrest_events = pd.read_csv('https://www.dropbox.com/scl/fi/n47jt4va049gh2o4bysjm/arrest_events_lab9.csv?rlkey=u66usya2xjgf8gk2acq7afk7m&dl=1')

    # Creates two additional dataframes using groupbys
    charge_counts = arrest_events.groupby(['charge_degree']).size().reset_index(name='count')
    charge_counts_by_offense = arrest_events.groupby(['charge_degree', 'offense_category']).size().reset_index(name='count')

    # Work for part 4r
    # Include charge_degree in the felony_charge dataframe
    felony_charge = arrest_events.groupby('arrest_id').apply(
        lambda df: pd.Series({
            'has_felony_charge': df['charge_degree'].str.contains('F').any(),
            'charge_degree': df['charge_degree'].iloc[0]  # Include the charge_degree column
        })
    ).reset_index()

    # Merge with pred_universe
    pred_universe = pd.merge(pred_universe, felony_charge, on='arrest_id', how='left')

    # Create the actual_felony_rearrest column based on y_felony
    pred_universe['actual_felony_rearrest'] = pred_universe['y_felony'].apply(lambda x: True if x == 1 else False)

    return pred_universe, arrest_events, charge_counts, charge_counts_by_offense