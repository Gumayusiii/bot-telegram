from typing import TextIO
import telebot

CHAVE_API = "5485930751:AAHiaL0DuwGLH3BFmNzaSwq20JtWI_KEEpA"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["sorvete"])
def sorvete(mensagem):
     bot.send_message(mensagem.chat.id, "Saindo o sorvete para sua casa: Tempo de espera em 10 minutos")

@bot.message_handler(commands=["picole"])
def picole(mensagem):
     bot.send_message(mensagem.chat.id, "Saindo o Picolé para sua casa: Tempo de espera em 5 minutos")


@bot.message_handler(commands=["acai"])
def acai(mensagem):
     bot.send_message(mensagem.chat.id, "Saindo o Açaí para sua casa: Tempo de espera em 20 minutos")



@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem): 
    texto = """
    O que você quer? (Clique em uma das opções)
    /sorvete Sorvete
    /picole Picolé
    /acai Açaí"""
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem): 
    bot.send_message(mensagem.chat.id, "Para eviar uma reclamação, mande um email para marcelo.damasceno@ifrn.edu.br")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem): 
    bot.send_message(mensagem.chat.id, "Tmj, um forte abraço!")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem): 
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraço 
    Responder qualquer outra coisa não irá funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem, texto) 




bot.polling()