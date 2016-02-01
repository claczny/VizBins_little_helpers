# VizBin's little helpers - A collection of handy tools when working with VizBin

[VizBin](https://github.com/claczny/VizBin) provides a user-friendly interface for the efficient visualisation of (assembled) **meta**genomic data.
Furthermore, it can be used for the visualisation of **single** genome assembly data in order to inspect if any significant amounts of contamination has occured.
This could manifest in a set of clusters apparent in the VizBin map rather than a single cluster.

# Chunkify
Sometimes, independent of whether the application is for metagenomes or single genomes, it might be interesting to increase the density of the apparent clusters by normalizing the sequence length.
In particular for metagenomic assemblies, assembled sequence length may vary greatly between the consituent populations.
Some population might have long and few contigs, whereas the opposite might be true for other populations.
For these cases, the `chunkify.py` script can be used.
This script creates "chunks" out of the provided sequences with a defaul chunk-length of 3,000 nt.


