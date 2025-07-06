#!/bin/bash
echo "Setting up Python environment for NLP project..."

# Install required packages
echo "Installing packages..."
python3 -m pip install --user ipykernel jupyter transformers datasets evaluate rouge-score torch tqdm

# Install kernel for jupyter
echo "Installing Jupyter kernel..."
python3 -m ipykernel install --user --name=newsum-model --display-name="Python (newsum-model)"

echo "Testing installation..."
python3 -c "
import sys
print(f'Python: {sys.version}')
try:
    import transformers
    print('✓ transformers installed')
except ImportError:
    print('✗ transformers not found')

try:
    import datasets
    print('✓ datasets installed')
except ImportError:
    print('✗ datasets not found')

try:
    import evaluate
    print('✓ evaluate installed')
except ImportError:
    print('✗ evaluate not found')

try:
    import rouge_score
    print('✓ rouge_score installed')
except ImportError:
    print('✗ rouge_score not found')

try:
    import torch
    print('✓ torch installed')
except ImportError:
    print('✗ torch not found')
"

echo "Setup complete!"
echo "Please restart VS Code and select the 'Python (newsum-model)' kernel for your notebook."
