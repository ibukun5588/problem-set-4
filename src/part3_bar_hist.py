'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ensure the directory exists
os.makedirs('./data/part3_plots', exist_ok=True)

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def bar_plot_fta(pred_universe):
    """
    Creates a bar plot for the 'fta' column.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.

    Output:
    - Saves the bar plot as 'fta_barplot.png'.
    """
    sns.barplot(x='fta', y='count', data=pred_universe.groupby('fta').size().reset_index(name='count'))
    plt.savefig('./data/part3_plots/fta_barplot.png', bbox_inches='tight')
    print("Part 3, Task 1: Bar plot for 'fta' column created.")


# 2. Hue the previous barplot by sex
def bar_plot_fta_by_sex(pred_universe):
    """
    Creates a bar plot for the 'fta' column, with hue by 'sex'.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.

    Output:
    - Saves the bar plot with hue as 'fta_barplot_by_sex.png'.
    """
    sns.barplot(x='fta', y='count', hue='sex', data=pred_universe.groupby(['fta', 'sex']).size().reset_index(name='count'))
    plt.savefig('./data/part3_plots/fta_barplot_by_sex.png', bbox_inches='tight')
    print("Part 3, Task 2: Bar plot for 'fta' column with hue by 'sex' created.")

# 3. Plot a histogram of age_at_arrest
def histogram_age(pred_universe):
    """
    Creates a histogram of 'age_at_arrest'.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.

    Output:
    - Saves the histogram as 'age_histogram.png'.
    """
    sns.histplot(data=pred_universe, x='age_at_arrest')
    plt.savefig('./data/part3_plots/age_histogram.png', bbox_inches='tight')
    print("Part 3, Task 3: Histogram of 'age_at_arrest' created.")


# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def histogram_age_bins(pred_universe):
    """
    Creates a histogram of 'age_at_arrest' with custom bins.

    Parameters:
    - pred_universe: DataFrame containing prediction-related data.

    Output:
    - Saves the histogram with bins as 'age_histogram_bins.png'.
    """
    bins = [18, 21, 30, 40, 100]
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins)
    plt.savefig('./data/part3_plots/age_histogram_bins.png', bbox_inches='tight')
    print("Part 3, Task 4: Histogram with custom bins created.")