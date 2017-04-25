from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone 

class HaiwaiVip(models.Model):
	user = models.ForeignKey(User)
	expired_date = models.DateField()
	first_credit_time = models.DateTimeField()
	last_credit_time = models.DateTimeField()
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()

class HaiwaiProduct(models.Model):
	name = models.CharField(max_length=30)
	price = models.IntegerField()
	currency = models.CharField(max_length=20)
	status = models.IntegerField()
	desc = models.CharField(max_length=128)
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()

class HaiwaiOrder(models.Model):
	user = models.ForeignKey(User)
	status = models.IntegerField()
	pay_type = models.IntegerField()
	product = models.ForeignKey(HaiwaiProduct)
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()

class HaiwaiDevicePlay(models.Model):
	date = models.DateField()
	device = models.CharField(max_length=64)
	play_times = models.IntegerField()
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()

	def auto_pv(self):
		self.play_times += 1

class HaiwaiUserPlay(models.Model):
	date = models.DateField()
	user = models.ForeignKey(User)
	play_times = models.IntegerField()
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()

class HaiwaiVipPlay(models.Model):
	date = models.DateField()
	user = models.ForeignKey(User)
	play_times = models.IntegerField()
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()

class HaiwaiSetting(models.Model):
	device_play_times = models.IntegerField()
	vip_play_times = models.IntegerField()
	user_play_times = models.IntegerField()
	device_max_times = models.IntegerField()
	vip_max_times = models.IntegerField()
	user_max_times = models.IntegerField()




		

