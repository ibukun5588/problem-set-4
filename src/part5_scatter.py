'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statements when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd

# Ensure the directory exists
os.makedirs('./data/part5_plots', exist_ok=True)


# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
def scatter_felony_vs_nonfelony(pred_universe):
    """
    Creates a scatter plot where the x-axis is 'prediction_felony' and the y-axis is 'prediction_nonfelony', 
    hued by whether the current charge is a felony.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.

    Output:
    - Saves the scatter plot as 'scatter_felony_vs_nonfelony.png'.
    """
    sns.lmplot(data=pred_universe, x='prediction_felony', y='prediction_nonfelony', hue='has_felony_charge', fit_reg=False)
    plt.savefig('./data/part5_plots/scatter_felony_vs_nonfelony.png', bbox_inches='tight')
    print("Part 5, Task 1: Scatter plot of felony vs nonfelony predictions created.")
    print("The dots on the right suggest that high felony predictions often come with high nonfelony predictions, indicating the model treats them similarly.")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def scatter_felony_vs_actual(pred_universe):
    """
    Creates a scatter plot where the x-axis is 'prediction_felony' and the y-axis is 'actual_felony_rearrest'.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.

    Output:
    - Saves the scatter plot as 'scatter_felony_vs_actual.png'.
    """
    sns.scatterplot(data=pred_universe, x='prediction_felony', y='actual_felony_rearrest')
    plt.savefig('./data/part5_plots/scatter_felony_vs_actual.png', bbox_inches='tight')
    print("Part 5, Task 2: Scatter plot of felony prediction vs actual rearrest created.")
    print("The plot suggests the model may not be perfectly calibrated; predictions don’t always align closely with actual rearrests.")

# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
def scatter_felony_vs_nonfelony_hue_rearrest(pred_universe):
    """
    Creates a scatter plot where the x-axis is 'prediction_felony' and the y-axis is 'prediction_nonfelony',
    hued by whether the person was actually rearrested for a felony crime.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.

    Output:
    - Saves the scatter plot as 'scatter_felony_vs_nonfelony_hue_rearrest.png'.
    """
    sns.lmplot(data=pred_universe, x='prediction_felony', y='prediction_nonfelony', hue='actual_felony_rearrest', fit_reg=False)
    plt.savefig('./data/part5_plots/scatter_felony_vs_nonfelony_hue_rearrest.png', bbox_inches='tight')
    print("Part 5, Task 3: Scatter plot of felony vs nonfelony predictions, hued by actual felony rearrest, created.")
    print("Analysis: The plot shows whether higher predictions for felony are associated with actual rearrests, "
          "highlighting how well the model's predictions align with real outcomes.")
 

# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?

print("The model seems biased, giving higher risk predictions to those with felony charges who didn’t reoffend, while underestimating those with misdemeanors who did.")
print("This suggests the model might be focusing too much on the severity of the initial charge instead of the actual likelihood of reoffending.")

