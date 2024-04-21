import pandas as pd
import numpy as np
import Extract
import Transform
import CorrMatrix
import LRModel
import Load

def main():
    # extract
    filepath = "rawdata/DatasetProject_HRAnalytics.xlsx"
    df = Extract.readData(filepath)

    # transform
    transformer = Transform.dataTransformation(df)
    transformedDf = transformer.transform()

    # correlation matrix
    df_corrmatrix = CorrMatrix.corrMatrix(transformedDf)

    # simple LR model
    LRSummaryModel = LRModel.LRModelGenerator(transformedDf)

    # load
    outputFile = 'cleanedData/HRDfFinished.xlsx'
    loadResult = Load.loadData(transformedDf, df_corrmatrix, LRSummaryModel, outputFile)

    if loadResult:
        print('ETL process completed successfully')
    else:
        print('ETL process encountered an error')

if __name__ == '__main__':
    main()







