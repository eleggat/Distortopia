import os 
import random #for random number gneration (will use for SNP positions)
import argparse

"""Simulate F1 hybrid from two parental VCFs."""

def run_simulation(args):
    parent1 = load_vcf(args.parent1)
    parent2 = load_vcf(args.parent2)

    f1_hybrid = {}

    for variant in shared_variants(parent1, parent2):
        allele1 = select_random_allele(parent1[variant])
        allele2 = select_random_allele(parent2[variant])
        f1_hybrid[variant] = f"{allele1}/{allele2}"

    write_vcf(f1_hybrid, output=args.output)
