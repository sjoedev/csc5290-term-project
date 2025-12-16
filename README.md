# Joe Sturm Term Project

## Instructions

1. Clone `https://github.com/sjoedev/csc5290-term-project.git` (if this fails, you may need to install git-lfs)
```
git clone https://github.com/sjoedev/csc5290-term-project.git
cd ./csc5290-term-project
```
2. Decompress `data/parquet.tar.gz` into the `data/parquet/` folder. You should end up with `data/parquet/benign.parquet` etc.
```
tar -xzf ./data/parquet.tar.gz -C ./data
```
3. Install Python dependencies from `pyproject.toml` (preferably in a venv) and set up ipykernel
```
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r ./requirements.txt
python -m ipykernel install --user --name csc5290-term-project --display-name "Python (.venv)"
```
4. Launch Juypter Lab
```
jupyter lab
```
5. In Jupyter Lab, open `notebooks/analysis.ipynb`
6. Make sure appropraite kernel is selected
7. Run

## Note

If you have the traces as CSV files instead of Parquet, place the CSV files in `data/parsed` and run `scripts/csv_to_parquet.py`.

In:

1. data/parsed/UDP.csv
2. data/parsed/UDP-lag.csv
3. data/parsed/SSDP.csv
4. data/parsed/SNMP.csv
5. data/parsed/NTP.csv
6. data/parsed/LDAP.csv
7. data/parsed/DNS.csv
8. data/parsed/benign.csv

Out:

1. data/parquet/UDP.parquet
2. data/parquet/UDP-lag.parquet
3. data/parquet/SSDP.parquet
4. data/parquet/SNMP.parquet
5. data/parquet/NTP.parquet
6. data/parquet/LDAP.parquet
7. data/parquet/DNS.parquet
8. data/parquet/benign.parquet
