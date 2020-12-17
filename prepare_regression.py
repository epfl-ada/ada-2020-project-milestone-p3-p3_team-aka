import pandas as pd

#this function takes an index of the starting month, of the ending month and of the intervention month  
#with January 2012 is month 1 and December 2015 is month number 48
#and prepares the data for regression in this specific window 
#returns None if the parameters are incorrect
def prepare_data_for_regression_with_window(data, month_start, month_end, intervention_month):
    
    if month_start> month_end: 
        return None
    if intervention_month<=month_start or intervention_month>= month_end:
        return None
    
    shift_intervention= intervention_month- month_start+1
    
    pageviews_per_month = data.groupby(pd.Grouper(key='date', freq='M')).sum().reset_index()
    pageviews_per_month ['time'] = range(1,len(pageviews_per_month) + 1)
    
    relevant= pageviews_per_month[(pageviews_per_month['time'] >= month_start) & (pageviews_per_month['time'] <= month_end) ]
    relevant['intervention'] = (relevant.time >= intervention_month).astype(int)
    relevant['time'] = relevant['time']-month_start+1
    relevant['post_slope'] = relevant['time'].apply(lambda r: 0 if r < shift_intervention else r - shift_intervention + 1)
    
    return relevant