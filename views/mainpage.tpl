<h1>Welcome {{user_uuid}}</h1>

<form action="./createroom/" method=POST>
	Имя комнаты<input type="text" name="roomname"><br>
	<input type="submit" value="Создать комнату">
</form>
<form>
	Идентификатор комнаты<input type="text" name="roomid">
	<input type="submit" value="Войти в комнату">
</form>
<a href="./rooms/">Мои комнаты</a>
<br />

