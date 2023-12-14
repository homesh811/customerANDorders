<html>
<body>
<hr/>
<form action="/add2" method="post">
  <p>product:<input name="product"/></p>
  <p>total_amount:<input name="total_amount"/></p>
  customer: 
  <select name="customerId">
  % for customer in customers:
    <option value="{{customer["id"]}}">{{customer["first_name"]}} {{customer["last_name"]}}</option>
  % end
  </select>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>