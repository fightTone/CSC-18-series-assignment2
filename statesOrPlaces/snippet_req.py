from pprint import pprint
import requests, json



while (True):
	choice = raw_input("[GET] [POST] [PUT] [DELETE] [X]\n\n>>>")
	if choice == 'GET':
		x=raw_input("[A] -for All\n[B] -searching for a specific Place\n[x] -Exit\n\n>>>")
		if x == 'A':
			req = requests.get("http://127.0.0.1:8080/results")
			obj=req.json()
			print(pprint(obj))
		elif x == 'B':
			name=raw_input("enter the name of place/states:")
			req = requests.get("http://127.0.0.1:8080/places="+name)
			obj=req.json()
			print(pprint(obj))
		elif x=='X':
			pass
	elif choice == 'POST':
		area_codes = []
		name  = raw_input("name of place/state: ")
		abbreviation  = raw_input("abbreviation: ")
		add = 'Y'
		while (add == 'Y'):
			code  = raw_input("area code: ")
			area_codes.append(code)
			stop = raw_input("Do u want to add more? (Y/N)\n>>>")
			if stop == 'N':
				add = stop
		
		print "\nUse GET to check results"
		req = requests.post("http://127.0.0.1:8080/places", json = {'name':name, 'abbreviation':abbreviation, 'area_codes':area_codes}) 

	elif choice == 'PUT':
		area_codes = []
		name = raw_input("enter name of place/state: ")
		print "\nCHANGES:\n"
		newname = raw_input("place/state:")
		abbreviation = raw_input("abbreviation: ")
		add = 'Y'
		while (add == 'Y'):
			code  = raw_input("area code: ")
			area_codes.append(code)
			stop = raw_input("Do u want to add more? (Y/N)\n>>>")
			if stop == 'N':
				add = stop

		print "\nUse GET to check results"
		req = requests.put("http://127.0.0.1:8080/places="+name, json={'name':newname, 'abbreviation':abbreviation, 'area_codes':area_codes})

	elif choice == "DELETE":
		name = raw_input("enter name of place/state: ")
		print "\nUse GET to check results"
		req = requests.delete("http://127.0.0.1:8080/places="+name)

	elif choice =='X':
		break