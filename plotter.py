import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd

# This function can be used to fit a linear regression model and to plot the segmented regression 
# The inputs shift_intervention and shift_end_month must be a the intervention month index and end month index relative to the 
# start month
def plotter(data, shift_intervention, shift_end_month):
    
    #fitting regression model
    model =smf.ols('pageviews ~ time + C(intervention) + post_slope', data=data)
    res = model.fit()
    
    #print the summary of the regression model
    print(res.summary())
    
    #retrieving the coefficients of each parameter
    coeffs= res.params.values
    time_coef= coeffs[2]
    intervention_coef= coeffs[1]
    post_slope_coef= coeffs[3]
    intercept= coeffs[0]
    
    #computing the limits of the regression line for the pre intervention period
    views_pre_int_first_month= intercept + time_coef * 1
    views_pre_int_last_month= intercept + time_coef * (shift_intervention-1)
    
    #computing the limits of the regression line for the post intervention period
    post_slope_first_month_post= data.set_index("time").loc[shift_intervention, "post_slope"]
    post_slope_last_month_post= data.set_index("time").loc[shift_end_month, "post_slope"]
    views_post_int_first_month= intercept + time_coef * shift_intervention + intervention_coef + post_slope_coef * post_slope_first_month_post  
    views_post_int_last_month= intercept + time_coef * shift_end_month + intervention_coef + post_slope_coef * post_slope_last_month_post   
    
    #plotting the two regression lines and data points
    fig= plt.figure(figsize=(14,9))
    plt.scatter(x="time", y="pageviews", data=data,figure=fig, color="black")
    plt.plot([1,shift_intervention-1], [views_pre_int_first_month, views_pre_int_last_month], figure=fig, color="darkgreen")
    plt.plot([shift_intervention,shift_end_month], [views_post_int_first_month, views_post_int_last_month], figure=fig, color="lightgreen")
    #adding the vertical line corresponding to the intervention
    plt.vlines(x=shift_intervention-0.5, ymin=0, ymax=7e+06)
    
    #adding labels to the axis
    plt.xlabel("month number")
    plt.ylabel("Page views")
    
    #adding plot title, if provided in the arguments
    if graph_title != None:
        plt.title (graph_title)