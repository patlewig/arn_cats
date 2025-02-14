from setuptools import find_packages, setup

setup(
        name="arn_cats", 
        version='0.1.0',
        author="patlewig",
        description='Package to facilitate profiling of chemicals through the ECHA ARN groupings.',
        packages=find_packages(),
        package_data = {'arn_cats':['data/*']},
        install_requires=['pandas==2.2.2', 'numpy==1.26.4', 'scikit-learn==1.4.2', 'rdkit==2023.9.5','matplotlib==3.9.2','seaborn==0.13.2'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        keywords=['chemical', 'categories'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Ubuntu :: Linux",
            
        ]
)