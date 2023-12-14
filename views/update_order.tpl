<html>
<body>
<hr/>
<form action="/update2" method="post">
  <input type="hidden" name="id" value="{{str(order['id'])}}"/>
  <p>product:<input name="product" value="{{order['product']}}"/></p>
  <p>total_amount:<input name="total_amount" value="{{order['total_amount']}}"/></p>

  customer: 
  <select name="customerId">
  % for customer in customers:
    <option value="{{customer["id"]}}">{{customer["first_name"]}} {{customer["last_name"]}}</option>
  % end
  </select>
  </p>

  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>