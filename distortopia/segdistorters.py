"""Identify variants showing distorted segregation patterns."""

def detect(args):
    genotypes = parse_vcf(args.f1)
    exp_ratio = 0.5 #expected ratio
    distorted = []

    for variant, genotype in genotypes.items():
        obs_ratio = compute_allele_frequency(genotype) #observed ratio
        if abs(obs_ratio - exp_ratio) > args.threshold:
            distorted.append(variant)

    write_results(distorted, output=args.output)
