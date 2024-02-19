"""Taller evaluable"""

import glob

import pandas as pd

import string

def load_input(input_directory):
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #
    input_files = glob.glob(input_directory + '/*.txt')
    df = pd.concat((pd.read_csv(f, sep='\t', header=None, names=['text']) for f in input_files), ignore_index=True)
    return df


def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    dataframe['clean_text'] = dataframe['text'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)).lower())
    return dataframe


def count_words(dataframe):
    """Word count"""
    words = dataframe['clean_text'].str.split(expand=True).stack()
    word_counts = words.value_counts().reset_index()
    word_counts.columns = ['word', 'count']
    return word_counts


def save_output(dataframe, output_filename):
    """Save output to a file."""
    dataframe.to_csv(output_filename, sep='\t', index=False, header=False)

#   1   q
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    input_df = load_input(input_directory)
    clean_df = clean_text(input_df)
    word_count_df = count_words(clean_df)
    save_output(word_count_df, output_filename)



if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
