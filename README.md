### Testing the Ginkgo API

#### Setup:

- Add `.env` with `GINKGO_API_KEY`
- Start python vnenv

This repo has two scripts:

1. `single.py` - Creates a set of random sequences and makes synchronous requests to the transform api
2. `batch.py` - Create a set of random sequences and sends everything to the batch endpoints

#### Generating sequences

The `protein_utils` script generates a group of random sequences.

```py
# Config
seq_number = 5
seq_length = 400
add_mask = True

# Generate N masked sequences
protein_sequences = generate_random_protein_sequences(seq_number, seq_length, add_mask)
```
