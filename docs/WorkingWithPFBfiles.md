![Logo](img/PcdcLogo.png)
# PCDC Data Portal
## Working with PFB Files

Data for approved PCDC Data Portal research projects will be provided in PFB (Portable Format for Bioinformatics) file format. PFB files include both schema and data in a single compact package. More information on [PFB files can be found here](https://bdcatalyst.gitbook.io/biodata-catalyst-documentation/written-documentation/getting-started/explore-available-data/gen3-discovering-data/pfb-files#what-is-a-portable-format-for-bioinformatics).    

PFB files are created, explored and modified using the Python PyPFB SDK. The SDK requires an installed Python version between 3.6 and 3.8. More information can be [found here](https://github.com/uc-cdis/pypfb). 

By convention, PFB files have a .avro file extension. 

### Set up the environment
1) Activate a Python 3 virtual environment: You can use any Python package manager to activate a virtual environment (e.g. Python virtualenv, Anaconda, Poetry)  
> python -m venv env
> source env/bin/activate

2) Install Python PyPFB SDK and its dependencies
> pip install pypfb[gen3]

3) Type "pfb" in the terminal window to verify the installation.

[![fig2](/img/PFBcommands.jpg "PFB Commands")](https://docs.google.com/drawings/d/1x4dZh19FPnKM2rLdoP8iZkdyT0G1amhfi8XPPG52XWM/edit?usp=sharing)

### Convert PFB into TSV
PFB files downloaded from the PCDC Data Portal can be converted to multiple .tsv (tab separated values) files. 

Usage: pfb to [PARENT OPTIONS] tsv [OPTIONS] [OUTPUT]

Convert PFB into TSV files under [OUTPUT] for modification of data in TSV format.

\[PARENT OPTIONS\]: -i  FILENAME(The PFB file)

The default [OUTPUT] is ./tsvs/.

\[OPTION\]: None

Example:
 > pfb to -i data.avro tsv
 
[![fig3](/img/PFBconvert.jpg "PFB conversion")](https://docs.google.com/drawings/d/1qKL_t_bvC_M1phzoug5tyckaYaIXhRkqdol53orveYw/edit?usp=sharing)

Note: The PFB file in this example includes data from three nodes (study, person, and subject).