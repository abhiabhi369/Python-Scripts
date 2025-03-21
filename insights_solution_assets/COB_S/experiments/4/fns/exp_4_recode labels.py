import pandas as pd
 
from workflow.task.task_mgr import Task
 
 
@Task(name='recode labels', description='Provide task desc', params={})
def base_custom(pdf: pd.DataFrame, params, cfg):
    # apply custom logic
    recoding_field = [{'PRIMACY_DETERMINATION_CODE': {"D001": 0, "D002": 1, "D003": 2, "D004": 3, "D008": 4, "D009": 5, "D010": 6, "D011": 7, "U006": 8, "U007": 9, "U021": 10, "U041": 11}}]
    for i in recoding_field:
        pdf = pdf.replace(i)
    return pdf