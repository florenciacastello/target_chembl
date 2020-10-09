import argparse
from chembl_webresource_client.new_client import new_client
from io import StringIO
import pandas as pd
import numpy as np
import collections
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
    def pchembl_median(x):
        names = {
            'activity_comment': x.iloc[0]['activity_comment'],
            'pchembl_median': x['pchembl_value'].median(),
        }
        return(pd.Series(names, index = ['pchembl_median', 'activity_comment']))
    df_pchembl_median = df_fin.groupby(['target_chembl_id']).apply(pchembl_median).reset_index()
    df_pchembl_median.loc[((df_pchembl_median['activity_comment'] != 'Not Active')
     | (df_pchembl_median['activity_comment'] != 'inconclusive')) & (df_pchembl_median['pchembl_median'].isnull()), 'pchembl_median'] = 6
    df_drop = df_pchembl_median.drop(df_pchembl_median[df_pchembl_median.pchembl_median < 6].index)
    df_nodup= df_drop.drop_duplicates(subset=['target_chembl_id'])
    output=StringIO()
    df_nodup.to_csv(args.output) ;

#    print(df_nodup)

if __name__=='__main__':
		Main()
