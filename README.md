# Joe Sturm Term Project

## Instructions

1. Decompress `data/parquet.tar.gz` into the `data/parquet/` folder. You should end up with `data/parquet/benign.parquet` etc.
2. Install Python dependencies from `pyproject.toml` (preferably in a venv)
3. Run the `notebooks/analysis.ipynb` Jupyter Notebook

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
