"""Input/output helpers for single-cell RNA-seq data."""

import glob

import pandas as pd
import scanpy as sc


def read_scRNA_data(location: str, data_type: str, barcode_str=None):
    if data_type == "h5ad":
        try:
            adata = sc.read_h5ad(location)
            if not barcode_str == None:
                adata_barcode = [f'{barcode_str}_{ii}' for ii in range(adata.shape[0])]
                adata.obs_names = adata_barcode
            return adata
        except IsADirectoryError:
            print("""#####
            The input is not a file. Maybe it is a directory.
            Reading the first h5ad file in it.
            #####""")
            try:
                h5ad_files = glob.glob(location + "/*.h5ad")
                print(f"h5ad files: {h5ad_files[0]}")
                adata = sc.read_h5ad(h5ad_files[0]) #(location + '/' + h5ad_files[0])

                if not barcode_str == None:
                    adata_barcode = [f'{barcode_str}_{ii}' for ii in range(adata.shape[0])]
                    adata.obs_names = adata_barcode
                return adata
            except IndexError:
                print("There was no h5ad file to read.")
        except FileNotFoundError:
            print('The path to h5ad file seems incorrect.')

    if data_type == "mtx":
        print('Reading mtx')
        mtx_file = glob.glob(location + "/*.mtx")
        assert len(mtx_file)==1, 'There are more than one mtx file'
        gene_file = glob.glob(location + "/gene*")
        if len(gene_file)==0:
            gene_file = glob.glob(location + "/feat*")
        assert len(gene_file)==1, 'There are more than one gene name/id file'
        cluster_file = glob.glob(location + "/cluster*")

        adata = sc.read_mtx(mtx_file[0])
        adata= adata.T

        adata_features=pd.read_csv(gene_file[0], header=None, sep='\t')
        adata.var_names= adata_features[0].tolist()

        if len(cluster_file) == 1:
            leiden_clusters = pd.read_csv(cluster_file[0])
            adata.obs['leiden_precalculated'] = leiden_clusters['partition'].values
            adata.obs['leiden_precalculated'] = adata.obs['leiden_precalculated'].astype('category')

        if not barcode_str == None:
            adata_barcode = [f'{barcode_str}_{ii}' for ii in range(adata.shape[0])]
            adata.obs_names = adata_barcode

        return adata
