from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from haiwai.models import HaiwaiDevicePlay, HaiwaiSetting
import django.utils.timezone as timezone

import json
import logging

USER_NOT_FOUND = 10001
USER_EXISTS = 10002
USER_NOT_ACTIVE = 10003

logger = logging.getLogger(__name__)

def res_json(data):
	return HttpResponse(json.dumps(data),content_type='application/json')

@login_required
def my_view(request):
	user = request.user
	return HttpResponse("hello "+ user.username)

@csrf_exempt
def sign_up(request):
	data ={'success':False}
	try:
		username = request.POST['username']
		password = request.POST['password']
		email = "default@email.com"
		logger.debug('username: '+ username)
		if User.objects.filter(username = username).exists():
			data ={'Error':USER_EXISTS, 'Msg':'user name exists.'}
			return res_json(data)
		else:
			user = User.objects.create_user(username, email, password)
			user.save()
			data ={'success':True}
	except Exception, e:
		logger.debug('error: '+ e)
	finally:
		return res_json(data)
	

@csrf_exempt
def login_view(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		data ={'success':False}
		user = authenticate(username = username , password = password )
		if user is not None:
			if user.is_active:
				login(request, user)
				data ={'success':True}	
			else:
				data ={'Error':USER_NOT_ACTIVE, 'Msg':'user is not active.'}
		else:
			data ={'Error':USER_NOT_FOUND, 'Msg':'User not found'}
	except Exception, e:
		logger.error(e)
	finally:
		return res_json(data)
	
	return res_json(data)

def logout_view(request):
	logout(request)
	return HttpResponse("user has logout ")

def get_setting():
	setting = HaiwaiSetting.objects.get(pk=1)
	return setting
	

def device_play_view(request, device):
	d = HaiwaiDevicePlay.objects.filter(device= device, date = timezone.now())
	if d.exists():
		d = HaiwaiDevicePlay.objects.get(device = device, date = timezone.now())
		d.auto_pv()
		d.save()
	else:
		d = HaiwaiDevicePlay(date = timezone.now(), device = device,play_times = 1, create_time =timezone.now(), update_time=timezone.now())
		d.save()

	setting = get_setting()

	data ={'times':  setting.device_play_times - d.play_times}
	return res_json(data)

def user_play_view(request):
	pass

def vip_play_view(request):
	pass

def product_view(request):
	pass

def check_vip(request):
	pass
