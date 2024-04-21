from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
import pandas as pd
import numpy as np


def LRModelGenerator(df):
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
    X = df_int.drop('AttritionInt', axis=1)
    y = df_int['AttritionInt']

    X = sm.add_constant(X)

    model = sm.Logit(y, X)
    result = model.fit()

    logRegSummary = pd.read_html(result.summary().tables[1].as_html(),
                                 header =0, index_col=0)[0]
    return logRegSummary
