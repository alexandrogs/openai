from code import *
from insert import *
import datetime
class Index(Code, Insert):
    def __init__(self):
        Code.__init__(self)
        Insert.__init__(self)
        with open("input.txt") as f: en = f.read()
        aux = en.split("[insert]")
        if len(aux) == 2:
            prompt = aux[0]
            suffix = aux[1]
            datetime_variable = datetime.datetime.now().strftime("%Y%m%dT%H%M%S-4").strip()
            with open('logs.txt', 'w') as f: f.write(datetime_variable + '\n')
            self.insert(prompt, suffix)
        else:
            prompt = aux[0]
            count = 1
            while True:
                datetime_variable = datetime.datetime.now().strftime("%Y%m%dT%H%M%S-4").strip()
                aux = '\n'.join(prompt.split('\n')[:3])
                with open('logs.txt') as f: f.write(datetime_variable + " - " + aux + "\n")
                datetime_variable = self.code(prompt, count)
                input('Continuar?')
                dest = f"history/complete/{datetime_variable}"
                with open(dest + "/output.txt") as f: prompt = f.read()
                count += 1

def main():
    Index()

if __name__ == "__main__":
    main()