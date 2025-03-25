import pandas as pd
import numpy as np

from workflow.task.task_mgr import Task


@Task(name='Handle Required Columns Primacy', description='Provide task desc', params={})
def base_custom(pdf: pd.DataFrame, params, cfg):
  req_cols = [
          "SUBSCRIBER_OR_DEPENDENT_INDICATOR",
    "MEMBER_ID",
          "RELATIONSHIP",
          "GENDER",
          "MARITAL_STATUS",
          "STATE",
          "EMPLOYER_SIZE",
          "BUSINESS_MODEL",
          "REASON_FOR_MEDICARE_ENTITLEMENT",
          "FUNDING_MODEL",
          "EMPLOYMENT_STATUS",
          "NOT_SUBJECT_TO_COB_INDICATOR",
          "NOT_SUBJECT_TO_COB_REASON",
          "EXISTING_COB_MEMBER_EMPLOYMENT_STATUS",
          "EXISTING_COB_SUBSCRIBER_EMPLOYMENT_STATUS",
          "EXISTING_COB_RELATIONSHIP",
          "EXISTING_COB_BUSINESS_MODEL",
          "EXISTING_COB_INITIAL_COVERAGE_DATE",
          "COB_STATE",
          "EMPLOYER_FLAG",
          "GROUP_FLAG",
          "EXISTING_GROUP_FLAG",
          "SUBSCRIBER_EMPLOYMENT_STATUS",
          "SUBSCRIBER_GENDER",
          "SUBSCRIBER_MARITAL_STATUS",
          "COVERAGE_START",
          "EXISTING_COVERAGE_FLAG",
          "COBRA_FLAG",
          "ESRD_COORDINATION_FLAG",
          "COVERAGE_OVERLAP_FLAG",
          "COVERAGE_FLAG",
          "MEDICARE_COVERAGE_30MONTHS",
          "EXISTING_MEDICARE_COVERAGE_30MONTHS",
          "SUBSCRIBER_BIRTH_FIRST",
          "COVERAGE_TYPE_1",
          "COVERAGE_TYPE_AL",
          "COVERAGE_TYPE_88",
          "COVERAGE_TYPE_MH",
          "COVERAGE_TYPE_35",
          "COVERAGE_TYPE_98",
          "COVERAGE_TYPE_47",
          "COVERAGE_TYPE_UC",
          "COVERAGE_TYPE_52",
          "COVERAGE_TYPE_33",
          "EXISTING_COB_COVERAGE_TYPE_1",
          "EXISTING_COB_COVERAGE_TYPE_AL",
          "EXISTING_COB_COVERAGE_TYPE_MH",
          "EXISTING_COB_COVERAGE_TYPE_88",
          "EXISTING_COB_COVERAGE_TYPE_35",
          "EXISTING_COB_COVERAGE_TYPE_98",
          "EXISTING_COB_COVERAGE_TYPE_47",
          "EXISTING_COB_COVERAGE_TYPE_UC",
          "EXISTING_COB_COVERAGE_TYPE_52",
          "EXISTING_COB_COVERAGE_TYPE_33",
          "DOB_IS_ADULT",
          "DOB_IS_SENIOR_CITIZEN",
          "DOB_IS_MINOR",
          "EXISTING_COB_DOB_IS_SENIOR_CITIZEN",
          "EXISTING_COB_DOB_IS_ADULT",
          "EXISTING_COB_DOB_IS_MINOR",
          "SUBSCRIBER_DOB_IS_ADULT",
          "SUBSCRIBER_DOB_IS_SENIOR_CITIZEN",
          "SUBSCRIBER_DOB_IS_MINOR",
          "EXISTING_COB_SUBSCRIBER_DOB_IS_SENIOR_CITIZEN",
          "EXISTING_COB_SUBSCRIBER_DOB_IS_ADULT",
          "EXISTING_COB_SUBSCRIBER_DOB_IS_MINOR",
    "PAYER_PRIMACY",
        ]
  unknown_cols = list(set(req_cols).symmetric_difference(set(pdf.columns)))
  for col in unknown_cols:
      pdf[col] = np.zeros(len(pdf))
  maintain_list = list(req_cols)
  pdf = pdf[maintain_list]
  return pdf