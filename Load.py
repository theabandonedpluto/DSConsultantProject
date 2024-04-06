import pandas as pd
import numpy as np

def loadData(df, CorrMatrix, outputFile):
    try:
        with pd.ExcelWriter(outputFile) as writer:
            df.to_excel(writer, sheet_name='HR data', index=False)
            CorrMatrix.to_excel(writer, sheet_name='CorrMatrix')
        return True
    except Exception as e:
        print(f"Error occurred while saving to Excel: {e}")
        return False