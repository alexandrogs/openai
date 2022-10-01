import argparse


class Lib(argparse.Namespace):
    def __init__(self):
        super(Lib, self).__init__()

    class History(argparse.Namespace):
        def __init__(self):
            super(Lib.History, self).__init__()

        def get(self):
            pass

        def set(self, values, subfolder=''):
            import datetime
            import os
            datetime_variable = datetime.datetime.now().strftime("%Y%m%dT%H%M%S-4").strip()
            dest = f'history/{subfolder}/{datetime_variable}'
            os.makedirs(dest)
            for value in values:
                file = f"{value}.txt"
                with open(dest + '\n' + file, 'w') as f: f.write(values[value])
            return datetime_variable