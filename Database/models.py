from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Data(models.Model):
    STATUS_CHOICE=(('unknown','Unknown'),
                   ('awaited','Awaited'),
                   ('waiting','Waiting'),
                   ('returned','Returned'),
                   ('clear','Clear'),
                   ('checked','Checked') 
                   )
    
    Candidate=models.ForeignKey(User,
                         on_delete=models.CASCADE,
                         related_name='Database')
    Post=models.CharField(max_length=250)
    Account=models.TextField()
    Status=models.CharField(max_length=10,
                            choices=STATUS_CHOICE,
                            default='Unknown')
    URL=models.SlugField(max_length=250,
                         unique_for_date='Designated')
    Designated=models.DateTimeField(default=timezone.now)
    Created=models.DateTimeField(auto_now_add=True)
    Updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'AMURoboclub_Database'
        ordering=('Designated',)
        
    def _str_(self):
        return self.title




