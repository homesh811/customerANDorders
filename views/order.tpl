<html>
<body>
<h2>Customer Order List</h2>
<hr/>
<table>
% for order in customer_order:
  <tr>
  <td>{{str(order['product'])}}</td>
  <td>{{str(order['total_amount'])}}</td>
  <td>{{str(order['customer'])}}</td>
  <td><a href="/update2/{{str(order['id'])}}">update2</a></td>
  <td><a href="/delete2/{{str(order['id'])}}">delete2</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add2">Add a new order</a>
<hr/>
</body>
</html>