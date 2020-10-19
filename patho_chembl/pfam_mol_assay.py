import pandas as pd
from pandas import json_normalize
import json
import argparse
import sys
import csv
from importlib import reload


base_pfam= pd.read_csv ('/home/fleer/Desktop/Target_chembl/pfam_mol/pfamid_chembl27_assay.csv')
base_pfam['compound_chemblid']=[eval(x) for x in base_pfam.compound_chemblid]

def search_bypfam(handle):
    confiable=[]
    target_domains=[]
    dudoso=[]
    if handle:
        for pfam_id in handle:
            pfam_id = pfam_id.strip()
            target_domains.append(pfam_id)
            for _,record in base_pfam.iterrows():
                df_base_pfam=base_pfam[base_pfam.Domain_key=="_".join(sorted(set(target_domains)))] #este en una funcion aparte
                if record.Domain_key == pfam_id:
                    confiable+=record.compound_chemblid
                elif pfam_id in record.Domain_key:
                    dudoso+=record.compound_chemblid
        for compuestos in df_base_pfam.compound_chemblid:
            confiable=confiable + compuestos
        confiable=set(confiable)
        dudoso=set(dudoso)-confiable
    return confiable, dudoso

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', help='Input pfam_file', type=argparse.FileType('r'), required=True)
    parser.add_argument('-o','--output', help='Output result must be .csv file',
     type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

    for pfam in args.input:
        if pfam:
            df_drugs=search_bypfam(pfam)
            df_drugs.to_csv(args.output) ;
            #if len(drugs):
            #    out = csv.writer(open(args.output,"w"))
            #    out.writerow(str(drugs))
        else:
            print(f'No result for {pfam}', file=sys.stderr)

    return 0



if __name__=='__main__':
		Main()
