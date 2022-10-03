from lib import *


class Translate(Lib):
    def __init__(self, *args, **kwargs):
        import pip
        try: import winshell
        except: pip.main(['install', 'winshell']); import winshell
        import os
        super(Translate, self).__init__(*args, **kwargs)
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = winshell.my_documents()+'/certain-art-327503-0ecb41524310.json'
        self.translate_text(args)

    def translate_text(self, args, project_id="certain-art-327503"):
        import pip
        try: from google.cloud import translate
        except: pip.main(['install', 'google-cloud-translate']); from google.cloud import translate
        if len(args) != 0:
            text = args[0]
        else:
            with open('input.txt') as input: text = input.read()
        client = translate.TranslationServiceClient()
        location = "global"
        parent = f"projects/{project_id}/locations/{location}"
        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [text],
                "mime_type": "text/plain",
                "source_language_code": "en-US",
                "target_language_code": "es",
            }
        )
        for translation in response.translations:
            print("Translated text: {}".format(translation.translated_text))


def main():
    Translate()


if __name__ == "__main__":
    main()
