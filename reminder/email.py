from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_reminder_mail(user,friends_name,receiver):
  subject = 'Birthday Reminder'
  sender = 'alfred.kahenya@student.moringaschool.com'
  
  text_content = render_to_string('email/remindermail.txt',{"name":user,"friend":friends_name})
  html_content = render_to_string('email/reminderemail.html',{"name":user,"friend":friends_name})
  
  message = EmailMultiAlternatives(subject,text_content,sender,[receiver])
  message.attach_alternative(html_content,'text/html')
  message.send()