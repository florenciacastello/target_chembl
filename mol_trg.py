import argparse
from chembl_webresource_client.new_client import new_client
from io import StringIO

def chembl_trg (handle):
    molecule_chembl_id = handle.read().strip()
    return new_client.assay.filter(molecule_chembl_id=molecule_chembl_id)

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', help='Input tanimoto_file', type=argparse.FileType('r'), required=True)
    parser.add_argument('-o','--output', help='Output result in a target.txt file', default=False)
    args = parser.parse_args()

    records = chembl_trg(args.input).only(['target_chembl_id'])

    if args.output:
        f = open(args.output, "w")
        f.write(str(records))
    else: print(output.getvalue())

if __name__=='__main__':
		Main()

