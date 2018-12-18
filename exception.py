def exception():
	car = {'make':'BMW','model':'ZS35F','year':1930}
	try:
		print(car['car'])
	except:
		print("Exception occured")
	finally:
		print("The result been shown above")
exception()