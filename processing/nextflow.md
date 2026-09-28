# UVA
---
```
#!/bin/bash
#SBATCH --job-name=dlfpc_nextflow_scrnaseq_3mid_cellranger
#SBATCH --nodes=1
#SBATCH --output=autput_%x_%A_%a.out
#SBATCH --partition=standard
#SBATCH --ntasks=24
#SBATCH --mem=256gb
#SBATCH --time=72:00:00
#SBATCH --account=iprime
#SBATCH --array=1-1

export NXF_SINGULARITY_CACHEDIR=/scratch/mbt8hz/apptainer_cache
export APPTAINER_CACHEDIR=/scratch/mbt8hz/apptainer_cache

module load nextflow
module load apptainer

nextflow run nf-core/scrnaseq \
-profile apptainer \
-w ./work_scrnaseq \
--input samplesheet_3mid_snRNA.csv \
--fasta GRCh38.primary_assembly.genome.fa \
--gtf gencode.v49.primary_assembly.annotation.gtf \
--protocol 10XV3 \
--aligner cellranger \
--outdir ./results_dlfpc_cellranger_mid_br6522_8325_8492 \
--skip_cellbender 
# -resume
```
