def results(request):
	if request.method == 'POST':
		Cells = request.POST.get("^No. of cells")
		Sumofcells = sum(Cells)
		return render(request, 'calculator/results.html', {Sumofcells})

'''	template = loader.get_template('calculator/index.html')
	#count total sum 
	Cells = request.POST.get('No. of cells')
	#numbersum = sum(Cells)
	#print(numbersum)
	return render(request, 'calculator/results.html', {})
	'''
#	var signal = ('^No. of cells' >= (0.25*50));
#
#	if var totalsum == 50:
#		continue 
#	else:
#		print("Error: A minimum of 50 cells need to be checked")


'''def results(red, green):
				if (red == 1 and green == 2):
					print ("Absolute deletion")
				if (red/green == 0.5):
					print ("Relative deletion")
    			elif (red/green == 1):
    				print("Polysomy")+
    			elif (red/green == 2):
    				print("Normal")
    			else
    				print("Signal Imbalance")'''
