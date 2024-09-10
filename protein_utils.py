import random

# Protein alphabet
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

# Generate N proteins of X length. Optional include random <mask> character
def generate_random_protein_sequences(num_sequences: int, sequence_length: int, add_mask: bool = False):
    sequences = []
    for _ in range(num_sequences):
        sequence = ''.join(random.choices(amino_acids, k=sequence_length))

        # Optionally insert <mask> at a random position
        if add_mask:
            mask_position = random.randint(0, sequence_length - 1)
            sequence = sequence[:mask_position] + \
                '<mask>' + sequence[mask_position + 1:]

        sequences.append(sequence)
    return sequences
