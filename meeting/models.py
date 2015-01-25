from django.db import models

class Meeting(models.Model):
  topic = models.CharField(max_length=500)
  start_date = models.DateTimeField('date started')
  end_date = models.DateTimeField('date ended', null=True)
  
  def __str__(self):
    return "meeting id: %d, start: %s, end: %s" % (self.id, self.start_date, self.topic)

class Content(models.Model):
  meeting = models.ForeignKey(Meeting)

  user = models.CharField(max_length=100)
  text = models.CharField(max_length=2000)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return "%s -- %s in meeting:%d" % (self.pub_date, self.user, self.meeting.id)

