from chembl_webresource_client.new_client import new_client
import pandas as pd
from pandas import json_normalize
import json
import argparse
from io import StringIO
import sys

def trg_mol (handle):
    mol_=[]
    if handle:
        for trg_id in handle:
            trg_id = trg_id.strip()
            mol_=mol_+list(new_client.activity.filter(target_chembl_id ='CHEMBL4818',
             assay_type = 'B').only("molecule_chembl_id", "canonical_smiles", "pchembl_value",
             "target_organism"))
    return mol_

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', help='Input. File containing list of target chembl_id', type=argparse.FileType('r'), required=True)
    parser.add_argument('-o','--output', help='Output result must be a .csv file',
     type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

    records=trg_mol(args.input)
    if records:
        df = pd.DataFrame.from_dict(json_normalize(records), orient='columns')
        #df_fin = df[['molecule_chembl_id']]
        df_nodup= df.drop_duplicates(subset=['molecule_chembl_id'])
        output=StringIO()
        df_nodup.to_csv(args.output) ;
    else:
    	print('No result', file=sys.stderr)
    	return 0

if __name__=='__main__':
		Main()
