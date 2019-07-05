from rdkit import Chem
import rdkit.Chem.Scaffolds.MurckoScaffold as Scaffold


def manage_data(path):
    """
    STOCK datasets form
    id_smiles.txt->[ID] [whole] [scaffold]
    data.txt -> [ID] [activity_whole] [activity_scaffold]

    CHEMBL dataset form
    [ID] [whole] [activity]

    should convert CHEMBL dataset into two file
    1. file with [ID] [whole] [scaffold]
    2. file with [ID] [activity_whole] [activity_scaffold]
    :param file:
    :return:
    """
    with open(path) as f:
        with_scaffold = []
        with_affinity = []
        for line in f:
            # making scaffold smiles
            scaffold_row = []
            affinity_row = []
            row = line.split()
            # row : ID smiles affinity
            for i in range(len(row)):
                if i == 1:
                    whole_smiles = row[i]
                    whole_molecule = Chem.MolFromSmiles(whole_smiles)
                    scaffold_molecule = Scaffold.GetScaffoldForMol(whole_molecule)
                    scaffold_smiles = Chem.MolToSmiles(scaffold_molecule)
                    scaffold_row.append(whole_smiles)
                    scaffold_row.append(scaffold_smiles)
                elif i == 2:
                    affinity = row[i]
                    affinity_row.append(affinity)
                else:
                    scaffold_row.append(row[i])
                    affinity_row.append(row[i])
            _scaffold = " ".join(scaffold_row)
            _affinity = " ".join(affinity_row)
            with_scaffold.append(_scaffold)
            with_affinity.append(_affinity)
    for i in range(len(with_scaffold)):
        scaffold_file.write("%s\n" % with_scaffold[i])
    scaffold_file.close()
    for i in range(len(with_affinity)):
        affinity_file.write("%s\n" % with_affinity[i])
    affinity_file.close()


manage_data("../data/chembl_affinity.txt")
