from django.db import models

class House(models.Model):
    number   = models.CharField(max_length=45, unique=True)
    password = models.TextField(max_length=2000)
    user     = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'houses'
    
class DoorUseLog(models.Model):
    created_at   = models.DateTimeField(auto_now_add=True)
    house_number = models.ForeignKey('House', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'door_use_logs'