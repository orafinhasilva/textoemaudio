import pyttsx3

# Faz o carregamento da lib 
engine = pyttsx3.init()

# Converte o texto inserido no campo em áudio
ads = engine.say(input('Digite o que você deseja falar: '))

# Executa a leitura do texto #
engine.runAndWait()

