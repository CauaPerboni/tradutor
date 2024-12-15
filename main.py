from googletrans import Translator

def traduzir_texto(texto, idioma_destino='en'):
    translator = Translator()
    traducao = translator.translate(texto, dest=idioma_destino)
    return traducao.text

if __name__ == "__main__":
    texto_original = "Olá, como você está?"
    idioma_destino = 'en' 
    texto_traduzido = traduzir_texto(texto_original, idioma_destino)

    print(f"Texto original: {texto_original}")
    print(f"Texto traduzido: {texto_traduzido}")
