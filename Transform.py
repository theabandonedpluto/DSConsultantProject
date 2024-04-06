import pandas as pd
import numpy as np

class dataTransformation:
    def __init__(self, df):
        self.df = df
    
    def deleteCols(self):
        unncessaryCols = ['DailyRate','HourlyRate','MonthlyRate','Over18','StandardHours']
        self.df.drop(columns = unncessaryCols, inplace=True)

    def addEmployeeCountCol(self):
        self.df['employeeCount'] = 1
    
    def mappingCols(self):
        def mapEducation(value):
            if value == 1:
                return "Below College"
            elif value == 2:
                return "College"
            elif value == 3:
                return "Bachelor"
            elif value == 4:
                return "Master"
            else:
                return "Doctor"

        def mapEnvironmentSatisfaction(value):
            if value == 1:
                return "Low"
            elif value == 2:
                return "Medium"
            elif value == 3:
                return "High"
            else:
                return "Very High"
    
        def mapJobInvolvement(value):
            if value == 1:
                return "Low"
            elif value == 2:
                return "Medium"
            elif value == 3:
                return "High"
            else:
                return "Very High"

                
        def mapJobSatisfaction(value):
            if value == 1:
                return "Low"
            elif value == 2:
                return "Medium"
            elif value == 3:
                return "High"
            else:
                return "Very High"
            
        def mapPerformanceRating(value):
            if value == 1:
                return "Low"
            elif value == 2:
                return "Good"
            elif value == 3:
                return "Excellent"
            else:
                return "Outstanding"

        def mapRelationshipSatisfaction(value):
            if value == 1:
                return "Low"
            elif value == 2:
                return "Medium"
            elif value == 3:
                return "High"
            else:
                return "Very High"
            
        def mapWorkLifeBalance(value):
            if value == 1:
                return "Bad"
            elif value == 2:
                return "Good"
            elif value == 3:
                return "Better"
            else:
                return "best"
            
        def mapBusinessTravel(value):
            if value == "Non-Travel":
                return 1
            elif value =="Travel_Frequently":
                return 2
            else:
                return 3
            
        def mapAttrition(value):
            if value == "Yes":
                return 1
            else:
                return 0
        
        self.df['educationChr'] = self.df['Education'].map(mapEducation)
        self.df['EnvironmentSatisfactionChr'] = self.df['EnvironmentSatisfaction'].map(mapEnvironmentSatisfaction)
        self.df['JobInvolvementChr'] = self.df['JobInvolvement'].map(mapJobInvolvement)
        self.df['JobSatisfactionChr'] = self.df['JobSatisfaction'].map(mapJobSatisfaction)
        self.df['PerformanceRatingChr'] = self.df['PerformanceRating'].map(mapPerformanceRating)
        self.df['RelationshipSatisfactionChr'] = self.df['RelationshipSatisfaction'].map(mapRelationshipSatisfaction)
        self.df['WorkLifeBalanceChr'] = self.df['WorkLifeBalance'].map(mapWorkLifeBalance)
        self.df['BusinessTravelInt'] = self.df['BusinessTravel'].map(mapBusinessTravel)
        self.df['AttritionInt'] = self.df['Attrition'].map(mapAttrition)

    def reorderCols(self):
        self.df = self.df[[
            #about the employee
            'employeeCount','EmployeeNumber','Age','Gender','MaritalStatus','Department',
            'Education','educationChr','EducationField',
            # about the job
            'BusinessTravelInt', 'BusinessTravel','DistanceFromHome',
            'StockOptionLevel','TotalWorkingYears', 'TrainingTimesLastYear', 
            'YearsAtCompany','YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager','NumCompaniesWorked',
            'JobInvolvement','JobInvolvementChr','JobLevel','JobRole',
            # indicator
            'WorkLifeBalance','WorkLifeBalanceChr',
            'JobSatisfaction','JobSatisfactionChr',
            'MonthlyIncome','OverTime', 'PercentSalaryHike',
            # KPI
            'RelationshipSatisfaction','RelationshipSatisfactionChr',
            'PerformanceRating','PerformanceRatingChr',
            'EnvironmentSatisfaction', 'EnvironmentSatisfactionChr',
            'Attrition','AttritionInt']]
        
    def transform(self):
        self.deleteCols()
        self.addEmployeeCountCol()
        self.mappingCols()
        self.reorderCols()
        return self.df
