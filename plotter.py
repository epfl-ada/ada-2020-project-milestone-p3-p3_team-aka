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
    
    print(res.summary())
    
    coeffs= res.params.values
    time_coef= coeffs[2]
    intervention_coef= coeffs[1]
    post_slope_coef= coeffs[3]
    intercept= coeffs[0]
    
    
    views_pre_int_first_month= intercept + time_coef * 1
    views_pre_int_last_month= intercept + time_coef * (shift_intervention-1)
    
    post_slope_first_month_post= data.set_index("time").loc[shift_intervention, "post_slope"]
    post_slope_last_month_post= data.set_index("time").loc[shift_end_month, "post_slope"]
    
    views_post_int_first_month= intercept + time_coef * shift_intervention + intervention_coef + post_slope_coef * post_slope_first_month_post  
    views_post_int_last_month= intercept + time_coef * shift_end_month + intervention_coef + post_slope_coef * post_slope_last_month_post   

    fig= plt.figure(figsize=(14,9))
    plt.scatter(x="time", y="pageviews", data=data,figure=fig, color="black")
    plt.plot([1,shift_intervention-1], [views_pre_int_first_month, views_pre_int_last_month], figure=fig, color="darkgreen")
    plt.plot([shift_intervention,shift_end_month], [views_post_int_first_month, views_post_int_last_month], figure=fig, color="lightgreen")

    plt.vlines(x=shift_intervention-0.5, ymin=0, ymax=7e+06)