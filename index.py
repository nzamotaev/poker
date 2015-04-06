#!/usr/bin/env python
# coding=utf-8
import bottle
from bottle import route, view, request, template, static_file, response, abort, redirect
import uuid
import datetime
import time
from my_db import db_exec_sql
import gpw

vote_value = ["?", "1", "2", "3", "5", "8", "13", "21", "40", "100", "Перерыв"]

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
	result = db_exec_sql('select name from names where uuid = ?', (str(user_uuid),))
	if result:
		user_uuid = result[0][0]
	return dict(user_uuid=user_uuid)

@route('/createroom/', method="POST")
def createroom():
	accesskey=gpw.GPW(10).password
	user_uuid= uuid_generate_and_set()
	name= request.forms.get('roomname')
	t=(str(user_uuid),accesskey,name,)
	db_exec_sql('insert into rooms (creator_uuid, accesskey,name) values ( ?, ?, ?)', t)
	redirect("/poker/rooms/")

@route('/rooms/')
@view('rooms')
def show_rooms():
	user_uuid = uuid_generate_and_set()
	t=(str(user_uuid),)
	result = db_exec_sql("select * from rooms where creator_uuid = ? ", t)
	return dict(data=result)

@route('/room/<roomid>')
@route('/room/<roomid>/')
@route('/room/', method="POST")
@view('room')
def show_room(roomid=None):
	user_uuid = uuid_generate_and_set()
	if not roomid:
		roomid = request.forms.get('roomid')
	user_uuid = uuid_generate_and_set()
	result = db_exec_sql('select * from rooms where accesskey = ?', (roomid,))
	if result:
		ttl=result[0][3]
		tdate=time.mktime(time.strptime(ttl,'%Y-%m-%d %H:%M:%S'))
		cdate=time.time()
		#CREATE TABLE votes (id integer primary key autoincrement not null, voter_uuid text not null, room_id integer not null, vote_id integer not null, value integer not null, date datetime not null default current_timestamp);
		votes = db_exec_sql('select id,voter_uuid,room_id,vote_id,value,date from votes where room_id = ? and vote_id = ?  group by voter_uuid', (roomid,result[0][5],))
		votes1 = []
		for i in votes:
			#find names
			name = db_exec_sql('select name from names where uuid = ?', (i[1],))
			if name:
				i=[i[0],name[0][0],i[2],i[3],i[4],i[5]]
			votes1.append(i)
			pass
			
		bump = (str(user_uuid) == str(result[0][1]))
		return dict(ttl=str(tdate-cdate+86400),roomname=result[0][4],roomid=roomid,vote_id=result[0][5],votes=votes1,bump=bump, vote_decode=vote_value)
	else:
		redirect("/poker/")

@route('/setname/', method="POST")
def set_name():
	user_uuid = uuid_generate_and_set()
	name = request.forms.get('name')
	db_exec_sql('insert or replace into names (uuid, name) values (?, ?)',(str(user_uuid), name,))
	redirect("/poker/")

@route('/room/<roomid>/vote/<vote>')
def accept_vote(roomid,vote):
	user_uuid = uuid_generate_and_set()
	if int(vote) in range(0,11):
		result = db_exec_sql('select * from rooms where accesskey = ?', (roomid,))
		if result:
			db_exec_sql('insert or replace into votes (voter_uuid, room_id, vote_id, value) values (?, ?, ?, ?)', (str(user_uuid), roomid, result[0][5],vote))
	redirect("/poker/room/"+roomid)

@route('/room/<roomid>/bump')
def bump_room(roomid):
	result=db_exec_sql('select vote_id from rooms where accesskey = ?',(roomid,))
	vote_id=result[0][0]+1
	db_exec_sql('update rooms set vote_id=? where accesskey = ?',(vote_id,roomid,))
	redirect("/poker/room/"+roomid)

def cleanup():
	pass

bottle.run(server=bottle.CGIServer)
