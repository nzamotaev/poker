#!/usr/bin/env python
# coding=utf-8
import bottle
from bottle import route, view, request, template, static_file, response, abort, redirect
import uuid
import datetime
import time
from my_db import db_exec_sql
import gpw

def uuid_generate_and_set():
	user_uuid = request.get_cookie("user_uuid", secret='some-secret-key1')
	if not user_uuid:
		user_uuid = uuid.uuid4()
		response.set_cookie("user_uuid", user_uuid, secret='some-secret-key1')
	return user_uuid

@route('/')
@view('mainpage')
def mainpage():
	user_uuid = uuid_generate_and_set()
	return dict(user_uuid=user_uuid)

@route('/createroom/', method="POST")
def createroom():
	accesskey=gpw.GPW(10).password
	user_uuid= uuid_generate_and_set()
	t=(str(user_uuid),accesskey,)
	db_exec_sql('insert into rooms (creator_uuid, accesskey) values ( ?, ?)', t)
	return accesskey

@route('/rooms/')
def show_rooms():
	user_uuid = uuid_generate_and_set()
	t=(str(user_uuid),)
	result = db_exec_sql("select * from rooms where creator_uuid = ? ", t)
	return str(result)

@route('/room/<roomid>')
@view('room')
def show_room(roomid):
	user_uuid = uuid_generate_and_set()
	result = db_exec_sql('select * from rooms where accesskey = ?', (roomid,))
	if result:
		ttl=result[0][3]
		tdate=time.mktime(time.strptime(ttl,'%Y-%m-%d %H:%M:%S'))
		cdate=time.time()
		return dict(ttl=str(tdate-cdate+86400))
	else:
		return ""

bottle.run(server=bottle.CGIServer)
