import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

import datetime

from meeting.models import Meeting, Content


def index(request):
  return HttpResponse("hello")

def meeting_start(request):
  topic = ''
  start_time = datetime.datetime.now()

  meeting = Meeting.objects.create(topic=topic, start_date=start_time)
  return HttpResponse(meeting.id)

def meeting(request):
  content_text = request.POST['content']
  user = request.POST['user']
  meeting_id = Meeting.objects.get(id=meeting_id)
  pub_date = datetime.datetime.now()

  content = Content.objects.create(meeting=meeting, user=user, text=content_text, pub_date=pub_date)

  return HttpResponse(content.pk)

def meeting_end(request):
  meeting_id = request.GET['meeting_id']
  meeting = Meeting.objects.get(id=meeting_id)
  meeting.end_date = datetime.datetime.now()
  dialogs = Content.objects.filter(meeting__id=meeting_id).order_by('pub_date')
  
  summary = topic = ''
  for dialog in dialogs:
    if 'summary' in dialog.text.lower():
      summary = dialog.text.split('summary')[1:]
      summary = ''.join(summary)
    if 'topic' in dialog.text.lower():
      topic = dialog.text.split('topic')[1:]
      topic = ''.join(topic)

  meeting.topic = topic
  meeting.save()

  to_list = {d.user for d in dialogs}
  subject = 'Meeting Minutes'
  from_email = 'hisoka_k@icloud.com'
  
  con = Context({'dialogs': dialogs, 'topic': topic, 'summary': summary, 'start_date': meeting.start_date, 'end_date':meeting.end_date})
  htmly = get_template('email.html')
  plaintext = get_template('email.txt')
  html_content = htmly.render(con)
  text_content = plaintext.render(con)
  
  msg = EmailMultiAlternatives(subject, text_content, from_email, to_list)
  msg.attach_alternative(html_content, "text/html")
  msg.send()

  return HttpResponse('ok')

def meeting_content(request):
  meeting_id = request.GET['meeting_id']
  user = reqeust.GET['user']
  content_id = request.GET['content_id']

  contents = Content.objects.filter(meeting__id=meeting_id, pk__gt=content_id).exclude(user=user).order_by('pub_date')

  contents_json = serializers.serialize('json', contents)
  return HttpResponse(contents_json, content_type='applicatoin/json')






