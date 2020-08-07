import argparse
from chembl_webresource_client.new_client import new_client
from io import StringIO
import pandas as pd
from pandas import json_normalize
def chembl_similarity (handle, tanimoto_similarity):
	smiles = handle.read().strip()
	return new_client.similarity.filter(smiles = smiles, similarity = tanimoto_similarity)

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--input', help='Input smiles_file', type=argparse.FileType('r'), required=True)
	parser.add_argument('-t','--tanimoto', help='Tanimoto similarity, 60 by default', type=int, default=60)
	parser.add_argument('-o','--output', help='Output result in a tanimoto.txt file', default=False)
	args = parser.parse_args()

	res = chembl_similarity(args.input, args.tanimoto)
	df = pd.DataFrame.from_dict(json_normalize(res), orient='columns')
	df_final = df[['molecule_chembl_id', 'similarity','molecule_structures.canonical_smiles']]
	output = StringIO()
	df_final.to_csv(output) ;
	if args.output:
		f = open(args.output, "w")
		f.write(str(df_final))
	else: print(output.getvalue())

if __name__=='__main__':
	Main()
