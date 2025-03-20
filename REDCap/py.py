import AMBRA_Backups
import json
import pandas as pd
from datetime import datetime


# TARGET PROJECT
target_project_name = 'SISTER - Image Tracking'
target_project = AMBRA_Backups.redcap_funcs.get_redcap_project(target_project_name)

# TEST PROJECT
test_project_name = 'Imaging Core - Test'
test_project = AMBRA_Backups.redcap_funcs.get_redcap_project(test_project_name)


all_records = test_project.export_records(format_type='df', export_blank_for_gray_form_status=True)