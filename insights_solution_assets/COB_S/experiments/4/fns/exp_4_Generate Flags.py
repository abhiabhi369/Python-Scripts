import numpy as np
import pandas as pd

from workflow.task.task_mgr import Task


@Task(name='Generate Flags', description='Provide task desc', params={})
def base_custom(pdf: pd.DataFrame, params, cfg):
    today = pd.to_datetime('09-15-2021')
    pdf['EMPLOYER_FLAG'] = np.where(pdf['EMPLOYER_NAME'].notna(), 1, 0)
    pdf['GROUP_FLAG'] = pdf[['GROUP_NUMBER', 'GROUP_NAME']].any(axis=1).astype(int)
    pdf['EXISTING_GROUP_FLAG'] = np.where(pdf['EXISTING_COB_GROUP_NAME'].notna(), 1, 0)
    pdf['SUBSCRIBER_DOB'] = pdf['DOB']
    pdf['SUBSCRIBER_EMPLOYMENT_STATUS'] = pdf['EMPLOYMENT_STATUS']
    # pdf['SUBSCRIBER_EMPLOYMENT_STATUS'] = np.where(
    #     (pdf['MEMBER_ID'].values == pdf['SUBSCRIBER_ID'].values) | (~pdf['SUBSCRIBER_ID'].isin(pdf['MEMBER_ID'])),
    #     pdf['EMPLOYMENT_STATUS'],
    #     pdf['EMPLOYMENT_STATUS'].where(pdf['SUBSCRIBER_ID'].map(dict(zip(pdf['MEMBER_ID'], pdf['EMPLOYMENT_STATUS']))))
    # )
    pdf['SUBSCRIBER_GENDER'] = pdf['GENDER']
    pdf['SUBSCRIBER_MARITAL_STATUS'] = pdf['MARITAL_STATUS']
    pdf["COVERAGE_START"] = np.where(
        (pd.to_datetime(pdf.INITIAL_COVERAGE_DATE) < pd.to_datetime(pdf.EXISTING_COB_INITIAL_COVERAGE_DATE)), 1,
        2)

    pdf["EXISTING_COB_INITIAL_COVERAGE_DATE"] = np.where((pdf.INITIAL_COVERAGE_DATE == 1), 2, 1)
    pdf['EXISTING_COVERAGE_FLAG'] = np.where(
        (pd.to_datetime(pdf.EXISTING_COB_CURRENT_COVERAGE_START_DATE) <= today)
        & (pd.to_datetime(pdf.EXISTING_COB_COVERAGE_EXPIRED_DATE) >= today), 1, 0)
    pdf['COBRA_FLAG'] = np.where(
        (pd.to_datetime(pdf.COBRA_START_DATE) <= today) & (pd.to_datetime(pdf.COBRA_END_DATE) >= today), 1, 0)
    pdf['ESRD_COORDINATION_FLAG'] = np.where(
        (pd.to_datetime(pdf.ESRD_COORDINATION_PERIOD_START_DATE) <= today)
        & (pd.to_datetime(pdf.ESRD_COORDINATION_PERIOD_END_DATE) >= today), 1, 0)
    pdf['COVERAGE_OVERLAP_FLAG'] = np.where(
        (pd.to_datetime(pdf.COVERAGE_OVERLAP_START_DATE) <= today)
        & (pd.to_datetime(pdf.COVERAGE_OVERLAP_END_DATE) >= today), 1, 0)
    pdf['COVERAGE_FLAG'] = np.where((pd.to_datetime(pdf.CURRENT_COVERAGE_START_DATE) <= today)
                                    & (pd.to_datetime(pdf.COVERAGE_EXPIRED_DATE) >= today), 1, 0)
    pdf["SUBSCRIBER_BIRTH_FIRST"] = np.where(
        pd.to_datetime(pdf['SUBSCRIBER_DOB'], dayfirst=False) == pd.to_datetime(
            pdf['EXISTING_COB_SUBSCRIBER_DOB'], dayfirst=False), 0,
        np.where(pd.to_datetime(pdf['SUBSCRIBER_DOB'], dayfirst=False) >= pd.to_datetime(
            pdf['EXISTING_COB_SUBSCRIBER_DOB'], dayfirst=False), 1,
                 2))
    return pdf
