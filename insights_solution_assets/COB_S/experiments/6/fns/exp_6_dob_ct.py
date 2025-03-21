import pandas as pd
import numpy as np

from workflow.task.task_mgr import Task


@Task(name='dob_ct', description='Provide task desc', params={})
def base_custom(pdf: pd.DataFrame, params, cfg):
  today = pd.to_datetime('09-15-2021')
  def date_of_birth_transform(today, df, keys=[]):
    
     for key in keys:
        
        df[key] = np.where((today.year - pd.to_datetime(df[key], format='%Y%m%d').dt.year) <= 18, "IS_MINOR",                   np.where((today.year - pd.to_datetime(df[key], format='%Y%m%d').dt.year > 18) & (                           today.year - pd.to_datetime(df[key], format='%Y%m%d').dt.year < 66),                            "IS_ADULT", "IS_SENIOR_CITIZEN"))

     return df
  pdf = date_of_birth_transform(today, pdf, ["DOB", "EXISTING_COB_DOB", "SUBSCRIBER_DOB",
                                                            "EXISTING_COB_SUBSCRIBER_DOB"]) 
  return pdf