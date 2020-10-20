import pandas as pd
from pandas import json_normalize
import json
import argparse
import sys
import csv
from importlib import reload

def load_dataset(dataset_path):
    base_pfam= pd.read_csv(dataset_path)
    base_pfam['compound_chemblid']=[eval(x) for x in base_pfam.compound_chemblid]
    return base_pfam

def search_bypfam(handle, base_pfam):
    confiable=[]
    target_domains=[]
    dudoso=[]
    if handle:
        for pfam_id in handle:
            pfam_id = pfam_id.strip()
            target_domains.append(pfam_id)
            for _,record in base_pfam.iterrows():
                if record.Domain_key == pfam_id:
                    confiable+=record.compound_chemblid
                elif pfam_id in record.Domain_key:
                    dudoso+=record.compound_chemblid
        df_base_pfam=base_pfam[base_pfam.Domain_key=="_".join(sorted(set(target_domains)))]
        for compuestos in df_base_pfam.compound_chemblid:
            confiable=confiable + compuestos
            confiable=set(confiable)
            dudoso=set(dudoso)-confiable
    return confiable, dudoso

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--dataset", help="Path to the directory of ChEMBL DB",
    default= "pfamid_chembl27_mech.csv")
    parser.add_argument('-i','--input', help='Input pfam_file', type=argparse.FileType('r'),
     required=True)
    parser.add_argument('-o','--output', help='Output result must be .csv file',
     type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

 #mejorar la salida, agregar target de donde saco el pfam. o la domain_key

    for pfam in args.input:
        if pfam:
            drugs= search_bypfam(pfam, load_dataset(args.dataset))
            if drugs:
                args.output.write(str(drugs)+ '\n')
            else:
                print(f'No result for {pfam}', file=sys.stderr)

    return 0



if __name__=='__main__':
		Main()
