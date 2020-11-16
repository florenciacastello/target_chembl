from distutils.core import setup
setup(name='target_chembl',
		version='0.0.1',
		py_modules=['patho_chembl'],
		scripts=['patho_chembl/chembldb_pfam_mech.py', 'patho_chembl/chembldb_pfam_assay.py', 'patho_chembl/mol_trg.py', 'patho_chembl/pfam_df_update.py', 'patho_chembl/pfam_mol_assay.py',
    'patho_chembl/pfam_mol_mech.py', 'patho_chembl/pfam_trg_sql_assay.py', 'patho_chembl/pfam_trg_sql_mecanism.py', 'patho_chembl/tanimoto.py', 'patho_chembl/trg_mol.py'],

		requires=['requests','argparse', 'chembl_webresource_client', 'pandas', ],

		author='Florencia A. Castello',
		license='MIT license',
		author_email='florencia.castelloz@gmail.com',
		description='Simple interface for ChEMBL DB',
		url='https://github.com/florenciacastello/target_chembl',
		long_description='',
		)
