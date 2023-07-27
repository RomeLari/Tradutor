from googletrans import Translator

text = input('Insira texto para traduzir: ')

translator = Translator()

translate = translator.translate(text, dest="en")
print(translate.text)

#Para o pacote funcionar, botei o: 
# 
# pip install googletrans==4.0.0-rc1