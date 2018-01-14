from django.db import models
from django.contrib.auth.models import User

class Forum_subject(models.Model):
    title = models.TextField(default = '')
#    total_message_count = models.DecimalField(default = 0)
    last_update = models.DateTimeField()
	
	
class Forum_account(User):
    pass
	
	
class Forum_message(models.Model):
    subject = models.ForeignKey(Forum_subject, default = None, null = True, on_delete = models.CASCADE)
    author = models.ForeignKey(Forum_account, default = None, null = True, on_delete = models.CASCADE)
    content = models.TextField(default = '')
    date_of_submission = models.DateTimeField()
	
    

