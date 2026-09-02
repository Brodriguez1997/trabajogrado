class Analysis:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.result = None
        self.score = None

    def set_result(self, result, score):
        self.result = result
        self.score = score