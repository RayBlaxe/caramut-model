# Indonesian Text Summarization with BERT2BERT

A fine-tuned Indonesian text summarization model based on BERT-to-BERT architecture using the Liputan6 dataset.

## 📖 Overview

This project implements an extractive and abstractive text summarization system for Indonesian language using a pre-trained BERT2BERT model. The model is fine-tuned on the Liputan6 dataset to generate concise summaries of Indonesian news articles.

## 🚀 Features

- **Indonesian Language Support**: Specialized for Bahasa Indonesia text summarization
- **BERT2BERT Architecture**: Uses encoder-decoder transformer architecture
- **CPU Training**: Optimized for training without GPU requirements
- **Liputan6 Dataset**: Trained on high-quality Indonesian news dataset
- **Custom Training Loop**: Manual training implementation for better control

## 📋 Requirements

- Python 3.8+
- PyTorch 2.0+
- Transformers 4.20+
- Datasets
- Evaluate
- ROUGE Score
- tqdm

## 🛠️ Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd newsum-model
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download the dataset:
   - Place `liputan6_data.tar.gz` in the root directory
   - The notebook will automatically extract it

## 📊 Dataset

The project uses the **Liputan6 dataset**, which contains:
- Indonesian news articles
- Human-written summaries
- Clean, preprocessed text data
- Train/test split for evaluation

**Dataset Statistics:**
- Training samples: 1,600
- Test samples: 400
- Language: Bahasa Indonesia
- Domain: News articles

## 🏃‍♂️ Usage

### Training the Model

1. Open the Jupyter notebook:
```bash
jupyter notebook Untitled0.ipynb
```

2. Run the cells in order:
   - Package verification
   - Data loading and preprocessing
   - Model configuration
   - Training loop
   - Evaluation
   - Model saving

### Model Configuration

The model uses the following configuration:
- **Base Model**: `cahya/bert2bert-indonesian-summarization`
- **Max Input Length**: 512 tokens
- **Max Output Length**: 128 tokens
- **Batch Size**: 1 (CPU optimized)
- **Learning Rate**: 2e-5
- **Optimizer**: AdamW

### CPU Training Settings

Optimized for CPU-only training:
- Small batch size (1)
- Gradient accumulation (8 steps)
- No CUDA dependencies
- Memory-efficient data loading

## 📈 Model Performance

The model is evaluated using ROUGE metrics:
- **ROUGE-1**: Unigram overlap
- **ROUGE-2**: Bigram overlap
- **ROUGE-L**: Longest common subsequence

## 🔧 Project Structure

```
newsum-model/
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── Untitled0.ipynb        # Main training notebook
├── setup.sh               # Environment setup script
├── test_packages.py       # Package verification
├── .venv/                 # Virtual environment (ignored)
├── dataset/               # Extracted dataset (ignored)
├── results/               # Training outputs (ignored)
├── logs/                  # Training logs (ignored)
└── indo_summary_model/    # Saved model (ignored)
```

## 💾 Model Saving and Loading

### Saving the Model
```python
model.save_pretrained("./indo_summary_model")
tokenizer.save_pretrained("./indo_summary_model")
```

### Loading the Model
```python
from transformers import BertTokenizer, EncoderDecoderModel

tokenizer = BertTokenizer.from_pretrained("./indo_summary_model")
model = EncoderDecoderModel.from_pretrained("./indo_summary_model")
```

### Generating Summaries
```python
def generate_summary(text, max_length=128):
    inputs = tokenizer(text, max_length=512, padding=True, 
                      truncation=True, return_tensors="pt")
    
    with torch.no_grad():
        summary_ids = model.generate(**inputs, 
                                   max_length=max_length, 
                                   num_beams=2, 
                                   early_stopping=True)
    
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Example usage
article = "Your Indonesian article text here..."
summary = generate_summary(article)
print(summary)
```

## 🎯 Example

**Input Article:**
```
Pemerintah Indonesia mengumumkan kebijakan baru untuk meningkatkan 
infrastruktur digital di seluruh nusantara. Program ini bertujuan 
untuk mengurangi kesenjangan digital antara daerah perkotaan dan 
pedesaan...
```

**Generated Summary:**
```
Pemerintah Indonesia umumkan kebijakan baru untuk tingkatkan 
infrastruktur digital guna kurangi kesenjangan digital.
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 Notes

- **CPU Only**: This implementation is optimized for CPU training
- **Memory Usage**: Monitor RAM usage during training
- **Training Time**: Expect longer training times on CPU
- **Dataset Size**: Using subset of full Liputan6 dataset for efficiency

## 🔗 References

- [Liputan6 Dataset](https://github.com/fajri91/sum_liputan6)
- [BERT2BERT Paper](https://arxiv.org/abs/1907.12461)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Base Model: cahya/bert2bert-indonesian-summarization](https://huggingface.co/cahya/bert2bert-indonesian-summarization)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Your Name - NLP Course Project, Semester 8

---

**Note**: This is an academic project for learning purposes. For production use, consider using larger datasets and GPU acceleration for better performance.
