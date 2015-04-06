<html>
<head>
<meta http-equiv="refresh" content="5;/poker/room/{{roomid}}">
</head>
<body>
<h1>Комната {{roomname}}</h1>
Оставшееся время жизни {{ttl}} секунд
<br>
<a href="/poker/"><button>На главную</button></a>
<h2>Текущий номер голосования</h2>
{{vote_id}}
<h2>Голоса</h2>
%for i in xrange(0,len(vote_decode)):
<a href="/poker/room/{{roomid}}/vote/{{i}}"><button>{{vote_decode[i]}}</button></a>
%end
<br>
<br>
<table border=1>
<tr><td>Пользователь</td><td>Голос</td><td>Время</td></tr>
%for i in votes:
<tr><td>{{i[1]}}</td><td>{{vote_decode[int(i[4])]}}</td><td>{{i[5]}}</td></tr>
%end
</table>
<br>
%if bump:
<a href="/poker/room/{{roomid}}/bump"><button>Следующее голосование</button></a>
%end
</body>
</html>
