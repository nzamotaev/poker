<h1>Welcome {{user_uuid}}</h1>

<form action="./createroom/" method=POST>
	Имя комнаты<input type="text" name="roomname"><br>
	<input type="submit" value="Создать комнату">
</form>
<form action="./room/" method=POST>
	Идентификатор комнаты<input type="text" name="roomid">
	<input type="submit" value="Войти в комнату">
</form>
<form action="./setname/" method=POST>
	Имя пользователя<input type="text" name="name">
	<input type="submit" value="Назначить имя">
</form>
<a href="./rooms/"><button>Мои комнаты</button></a>
<br />

