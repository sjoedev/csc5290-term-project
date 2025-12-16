import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def csv_to_parquet_streaming(
    csv_path,
    parquet_path,
    chunksize,
    compression,
) -> None:
    writer = None
    rows = 0

    for i, chunk in enumerate(pd.read_csv(
        csv_path,
        chunksize=chunksize,
        low_memory=False,
    )):
        table = pa.Table.from_pandas(chunk, preserve_index=False)

        if writer is None:
            writer = pq.ParquetWriter(
                parquet_path,
                table.schema,
                compression=compression
            )

        writer.write_table(table)
        rows += len(chunk)

        if (i + 1) % 5 == 0:
            print(f"Wrote ~{rows:,} rows...")

    if writer is not None:
        writer.close()

    print(f"Done. Wrote {rows:,} rows to {parquet_path}")

csv_to_parquet_streaming(
    csv_path="data/parsed/UDP.csv",
    parquet_path="data/parquet/UDP.parquet",
    chunksize=200_000,
    compression="zstd",
)

csv_to_parquet_streaming(
    csv_path="data/parsed/UDP-lag.csv",
    parquet_path="data/parquet/UDP-lag.parquet",
    chunksize=200_000,
    compression="zstd",
)

csv_to_parquet_streaming(
    csv_path="data/parsed/SSDP.csv",
    parquet_path="data/parquet/SSDP.parquet",
    chunksize=200_000,
    compression="zstd",
)

csv_to_parquet_streaming(
    csv_path="data/parsed/SNMP.csv",
    parquet_path="data/parquet/SNMP.parquet",
    chunksize=200_000,
    compression="zstd",
)

csv_to_parquet_streaming(
    csv_path="data/parsed/NTP.csv",
    parquet_path="data/parquet/NTP.parquet",
    chunksize=200_000,
    compression="zstd",
)

csv_to_parquet_streaming(
    csv_path="data/parsed/LDAP.csv",
    parquet_path="data/parquet/LDAP.parquet",
    chunksize=200_000,
    compression="zstd",
)

csv_to_parquet_streaming(
    csv_path="data/parsed/DNS.csv",
    parquet_path="data/parquet/DNS.parquet",
    chunksize=200_000,
    compression="zstd",
)

csv_to_parquet_streaming(
    csv_path="data/parsed/benign.csv",
    parquet_path="data/parquet/benign.parquet",
    chunksize=200_000,
    compression="zstd",
)
