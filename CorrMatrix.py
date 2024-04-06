import pandas as pd
import numpy as np

def corrMatrix(df):
    df_int = df[[
        'Age','Education',
        # about the job
        'BusinessTravelInt','DistanceFromHome',
        'StockOptionLevel','TotalWorkingYears', 'TrainingTimesLastYear', 
        'YearsAtCompany','YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager','NumCompaniesWorked',
        'JobInvolvement','JobLevel',
        # indicator
        'WorkLifeBalance','JobSatisfaction',
        'MonthlyIncome','PercentSalaryHike',
        # KPI
        'RelationshipSatisfaction','PerformanceRating',
        'EnvironmentSatisfaction',
        'AttritionInt']]
    
    return df_int.corr()