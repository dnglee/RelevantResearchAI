# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
import torch
# open text file and get the content from the trained_data folder 
import os


def get_text():
    # # Print the current working directory
    # print("Current Working Directory:", os.getcwd())

    file_path = os.path.join(os.getcwd(), "models", "trained_data", "example.txt")
    
    with open(file_path, 'r') as f:
        text = f.read()
    return text

def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    nltk.download('punkt')
    return tokenizer, model


def summarize_text():
    print("Summarizing text...")
    tokenizer, model = load_model("UNIST-Eunchan/Research-Paper-Summarization-Pegasus-x-ArXiv")

    print("Model loaded successfully")
    text = get_text()

    # Tokenize the input text
    print("Tokenizing input text...")
    inputs = tokenizer("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    
    # Generate summary
    print("Generating summary...")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)  # Move model to the appropriate device

    # Generate summary # summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    #DB-SD
    summary_ids = model.generate(
        input_ids=inputs["input_ids"].to(device),
        attention_mask=inputs["attention_mask"].to(device),
        num_beam_groups=5,
        diversity_penalty=1.0,
        num_beams=5,
        min_length=150,
        max_length=512,  # Adjust this based on your needs
        length_penalty=2.0,
        early_stopping=True
    )
    

    # Decode the output
    print("Decoding output...")
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    print("Summary:", summary)
    return summary




# tokenizer, model = load_model("UNIST-Eunchan/Research-Paper-Summarization-Pegasus-x-ArXiv")

# text = get_text()

# summary = summarize_text(text, tokenizer, model)

