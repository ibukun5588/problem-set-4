'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd

# Ensure the directory exists
os.makedirs('./data/part4_plots', exist_ok=True)

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do this is that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

def create_felony_charge_df(arrest_events):
    """
    Create a new dataframe with felony charge information for each arrest.

    Parameters:
    - arrest_events: DataFrame containing arrest event data.

    Output:
    - Returns a DataFrame with columns ['arrest_id', 'has_felony_charge'].
    """
    felony_charge = arrest_events.groupby('arrest_id').apply(
        lambda df: pd.Series({
            'has_felony_charge': df['charge_degree'].str.contains('F').any()
        })
    ).reset_index()
    return felony_charge

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe
def merge_with_felony_charge(pred_universe, felony_charge):
    """
    Merge the felony charge dataframe with the pred_universe dataframe.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.
    - felony_charge: DataFrame containing felony charge information.

    Output:
    - Returns a merged DataFrame.
    """
       # Merge the DataFrames
    merged_df = pd.merge(pred_universe, felony_charge, on='arrest_id', how='left')
    
    # Clean up the DataFrame by dropping one of the duplicated 'has_felony_charge' columns
    merged_df.drop(columns=['has_felony_charge_x'], inplace=True)
    merged_df.rename(columns={'has_felony_charge_y': 'has_felony_charge'}, inplace=True)

    return merged_df
##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def plot_felony_rearrest_catplot(pred_universe):
    """
    Creates a categorical plot for felony rearrest prediction.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.

    Output:
    - Saves the plot as 'felony_rearrest_catplot.png'.
    """
    sns.catplot(data=pred_universe, x='charge_degree', y='prediction_felony', kind='bar')
    plt.savefig('./data/part4_plots/felony_rearrest_catplot.png', bbox_inches='tight')
    print("Part 4, Task 1: Felony rearrest catplot created.")

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
def plot_nonfelony_rearrest_catplot(pred_universe):
    """
    Creates a categorical plot for nonfelony rearrest prediction.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.

    Output:
    - Saves the plot as 'nonfelony_rearrest_catplot.png'.
    """
    sns.catplot(data=pred_universe, x='charge_degree', y='prediction_nonfelony', kind='bar')
    plt.savefig('./data/part4_plots/nonfelony_rearrest_catplot.png', bbox_inches='tight')
    print("Part 4, Task 2: Nonfelony rearrest catplot created.")
    # Add your analysis on the difference between these plots here.


# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
def plot_felony_rearrest_with_hue(pred_universe):
    """
    Creates a categorical plot for felony rearrest prediction, with a hue for actual rearrest.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.

    Output:
    - Saves the plot as 'felony_rearrest_with_hue_catplot.png'.
    """
    sns.catplot(data=pred_universe, x='charge_degree', y='prediction_felony', hue='actual_felony_rearrest', kind='bar')
    plt.savefig('./data/part4_plots/felony_rearrest_with_hue_catplot.png', bbox_inches='tight')
    print("Part 4, Task 3: Felony rearrest catplot with hue created.")
    # Add your analysis on the plot here.





# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?