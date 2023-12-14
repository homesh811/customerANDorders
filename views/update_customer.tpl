<html>
<body>
<hr/>
<form action="/update1" method="post">
  <input type="hidden" name="id" value="{{str(customer['id'])}}"/>
  <p>first_name:<input name="first_name" value="{{customer['first_name']}}"/></p>
  <p>last_name:<input name="last_name" value="{{customer['last_name']}}"/></p>
  <p>country:<input name="country" value="{{customer['country']}}"/></p>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>