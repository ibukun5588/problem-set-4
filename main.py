'''
- You will run Problem Set 4 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5
import os

def main():

    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()

    # Update with felony charge dataframe for p4
    felony_charge = part4.create_felony_charge_df(arrest_events)
    pred_universe = part4.merge_with_felony_charge(pred_universe, felony_charge)

    ##  PART 2: PLOT EXAMPLES  ##
    os.makedirs('./data/part2_plots', exist_ok=True)

    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    os.makedirs('./data/part3_plots', exist_ok=True)

    # 1. Generate a bar plot for the fta column
    part3.bar_plot_fta(pred_universe)
    

    # 2. Generate a bar plot for the fta column, with hue by sex
    part3.bar_plot_fta_by_sex(pred_universe)
    

    # 3. Plot a histogram of age_at_arrest
    part3.histogram_age(pred_universe)
    
    # 4. Plot the histogram of age_at_arrest with custom bins
    part3.histogram_age_bins(pred_universe)
    

   ##  PART 4: CATEGORICAL PLOTS  ##
    os.makedirs('./data/part4_plots', exist_ok=True)

    # 1. Generate a categorical plot for felony rearrest prediction
    part4.plot_felony_rearrest_catplot(pred_universe)
    print("The first plot shows that the model predicts a much higher chance of felony rearrest for those with a felony charge compared to those with a misdemeanor charge. This suggests the model is focusing heavily on the severity of the current charge when predicting future risks.")

    # 2. Generate a categorical plot for nonfelony rearrest prediction
    part4.plot_nonfelony_rearrest_catplot(pred_universe)
    print("In the second plot, the model still assigns higher risks to those with felony charges even when predicting nonfelony rearrests, though the difference isn't as drastic. This might indicate the model's overall bias towards associating higher risk with more severe charges.")

    # 3. Generate a categorical plot for felony rearrest prediction with hue
    part4.plot_felony_rearrest_with_hue(pred_universe)
    print("The third plot, with hues showing actual rearrests, reveals that even those who weren't rearrested for a felony still had a higher predicted probability if they were originally charged with a felony. This suggests the model might overestimate risk based on initial charges, potentially leading to biased predictions.")

    # Answer the question about prediction probabilities
    print("The model predicting higher risks for people with a felony charge who didn't reoffend, compared to those with a misdemeanor who did, shows a possible bias. It suggests the model may be putting too much weight on the severity of the initial charge rather than the actual likelihood of reoffending.")

    ##  PART 5: SCATTERPLOTS  ##
    os.makedirs('./data/part5_plots', exist_ok=True)

    # 1. Generate scatter plot for prediction for felony vs prediction for nonfelony
    part5.scatter_felony_vs_nonfelony(pred_universe)

    # 2. Generate scatter plot for prediction for felony rearrest vs actual felony rearrest
    part5.scatter_felony_vs_actual(pred_universe)

    # 3. Generate scatter plot for prediction for felony vs prediction for nonfelony but it's hued by actual felony rearrest
    part5.scatter_felony_vs_nonfelony_hue_rearrest(pred_universe)
    print("The model seems biased, giving higher risk predictions to those with felony charges who didn’t reoffend, while underestimating those with misdemeanors who did.")
    print("This suggests the model might be focusing too much on the severity of the initial charge instead of the actual likelihood of reoffending.")



if __name__ == "__main__":
    main()
