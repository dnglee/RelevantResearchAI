Relevant Research AI 

The goal is to create an application where it can summarize a research paper levaraging open source models from the Hugging Face Hub. The idea is to use LangChain and detect which kind of research paper it is and use the specific model for that topic (ex. if it's a paper about medicine, then use the medical model to summarize the paper, analyze and draw out all the main points). 

For summarization: 
Base Model: Pegasus-x-base (State-of-the-art for Long Context Summarization) - google/pegasus-x-base
Fined Tunes Open-Source: https://huggingface.co/UNIST-Eunchan/Research-Paper-Summarization-Pegasus-x-ArXiv

If repository is pulled, please install the following and use a Python env to encapsulate the projects needs. 

- Clone repository
- Open locally
- Before running the following commands, please ensure you have the following installed locally
  -  python 3.x or higher
  -  CUDA if using windows (in my case)
    - if you encounter an issue later on with not having a .dll file but you do check this issue https://github.com/pytorch/pytorch/issues/131662, you will be required to install a C++ package
- Use the terminal from VSCode (which is what I am using) to start a python virtual environment
  - `python -m venv {name for the folder which holds your virtual env}`
  - `pip install transformers`
  - `pip install torch`


Things to know before running: 
- Once you run the main.py file, it will locally download the model from the Hugging Face Hub and load the model to your computers local memory (if you have GPU it will use it, else if will use your RAM)





Disclamer: The projects goal is for learning purposes, it is up to your own descretion if pulled. 
