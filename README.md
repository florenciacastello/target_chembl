# target_chembl
mol_trg.py: returns all target related to the search compound according to API. INPUT=.txt list of Chemble_id (compound). OUTPUT= .csv table containing 3 columns trg_chembl_ID, 'pchembl_median', 'activity_comment'.

trg_mol.py: returns all compounds related to the search target according to API. INPUT= .txt list of Chemble_id (target). OUTPUT= .csv  table containing 4 columns mol_chembl_ID, 'pchembl_median', 'activity_comment', 'target_organism'.

tanimoto.py: returns all compounds related to the search SMILES according to the Tanimoto similarity score given (60% Default). INPUT= .txt SMILES list. OUTPUT= .csv  table containing 3 columns 'mol_chembl_id', 'similarity','smiles'

pfam_mol_assay.py: returns all compounds related to the search pfam ID according to ChEMBL data base via assay related information. INPUT= .txt PFAM ID list. OUTPUT= .csv  table containing 2 columns of 'mol_chembl_id': "Dudoso", "Confiable".

pfam_mol_mech.py: returns all compounds related to the search pfam ID according to ChEMBL data base via mechanism related information. INPUT= .txt PFAM ID list. OUTPUT= .csv  table containing 2 columns of 'mol_chembl_id': "Dudoso", "Confiable".

SMILES_file: SMILES list

OUT: File with two columns. First column ChEMBL_ID, second column SMILES. Separated by "\t". xPfamID + xTanimoto
<img src="https://docs.google.com/drawings/d/e/2PACX-1vSSwg9kpBGrZ5d2lJAgvReRPHrV0O1JAkZ2C8Mu9ui4F2FxBriT6iRT8mE1QZaTFPWPx9qbpNCMPNRf/pub?w=960&amp;h=720">
