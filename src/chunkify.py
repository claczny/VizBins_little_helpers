#! /usr/bin/env python

"""Chunkify FASTA sequences

Usage:
    chunkifySequences.py (-i IN_FASTA) (-o OUT_FASTA) [-c CHUNK_LENGTH]
    chunkifySequences.py (-h | --help)
    chunkifySequences.py --version

Arguments:
    IN_FASTA    Path to input FASTA file.
    OUT_FASTA    Path to output FASTA file.
    CHUNK_LENGTH   Integer value representing the desired chunk length (e.g., 1000).

Options:
    -i IN_FASTA The input fasta file.
    -o OUT_FASTA    The output fasta file containing the chunkified sequences.
    -c CHUNK_LENGTH How large should the chunks be? Only creates chunks if the resulting chunks are ALL >= CHUNK_LENGTH [default: 5000].
    -h --help   Show this screen.
    --version   Show version.
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from docopt import docopt

if __name__ == "__main__":
    # Get the arguments
    arguments = docopt(__doc__, version='0.9')

    in_fasta_file = arguments['-i']
    out_fasta_file = arguments['-o']
    chunk_length = 5000 # Default chunk length
    if( arguments['-c']):
        chunk_length = int(arguments['-c'])

    handle = open(in_fasta_file, "rU")
    output_handle = open(out_fasta_file, "w")
    counter_in_sequences = 0
    counter_out_sequences = 0

    for record in SeqIO.parse(handle, "fasta") :
        counter_in_sequences = counter_in_sequences + 1
        to_chunk_pos = 0
        seq_left = True
        chunk_counter = 0
        while seq_left:
            new_record = SeqRecord( id = record.id,
                                    name = "",
                                    seq = record.seq
                                    )
            new_record.id = new_record.id + "_" + str(chunk_counter)
            remaining_seq_length = len(record.seq) - to_chunk_pos
            # Is there enough sequence left to create another chunk?
            if(remaining_seq_length >= (2*chunk_length)):
                new_record.description = ("%s : [%i,%i]" ) % ("".join((record.description).split()[1:]), to_chunk_pos, to_chunk_pos + chunk_length -1)
                new_record = new_record[to_chunk_pos:to_chunk_pos + chunk_length]
                to_chunk_pos = to_chunk_pos + chunk_length
                seq_left = True
                chunk_counter = chunk_counter + 1
            else:
                new_record.description = ("%s : [%i,%i]" ) % ("".join((record.description).split()[1:]), to_chunk_pos, len(record.seq) -1)
                new_record = new_record[to_chunk_pos:]
                seq_left = False
            # Save the results
            SeqIO.write(new_record, output_handle, "fasta")
            counter_out_sequences = counter_out_sequences + 1

    handle.close() # Close input
    output_handle.close()

    print(("DONE: Chunkified %i input sequences into %i output sequences (chunk length %i).") % (counter_in_sequences, counter_out_sequences, chunk_length))
