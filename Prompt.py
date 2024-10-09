class Prompt:
    def __init__(self, question, data):
        self.question = question
        self.data = data
        self.prompt = self.createPrompt()

    def loadPrompt(self, file_name = "prompt.txt"):
        with open(file_name) as f:
            content = f.read()
        return content
    
    def createPrompt(self):
        prompt_template = self.loadPrompt()
        prompt_template = prompt_template.replace("<insert question>", self.question).replace("<insert data>", self.data)
        return prompt_template