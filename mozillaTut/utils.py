from django.core.mail import send_mail

'''
para: é uma lista de destinatários.
'''
def send_prf_mail(assunto, mensagem, para):
    send_mail(assunto, mensagem, 'rodrigo.nogueira@prf.gov.br', para, fail_silently=False)
