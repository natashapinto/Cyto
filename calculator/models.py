from django.db import models

# Create your models

class Region(models.Model):
	Red_Probe_Region = models.CharField(max_length=100)
	Green_Probe_Region = models.CharField(max_length=100)


class Signal(models.Model):
	RedProbe=models.IntegerField(
		default=1)
	GreenSignal=models.IntegerField(
		default=1)
	NoOfCells=models.IntegerField(
		default=1)


