import re

def format_name(name):
    return re.sub(r"[\/\.\<\>|\:&\",]", "_", name)[:150]

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def format_names():
    import os
    from tqdm import tqdm
    
    os.chdir("Documents")

    for doc in tqdm(os.listdir()):
        if doc.endswith(".txt"):
            doc_text = open(doc).read()
            doc_title_split = re.split(r'[.%]', doc)
            doc_title = doc_title_split[0]
            doc_year = re.search(r"\d{4}", doc_title_split[-2]).group(0)
            os.rename(doc, f"{format_name(doc_title)} %{doc_year}.txt")