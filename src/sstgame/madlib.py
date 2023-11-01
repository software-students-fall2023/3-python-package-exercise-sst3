def readText(fileString):
    prompts = []
    with open(fileString, "r") as file:
        for line in file:
            prompt = line.strip()
            prompts.append(prompt)
        return prompts
readText("madLib.txt")
