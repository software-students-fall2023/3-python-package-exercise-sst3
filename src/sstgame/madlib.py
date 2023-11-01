import re
def readText(fileString):
    prompts = []
    with open(fileString, "r") as file:
        for line in file:
            prompt = line.strip()
            prompts.append(prompt)
        return prompts

def extractWords(madlib):
    pattern = r'\[([^\[\]]+)\]'
    matches = re.findall(pattern, madlib)
    
    return matches
