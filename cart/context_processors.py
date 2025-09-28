from .cart import Cart

# Create a cart_processor so that our cart can work on all pages of website
def cart(request):
	# Return the default data from our cart
	return {'cart': Cart(request)}