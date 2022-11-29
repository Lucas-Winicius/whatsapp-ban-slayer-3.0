import smtplib
import email.message


#banner
print ('███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░')
print ('████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗')
print ('██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝')
print ('██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗')
print ('██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║')
print ('╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
print ('                                                     ')
print ('██████╗░░█████╗░███╗░░██╗')
print ('██╔══██╗██╔══██╗████╗░██║')
print ('██████╦╝███████║██╔██╗██║')
print ('██╔══██╗██╔══██║██║╚████║')
print ('██████╦╝██║░░██║██║░╚███║')
print ('╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝')
print ('                                                     ')
#prime 
print ('█▀█ █▀█ █ █▀▄▀█ █▀▀')
print ('█▀▀ █▀▄ █ █░▀░█ ██▄')
print ('                       ')

#banner by
print ('█▀▀▄ █░░█ 　 █▀▀ █░░ █▀▀█ █░░█ █▀▀ █▀▀█ ')
print ('█▀▀▄ █▄▄█ 　 ▀▀█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀ ')
print ('▀▀▀░ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀ ')



#auto

a = input('coloque o numero q vc quer derrubar:')
b = input('coloque o seu email:')
#email
def enviar_email():
    corpo_email = f'Olá suporte do whatsapp, meu filho sofreu abuso deste numero {a} em seu app!!, muitas crianças vem recebendo nudes e pornografia deste numero!!, ja denunciamos mas nada funciona, infelizmente. para melhor contato fale comigo por este email {b}, tenho print para provar dos abusos que meu filho sofreu!, tem ate uma das fotos pornograficas que meu filho recebeu!, links: https://drive.google.com/file/d/1iJrqn_SkiLs5VmVnIWjnBhqAz5m1beyT/view?usp=sharing // https://drive.google.com/file/d/1wD_qS4y8NMDM0CL8XYv3EbYPxgTZJczq/view?usp=sharing'
    
 
    msg = email.message.Message()
    msg['Subject'] = 'Olá suporte do whatsapp!'
    msg['From'] = 'cleber.santos9983sl@gmail.com'
    msg['To'] = 'slayerandkr@gmail.com'
    password = 'sulxglmlsjbndavn'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('o numero sera banido em breve.')

enviar_email()
#fecho email

#denuncia 
print ('''
█▀▄ █▀▀ █▄░█ █░█ █▄░█ █▀▀ █ █▀▀   █▀█   █▄░█ █░█ █▀▄▀█ █▀▀ █▀█ █▀█   █▀   █▀█ █░█   ▄█ █▀█   █░█ █▀▀ ▀█ █▀▀ █▀ ░
█▄▀ ██▄ █░▀█ █▄█ █░▀█ █▄▄ █ ██▄   █▄█   █░▀█ █▄█ █░▀░█ ██▄ █▀▄ █▄█   ▄█   █▄█ █▄█   ░█ █▄█   ▀▄▀ ██▄ █▄ ██▄ ▄█ ▄''')


print ('''
░██████╗██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░██╗
██╔════╝██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗██║
╚█████╗░██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝██║
░╚═══██╗██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗╚═╝
██████╔╝███████╗██║░░██║░░░██║░░░███████╗██║░░██║██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝''')
print ('                              ')
#acabou :)