"""
Read an input file and convert it to required format
"""
import os.path
import constants


def read_file(path):
    """
    Given a path, read a file where each line is a sentence in the format <word>_<POS>

    Part of speech tags are from Penn Treebank

    Parameters
    ----------
    path : str
        Path to the file

    Returns
    -------
    list
        A list containing each sentence broken into tokens. Each token is a tuple in form (word, pos)
    """
    if not os.path.isfile(path):
        return ValueError("The given input is not a file: " + str(path))

    output = []

    with open(path, 'r') as input_file:
        for line in input_file:
            # break the line into words first
            words = line.strip().split(" ")
            tag_tuples = []
            for token in words:
                split_token = token.split(constants.DELIMITER)
                tag_tuples.append((split_token[0], split_token[1]))
            output.append(tag_tuples)

    return output
