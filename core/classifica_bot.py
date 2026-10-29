from core.audio import BotAudio
from core.bot_imagem import BotImagem


class ClassificaBot(BotImagem, BotAudio):

    def __init__(self, token=None):
            super().__init__(token)  # 👈 Executa a cadeia: ClassificaBot -> BotImagem -> BotAudio -> BotTelegram
            