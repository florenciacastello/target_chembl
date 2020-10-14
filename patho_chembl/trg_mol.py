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
            mol_=mol_+list(new_client.activity.filter(target_chembl_id =trg_id,
             assay_type = 'B').only("molecule_chembl_id", "canonical_smiles", "pchembl_value",
             "target_organism", "activity_comment"))
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
        df.loc[((df['activity_comment'] == 'Active') & (df['pchembl_value'].isnull())), 'pchembl_value'] = 6  #TODO: revisar este filtro
        df1 = df.dropna(subset=['pchembl_value'])
        def pchembl_median(x):
            names = {
                'activity_comment': x.iloc[0]['activity_comment'],
                'target_organism': x.iloc[0]['target_organism'],
                'pchembl_median': x['pchembl_value'].median(),
            }
            return(pd.Series(names, index = ['pchembl_median', 'activity_comment', 'target_organism']))
        df_pchembl_median = df1.groupby(['molecule_chembl_id', 'canonical_smiles']).apply(pchembl_median).reset_index()
        df_drop = df_pchembl_median.drop(df_pchembl_median[df_pchembl_median.pchembl_median < 6].index)
        df_nodup= df_drop.drop_duplicates(subset=['molecule_chembl_id'])
        output=StringIO()
        df_nodup.to_csv(args.output) ;
    #    print(df)
    else:
    	print('No result', file=sys.stderr)
    	return 0

if __name__=='__main__':
		Main()
