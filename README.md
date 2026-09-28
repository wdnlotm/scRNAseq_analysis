# Real vs generated scRNA-seq: differential expression comparison

DLPFC sample **BR6471mid**. Compares cluster-level differential expression between the
real dataset and a generated (synthetic) dataset processed through an identical pipeline.

Both datasets are concatenated, QC'd, normalised, embedded and clustered **jointly**, so
that Leiden cluster labels are directly comparable between them. Differential expression
is then run separately within each dataset, and the resulting gene sets are compared
cluster by cluster.

All artefacts are written under `output/`:

| Path | Contents |
| --- | --- |
| `output/figures/` | Every figure, prefixed `00_`, `01_`, ... in notebook order |
| `output/tables/` | Differential expression CSVs |
| `output/` | `.h5ad` exports for downstream monocle3 analysis |
