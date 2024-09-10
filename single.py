import os
import requests
from dotenv import load_dotenv
from protein_utils import generate_random_protein_sequences

load_dotenv()

# API Config
url = 'https://api.ginkgobioworks.ai/v1/transforms/run'
api_key = os.getenv('GINKGO_API_KEY')
print(api_key)
transform = [{'type': 'FILL_MASK'}]
model = 'ginkgo-aa0-650M'

# Protein Sequence
seq_number = 5
seq_length = 400
add_mask = True

# Generate N masked sequences
protein_sequences = generate_random_protein_sequences(
    seq_number, seq_length, add_mask)

# Make one transform request per seq
for sequence in protein_sequences:
    payload = {
        'model': model,
        'text': sequence,
        'transforms': transform
    }
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=payload)

    if response.ok:
        data = response.json()
        print(f"Running sequence: {sequence}")
        print(f"Response: {data}")
    else:
        print(f"Error for sequence {sequence}: {response.text}")
