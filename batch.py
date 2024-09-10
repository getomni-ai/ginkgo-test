import os
import requests
from protein_utils import generate_random_protein_sequences

# Define your API endpoint and API key
url = 'https://api.ginkgobioworks.ai/v1/batches/transforms/run'
api_key = os.getenv('GINKGO_API_KEY')
transform = [{'type': 'FILL_MASK'}]
model = 'ginkgo-aa0-650M'

# Protein Sequence
seq_number = 5
seq_length = 400
add_mask = True

# Generate N masked sequences
protein_sequences = generate_random_protein_sequences(
    seq_number, seq_length, add_mask)

# Prepare the list of requests for the batch
requests_list = []
for seq in protein_sequences:
    transforms = transform
    # transforms = [{'type': 'EMBEDDING'}]
    requests_list.append({
        'model': model,
        'text': seq,
        'transforms': transforms
    })

# Send sequences to batch request
response = requests.post(
    url,
    headers={'x-api-key': api_key, 'Content-Type': 'application/json'},
    json={'requests': requests_list}
)

if response.ok:
    data = response.json()
    print(f"Batch response: {data}")
else:
    print(f"Error: {response.text}")
