import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton
from PyQt5.QtGui import QFont, QFontDatabase
from googletrans import Translator

class Tradutor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tradutor Automático")
        self.setGeometry(100, 100, 500, 500)

        font_db = QFontDatabase()
        regular_font_id = font_db.addApplicationFont('fonts/Poppins-Regular.ttf')
        bold_font_id = font_db.addApplicationFont('fonts/Poppins-Bold.ttf')

        regular_font_family = font_db.applicationFontFamilies(regular_font_id)[0]
        bold_font_family = font_db.applicationFontFamilies(bold_font_id)[0]

        self.regular_font = QFont(regular_font_family)
        self.bold_font = QFont(bold_font_family)

        self.setFont(self.regular_font)

        # Layout principal
        self.layout = QVBoxLayout()

        self.texto_entrada_label = QLabel("Texto a ser traduzido:")
        self.texto_entrada_label.setFont(self.bold_font)
        self.texto_entrada_label.setStyleSheet("font-size: 14px;")
        self.layout.addWidget(self.texto_entrada_label)

        self.texto_entrada = QTextEdit(self)
        self.texto_entrada.setFixedHeight(100)
        self.texto_entrada.setStyleSheet("font-size: 14px; border-radius: 10px;")
        self.layout.addWidget(self.texto_entrada)

        self.combo_idioma_label = QLabel("Idioma de destino:")
        self.combo_idioma_label.setFont(self.bold_font)
        self.combo_idioma_label.setStyleSheet("font-size: 14px;")
        self.layout.addWidget(self.combo_idioma_label)

        self.combo_idioma = QComboBox(self)
        # idiomas
        self.idiomas = {
            'Inglês': 'en',
            'Espanhol': 'es',
            'Francês': 'fr',
            'Alemão': 'de',
            'Italiano': 'it',
            'Português': 'pt',
            'Chinês': 'zh-cn',
            'Japonês': 'ja',
            'Russo': 'ru',
            'Árabe': 'ar',
            'Hindi': 'hi',
            'Bengali': 'bn',
            'Coreano': 'ko',
            'Sueco': 'sv',
            'Holandês': 'nl',
            'Turco': 'tr',
            'Grego': 'el',
            'Polonês': 'pl',
            'Tailandês': 'th',
            'Vietnamita': 'vi',
            'Indonésio': 'id'
        }
        self.combo_idioma.addItems(self.idiomas.keys())
        self.combo_idioma.setStyleSheet("font-size: 14px; border-radius: 10px;")
        self.layout.addWidget(self.combo_idioma)

        self.botao_traduzir = QPushButton("Traduzir", self)
        self.botao_traduzir.setStyleSheet("font-size: 14px; background-color: #4CAF50; color: white; border-radius: 10px;")
        self.botao_traduzir.clicked.connect(self.traduzir_texto)
        self.layout.addWidget(self.botao_traduzir)

        self.texto_saida_label = QLabel("Texto traduzido:")
        self.texto_saida_label.setFont(self.bold_font)
        self.texto_saida_label.setStyleSheet("font-size: 14px;")
        self.layout.addWidget(self.texto_saida_label)

        self.texto_saida = QTextEdit(self)
        self.texto_saida.setFixedHeight(100)
        self.texto_saida.setReadOnly(True)
        self.texto_saida.setStyleSheet("font-size: 14px; border-radius: 10px;")
        self.layout.addWidget(self.texto_saida)

        self.setLayout(self.layout)

    def traduzir_texto(self):
        texto = self.texto_entrada.toPlainText().strip()
        idioma_selecionado = self.combo_idioma.currentText()
        idioma_destino = self.idiomas.get(idioma_selecionado)

        if texto and idioma_destino:
            try:
                translator = Translator()
                traducao = translator.translate(texto, dest=idioma_destino)

                texto_traduzido = traducao.text

                if hasattr(traducao, 'pronunciation') and traducao.pronunciation:
                    transliteracao = traducao.pronunciation
                else:
                    transliteracao = texto_traduzido 

                texto_final = f"{transliteracao}"

                self.texto_saida.setPlainText(texto_final)

            except Exception as e:
                self.texto_saida.setPlainText(f"Erro na tradução: {str(e)}")
        else:
            self.texto_saida.setPlainText("Erro: Texto ou idioma de destino não selecionados.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tradutor()
    window.show()
    sys.exit(app.exec_())
