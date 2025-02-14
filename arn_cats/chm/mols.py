# setup logging
from arn_cats.utl import logger
ort matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
import math
import re
from pathlib import Path
import textwrap
from inspect import getmembers, isfunction
from typing import List
from pickle import dump, load
import zipfile

import pickle

from tqdm import tqdm

from rdkit import Chem
from rdkit.Chem import Fragments
from rdkit.Chem import Draw
from rdkit.Chem import rdFMCS
from rdkit.Chem import rdRGroupDecomposition
from rdkit.Chem import AllChem
from rdkit import DataStructs
from rdkit.DataManip.Metric.rdMetricMatrixCalc import GetTanimotoDistMat

from arn.cats.chm.cheminfo_toolkit import Molecule, Fingerprint_engine

from arn_cats.data.data_load import arn_groups


# read in molecules and put them in a list
molecules = []
for idx, row in arn_groups.iterrows():
    smiles = row['SMILES_DSSTox']
    try:
        mol = Molecule.from_smiles(smiles)
        molecules.append(mol)       
    except Exception as e:
        log.error(e)
with open('molecules_all.pickle', 'wb') as handle:
    pickle.dump(molecules, handle, protocol=pickle.HIGHEST_PROTOCOL)




