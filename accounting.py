#defining Global variable
MELON_COST = 1.00

#opening file
#order_file=open('customer-orders.txt')

#defining function
def account_discrepancies(order_file):
  """Determine if which customers have over or underpaid."""

  #open customer file
  customer_order_file = open(order_file)

  #counter for accounts that need action
  number_of_unreconciled_customers = 0
  
  #Iterate over file, using | to split variables
  for line in customer_order_file:
    line = line.rstrip()
    words = line.split('|')

  #assigning attributes from file to variables
    customer_number = words [0]
    customer_name = words [1]
    melons_purchased = float(words [2])
    customer_paid = float(words [3]) 

  #equations for how much customer paid and their balance
    expected_payment=(melons_purchased * MELON_COST)
    customer_balance  = round((expected_payment-customer_paid),2)
    
  #determine customers that over/underpaid and give exact details  
    if customer_paid != expected_payment:
      number_of_unreconciled_customers += 1

      if customer_paid > expected_payment:
        print (f'{customer_name} overpaid. Paid ${customer_paid},', f'expected ${expected_payment},', f'balance is ${customer_balance}.')   

      if customer_paid < expected_payment:
        print (f'{customer_name} underpaid. Paid ${customer_paid},', f'expected ${expected_payment},', f'balance is ${customer_balance}.')

  #close file
  customer_order_file.close()

  #return tally of outstanding accounts      
  return number_of_unreconciled_customers
#call function
print (f'There are {account_discrepancies("customer-orders.txt")} accounts not reconciled.')

