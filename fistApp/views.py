from django.shortcuts import render
from . import datas
import smtplib,ssl


def wish(request):
    page2 = 0
    res = str(request)
    z, y = res.split("//")
    print(y)
    if y == "App1'>":
        page2 = datas.App1
    elif y == "Web3'>":
        page2 = datas.web3
    elif y == "App2'>":
        page2 = datas.App2
    elif y == "Card2'>":
        page2 = datas.card2
    elif y == "Web2'>":
        page2 = datas.web2
    elif y == "App3'>":
        page2 = datas.App3
    elif y == "Card1'>":
        page2 = datas.card1
    elif y == "Card3'>":
        page2 = datas.card3
    elif y == "Web3'>":
        page2 = datas.Web3
    print(page2)
    return render(request, 'portfolio-details.html', page2)
def welcome(request):
    return render(request, 'index.html', datas.display)
def done(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    des= name+email+subject+message
    print(des)
    mail= "rockeytma@gmail.com"

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = mail
    receiver_email = "tmarakesh@gmail.com"
    password = datas.pa
    message = des

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return render(request, 'done.html')
