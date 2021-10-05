import pyttsx3

# Faz o carregamento da lib 
engine = pyttsx3.init()

# Texto em que a maquina vai ler
ads = engine.say(input('Digite o que você deseja falar: '))

# Executa a leitura do texto #
engine.runAndWait()

