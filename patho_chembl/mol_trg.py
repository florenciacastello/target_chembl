import argparse
from chembl_webresource_client.new_client import new_client
from io import StringIO
import pandas as pd
from pandas import json_normalize
import sys

def chembl_trg (handle):
    trg_info=[]
    if handle:
        for molecule_chembl_id in handle:
            molecule_chembl_id = molecule_chembl_id.strip()
            trg_info=trg_info+list(new_client.activity.filter(molecule_chembl_id=molecule_chembl_id,
            assay_type = 'B').only('target_chembl_id', 'activity_comment', 'pchembl_value'))
    return trg_info

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', help='Input tanimoto_file', type=argparse.FileType('r'), required=True)
    parser.add_argument('-o','--output', help='Output result in a target.txt file',
     type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

    records=chembl_trg(args.input)
    if not records:
    	print('No result', file=sys.stderr)
    	return 0

    df = pd.DataFrame.from_dict(json_normalize(records), orient='columns')
    df_fin = df[['target_chembl_id', 'activity_comment', 'pchembl_value']]
    df_nodup= df_fin.drop_duplicates(subset=['target_chembl_id'])
    output=StringIO()
    df_nodup.to_csv(output) ;
#    print(df_nodup)

    if args.output:
        f = open(args.output, "w")
        f.write(str(df_nodup))
    else: print(output.getvalue())

if __name__=='__main__':
		Main()
