order_file=open('customer-orders.txt')

def account_discrepancies(order_file):
  """Determine if which customers have over or underpaid."""

  melon_cost = 1.00
  number_of_unreconciled_customers = 0
  
  for line in order_file:
    line = line.rstrip()
    words = line.split('|')

    customer_number = words [0]
    customer_name = words [1]
    melons_purchased = float(words [2])
    customer_paid = float(words [3]) 
    expected_payment=(melons_purchased * melon_cost)
    
    if customer_paid != expected_payment:
      print (f'{customer_name} paid ${customer_paid},', f'expected ${expected_payment}')
      number_of_unreconciled_customers += 1

  return number_of_unreconciled_customers

print (f'There are {account_discrepancies(order_file)} accounts not reconciled.')

