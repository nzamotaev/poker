<h1>Комнаты</h1>
<table border=1>
<tr><td>Имя комнаты</td><td>Ключ доступа</td><td>Дата создания</td><td>Владелец</td><td>Vote ID</td></tr>
%for i in data:
<tr><td>{{i[4]}}</td><td><a href="/poker/room/{{i[2]}}">{{i[2]}}</a></td><td>{{i[3]}}</td><td>{{i[1]}}</td><td>{{i[5]}}</td></tr>
%end
</table>
