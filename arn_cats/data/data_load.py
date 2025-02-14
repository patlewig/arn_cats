from pathlib import Path
import pandas as pd
import openpyxl
import pickle
import numpy

arn_path = Path(__file__).parent / "2023_03_24_ARN_grouping.xlsx"
cols_ARN = ['entry ID', 'Group_name_ARN', 'Substance_name_ARN', 'EC_number_ARN', 'CAS_number_ARN']
cols_added = ['DSSTox_ID', 'DSSTox_structure_ID', 'DSSTox_QC_Level', 'Substance_name_DSSTox',
              'CAS_number_DSSTox', 'Substance_type_DSSTox', 'Substance_Note_DSSTox', 'SMILES_DSSTox',
              'InChI_DSSTox', 'InChIKey_DSSTox', 'Formula_DSSTox', 'MolWeight_DSSTox', 'SMILES_2D_QSAR_DSSTox']
arn_groups = pd.read_excel(arn_path,usecols=cols_ARN+cols_added)
arn_groups.insert(1, 'Group_number', arn_groups['Group_name_ARN'].map(pd.Series(data=range(0, arn_groups['Group_name_ARN'].nunique()), index=arn_groups['Group_name_ARN'].drop_duplicates().to_list())))


arn_path2 = Path(__file__).parent / "ARN_groups.xlsx"
arn_groupings = pd.read_excel(arn_path2)

file = Path(__file__).parent / "best_model_rf.pickle"
best_model_rf = pickle.load(open(file,  "rb" ))

file2 = Path(__file__).parent / "molecules_all.pickle"
print(f"Resolved path: {file2.resolve()}")  # Debugging line

with open(file2, "rb") as f:
    molecules = pickle.load(f)
