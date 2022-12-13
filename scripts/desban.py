import smtplib
import email.message
from modules import sendEmail, questions
import json


#banner
print ('███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░')
print ('████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗')
print ('██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝')
print ('██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗')
print ('██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║')
print ('╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
print ('                                                     ')
print ('██████╗░███████╗░██████╗██████╗░░█████╗░███╗░░██╗')
print ('██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░██║')
print ('██║░░██║█████╗░░╚█████╗░██████╦╝███████║██╔██╗██║')
print ('██║░░██║██╔══╝░░░╚═══██╗██╔══██╗██╔══██║██║╚████║')
print ('██████╔╝███████╗██████╔╝██████╦╝██║░░██║██║░╚███║')
print ('╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝')
print ('                                                     ')

#banner by
print ('█▀▀▄ █░░█ 　 █▀▀ █░░ █▀▀█ █░░█ █▀▀ █▀▀█ ')
print ('█▀▀▄ █▄▄█ 　 ▀▀█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀ ')
print ('▀▀▀░ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀ ')



try:
    with open('settings.json') as file:
        data = json.load(file)

except:
    retorno = questions.conjunto_1()

    f = open("settings.json", "w")
    f.write(json.dumps({"Email": retorno['email'], "Pass": retorno['senha']}))
    f.close()

    sendEmail.enviar_UnBanMail(retorno['email'], retorno['senha'], retorno['numero'])

else:
    choice = str(input('Encontrei uma config que foi ultilizada anteriormente deseja usa-la? (s/n)')).lower()

    if(choice == 'n'):

        retorno = questions.conjunto_1()

        sendEmail.enviar_UnBanMail(retorno['email'], retorno['senha'], retorno['numero'])

    elif(choice == 's'):
        a = input('coloque o numero q vc quer derrubar +55 (12) 12345-6789:')

        sendEmail.enviar_UnBanMail(data['Email'], data['Pass'], a)