import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# This function can be used to fit a linear regression model and to plot the segmented regression 
# The inputs shift_intervention and shift_end_month must be a the intervention month index and end month index relative to the 
# start month
def plotter(data, graph_title=None):
    
    pageviews= data['pageviews']
    max_pv= pageviews.max()
    
    shift_intervention = data[data.intervention==1]["time"].iloc[0]
    shift_end_month = data.iloc[len(data)-1]['time']
    
    #fitting regression model
    model = smf.ols('pageviews ~ time + C(intervention) + post_slope', data=data)
    res = model.fit()
    
    #print the summary of the regression model
    print(res.summary())
    
    #retrieving the coefficients of each parameter
    coeffs = res.params.values
    time_coef = coeffs[2]
    intervention_coef = coeffs[1]
    post_slope_coef = coeffs[3]
    intercept = coeffs[0]
    
    #computing the limits of the regression line for the pre intervention period
    views_pre_int_first_month = intercept + time_coef * 1
    views_pre_int_last_month = intercept + time_coef * (shift_intervention-1)
    
    #computing the limits of the regression line for the post intervention period
    post_slope_first_month_post = data.set_index("time").loc[shift_intervention, "post_slope"]
    post_slope_last_month_post = data.set_index("time").loc[shift_end_month, "post_slope"]
    views_post_int_first_month = intercept + time_coef * shift_intervention + intervention_coef + post_slope_coef * post_slope_first_month_post  
    views_post_int_last_month = intercept + time_coef * shift_end_month + intervention_coef + post_slope_coef * post_slope_last_month_post   
    
    #plotting the two regression lines and data points
    preds = res.get_prediction(data).summary_frame(alpha=0.05)[['mean_ci_lower', 'mean_ci_upper']]
    xticks = range(1, shift_end_month + 1)
    
    fig = plt.figure(figsize=(14,5))
    plt.scatter(x="time", y="pageviews", data=data,figure=fig, color="black", label="articles")
    plt.plot([1,shift_intervention-1], [views_pre_int_first_month, views_pre_int_last_month], figure=fig, color="darkgreen", label="Trend Pre June 2013")
    plt.plot([shift_intervention,shift_end_month], [views_post_int_first_month, views_post_int_last_month], figure=fig, color="lightgreen", label="Trend Post June 2013")
    #adding the vertical line corresponding to the intervention
    plt.vlines(x=shift_intervention-0.5, ymin=0, ymax=max_pv, ls='--', label="mid June 2013")
    
    #adding labels to the axis
    plt.xlabel("Time (Months)")
    plt.ylabel("Total views")
    plt.xticks(xticks)
    
    plt.fill_between(x=xticks, y1=preds['mean_ci_lower'], y2=preds['mean_ci_upper'],color='g', where=np.array(xticks) <= shift_intervention - 1, alpha=0.5, label= "Confidence interval (95%)")
    plt.fill_between(x=xticks, y1=preds['mean_ci_lower'], y2=preds['mean_ci_upper'],color='g', where=np.array(xticks) > shift_intervention - 1, alpha=0.5)
    plt.legend()
    plt.grid (True, axis='y')
    
    
    #adding plot title, if provided in the arguments
    if graph_title != None:
        plt.title (graph_title)