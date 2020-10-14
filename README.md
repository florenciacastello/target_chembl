# target_chembl
mol_trg.py: returns all target related to the search compound according to API. INPUT= list of Chemble_id (compound). OUTPUT= table containing 3 columns trg_chembl_ID, 'pchembl_median', 'activity_comment'.

trg_mol.py: returns all compounds related to the search target according to API. INPUT= list of Chemble_id (target). OUTPUT= table containing 4 columns mol_chembl_ID, 'pchembl_median', 'activity_comment', 'target_organism'.

tanimoto.py: returns all compounds related to the search SMILES according to the Tanimoto similarity score given (60% Default). INPUT= SMILES list. OUTPUT= table containing 3 columns 'mol_chembl_id', 'similarity','smiles'

SMILES_file: SMILES list

OUT: File with two columns. First column ChEMBL_ID, second column SMILES. Separated by "\t". xPfamID + xTanimoto
<img src="https://docs.google.com/drawings/d/e/2PACX-1vSSwg9kpBGrZ5d2lJAgvReRPHrV0O1JAkZ2C8Mu9ui4F2FxBriT6iRT8mE1QZaTFPWPx9qbpNCMPNRf/pub?w=960&amp;h=720">
