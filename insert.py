from lib import *
class Insert(Lib):
    def __init__(self):
        super(Insert, self).__init__()

    def insert(self,prompt, suffix):
        import pip
        import os
        import datetime
        import shutil
        try: import openai
        except: pip.main(['install', 'openai']); import openai
        name_var_env = "OPENAI_API_KEY"
        if name_var_env in os.environ: openai.api_key = os.getenv("OPENAI_API_KEY")
        else: openai.api_key = "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"
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=prompt,
            suffix=suffix,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        for choice in response['choices']:
            output = prompt + choice['text'] + suffix
            print(output)
            self.History().set({'input': prompt + suffix, 'output': output}, 'insert')