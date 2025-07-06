#!/usr/bin/env python3
"""
Test script to verify all required packages are working correctly.
"""

import sys
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print("-" * 50)

# Test all required packages
packages_to_test = [
    'transformers',
    'datasets', 
    'evaluate',
    'rouge_score',
    'torch',
    'tqdm'
]

for package in packages_to_test:
    try:
        module = __import__(package)
        version = getattr(module, '__version__', 'unknown')
        print(f"✓ {package} version: {version}")
    except ImportError as e:
        print(f"✗ {package} import failed: {e}")

print("-" * 50)
print("Testing transformers functionality...")

try:
    from transformers import BertTokenizer, EncoderDecoderModel
    print("✓ BertTokenizer and EncoderDecoderModel imported successfully")
    
    # Test if we can load the model (this will download it if not cached)
    print("Testing model loading...")
    tokenizer = BertTokenizer.from_pretrained("cahya/bert2bert-indonesian-summarization")
    print("✓ Tokenizer loaded successfully")
    
    model = EncoderDecoderModel.from_pretrained("cahya/bert2bert-indonesian-summarization")
    print("✓ Model loaded successfully")
    
    # Test tokenization
    test_text = "Ini adalah teks uji untuk summarization."
    tokens = tokenizer.encode(test_text, return_tensors="pt")
    print(f"✓ Tokenization test passed. Tokens shape: {tokens.shape}")
    
except Exception as e:
    print(f"✗ Transformers functionality test failed: {e}")

print("-" * 50)
print("Package test completed!")
