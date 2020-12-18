from prepare_regression import *
import statsmodels.formula.api as smf

#This function takes data , the minimum allowed window between the start and end of the period studied, the minum allowed window between the start and the intervention, fits the regression and returns important relevant events that can be confounders

def confounder_founder(data, start_end_window, start_inter_window):
    
    start_index = 18
    end_index = 48
    
    rg = range(start_index, end_index) 
    for start in rg: 
        for end in rg:
            if end - start < start_end_window:
                continue;
        
            for inter in range (start,end): 
                if inter - start < start_inter_window or end - inter < start_inter_window:
                    continue;
            
        
                relevant= prepare_data_for_regression_with_window(data, start,end,inter)
                model = smf.ols('pageviews ~ time + C(intervention) + post_slope', data=relevant)
                res = model.fit()
                if res.rsquared>0.5:
                    print("start at "+ str(start))
                    print("intervention at "+ str(inter))
                    print("end at "+ str(end))
                    print(res.rsquared)