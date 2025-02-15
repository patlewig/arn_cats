arn_cats
==============================

Package to facilitate profiling of chemicals through the ECHA ARN groupings using the Random Forest model developed in Karamertzanis et al. (2024) Systematic Approaches for the Encoding of Chemical Groups: A Case study. Chem. Res. Toxicol. 37, 600-619. The associated repository supporting this publication can be found here  https://github.com/pkaramertzanis/regulatory_grouping/tree/master. Herein we provide a simpler means of applying the best random forest model developed in the study to make grouping assignments for new chemicals. The original functions have been used but restructured in the arn_cats package to facilitate ease of use. 

To get started, either a local installation using `pip install -e .` can be used from the root directory to install the package. 
Alternatively using 
`import sys`
`import os`
`project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))`
`sys.path.insert(0, project_root)`
<br>
in a code block in an IDE such as Jupyter notebook will enable importing of the functions directly. Data files associated with the package are located in `arn_cats/data/` Notebooks in `arn_cats/notebooks` walk through how to recreate the RF model, how to recreate the pickle file of training set molecules and how to apply the model and the applicability domain assessment function for new substances imported as part of a pandas dataframe containing identifiers and SMILES.

Project Organisation
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed    <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         , and a short `-` delimited description, e.g.
    │                         `1.0-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so arn_cats can be imported
    ├── arn_cats                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes arn_cats a Python module
    │   ├── chm         <- Scripts to process molecules and generate fingerprints
    │   │   ├── cheminfo_toolkit.py
    │   │   └── mols.py
    │   ├── data           <- Scripts to import or generate data
    │   │   └── data_load.py
    │   ├── model        <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── build_model.py
    │   │   └── model_domain.py 
    │   ├── utl       <- Scripts for logging
    │   │   └── logger.py
    │   └── visualisation  <- Scripts to create exploratory and results oriented visualisations
    │       
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
