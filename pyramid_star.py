def star_pyramid():
	
	for i in range(1,6):
    		for j in range(1, i + 1):
        		print("*", end=' ')
    		print("\r")

	for i in range(6, 0, -1):
    		for j in range(1, i - 1):
        		print("*", end=' ')
    		print("\r")
	


star_pyramid()
