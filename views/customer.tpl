<html>
<body>
<h2>Customer Order List</h2>
<hr/>
<form action="/customer" method="get">
  <input type="text" name="key" value="{{key}}"/>
  <button type="submit">Search</button>
</form>
<table>
% for customer in customer_order:
  <tr>
  <td>{{str(customer['first_name'])}}</td>
  <td>{{str(customer['last_name'])}}</td>
  <td>{{str(customer['country'])}}</td>
  <td><a href="/update1/{{str(customer['id'])}}">update1</a></td>
  <td><a href="/delete1/{{str(customer['id'])}}">delete1</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add1">Add a new customer</a>
<hr/>
</body>
</html>