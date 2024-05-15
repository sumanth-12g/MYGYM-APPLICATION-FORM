import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def submit(name,weight,address,personal):
  app_tables.gym.add_row(name=name,weight=weight,address=address,personal=personal)
  anvil.email.send(from_name="MYGYM FORM",
                 to="sumanthusorab@gmail.com",
                 subject="Your form",
                 text= f"submission from {name}, the weight is {weight} and address is {address} and he needs personal training : {personal}")
                



