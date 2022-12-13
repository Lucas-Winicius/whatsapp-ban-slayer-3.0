import smtplib
import email.message as message

def enviar_banMail(email, senha, numero):
    corpo_email = f'Olá suporte do whatsapp, sou mãe de um menino que foi abusado virtualmente por este numero {numero} meu filho nao foi o unico!!'
    
 
    msg = message.Message()
    msg['Subject'] = 'Olá suporte do whatsapp!'
    msg['From'] = f'{email}'
    msg['To'] = 'support@whatsapp.com'
    password = f'{senha}'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail

    # VERIFICA SE FOI POSSIVEL CONECTAR COM O EMAIL INSERIDO
    try:
        s.login(msg['From'], password)
    except:
        print('Verifique seu login google e tente novamente.')

    # VERIFICA SE E POSSIVEL ENVIAR O EMAIL 
    try:
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    except:
        print('Houve um erro ao enviar o email.')

    else:
        print('o numero sera banido em breve.')

def enviar_UnBanMail(email, senha, numero):
    corpo_email = f'Olá suporte do whatsapp, meu numero foi banido de forma injusta!!, por meios ilegais. Solicito o desbanimento do mesmo, o numero é {numero}'
 
    msg = message.Message()
    msg['Subject'] = 'Olá suporte do whatsapp!'
    msg['From'] = f'{email}'
    msg['To'] = 'support@whatsapp.com'
    password = f'{senha}'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    try:
        s.login(msg['From'], password)
    except:
        print('Verifique seu login google e tente novamente.')

    try:
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    except:
        print('Houve um erro ao enviar o email.')

    else:
        print('o numero sera desbanido em breve.')