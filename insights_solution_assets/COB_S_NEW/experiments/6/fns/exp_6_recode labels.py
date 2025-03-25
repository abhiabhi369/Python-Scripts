import pandas as pd
 
from workflow.task.task_mgr import Task
 
 
@Task(name='recode labels', description='Provide task desc', params={})
def base_custom(pdf: pd.DataFrame, params, cfg):
    # apply custom logic
    recoding_field = [{'PAYER_PRIMACY': {1: 0, 2: 1}}]
    for i in recoding_field:
        pdf = pdf.replace(i)
    return pdf