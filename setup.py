#from distutils.core import setup
import setuptools

setuptools.setup(name='target_chembl',
		version='0.0.5',
		scripts=['patho_chembl/chembldb_pfam_mech.py', 'patho_chembl/chembldb_pfam_assay.py', 'patho_chembl/mol_trg.py', 'patho_chembl/pfam_df_update.py', 'patho_chembl/pfam_mol_assay.py',
    		'patho_chembl/pfam_mol_mech.py', 'patho_chembl/pfam_trg_sql_assay.py', 'patho_chembl/pfam_trg_sql_mecanism.py', 'patho_chembl/tanimoto.py', 'patho_chembl/trg_mol.py', 'patho_chembl/trg_mol_funcion.py'],

		requires=['requests','argparse', 'chembl_webresource_client', 'pandas'],

		author='Florencia A. Castello',
		license='MIT license',
		author_email='florencia.castelloz@gmail.com',
		description='Simple interface for ChEMBL DB',
		url='https://github.com/florenciacastello/target_chembl',
      		packages=setuptools.find_packages(),
		long_description='',
		python_requires='>=3.6'
		)
