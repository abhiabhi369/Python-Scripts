import pandas as pd
import numpy as np

from workflow.task.task_mgr import Task


@Task(name='Medicare_Coverage_30Months', description='Provide task desc', params={})
def base_custom(pdf: pd.DataFrame, params, cfg):
  today = pd.to_datetime('09-15-2021')
  if len(pdf.BUSINESS_MODEL.tolist()) > 0:
    business_model = int(pdf.BUSINESS_MODEL.tolist()[0])
    pdf['MEDICARE_COVERAGE_30MONTHS'] = np.where((business_model < 3) | (business_model > 6), 0,
                                                 np.where(((today.year - pd.to_datetime(
                                                   pdf['INITIAL_COVERAGE_DATE']).dt.year) * 12 +
                                                           (today.month - pd.to_datetime(
                                                             pdf['INITIAL_COVERAGE_DATE']).dt.month) > 30),
                                                          1, 2))
    pdf['EXISTING_MEDICARE_COVERAGE_30MONTHS'] = np.where((business_model < 3) | (business_model > 6), 0,
                                             np.where(((today.year - pd.to_datetime(
                                                 pdf['EXISTING_COB_INITIAL_COVERAGE_DATE']).dt.year) * 12 +
                                                       (today.month - pd.to_datetime(
                                                           pdf['EXISTING_COB_INITIAL_COVERAGE_DATE']).dt.month) > 30),
                                                      1, 2))
    return pdf
