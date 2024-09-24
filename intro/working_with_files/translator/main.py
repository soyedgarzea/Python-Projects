from translate import Translator


translator = Translator(to_lang='es')

try:
    with open(file='./working_with_files/translator/text.txt', mode='r', encoding='UTF-8') as file:
        text = file.read()
        translation = translator.translate(text) # type: ignore

        with open(file='./working_with_files/translator/translate.txt', mode='x', encoding='UTF-8') as new_file:
            new_file.write(translation)
except FileNotFoundError:
    print("File not found")
