from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import *
import re
import pdfkit

# Create your views here.
def index(request):
	Error = {}
	Form = {}
	HighestSignal = []
	Sumofcells = []
	Cells = []
	Results = []
	Finalsignal = []
	high = {}
	Probe = []
	MainProbe = {}
	Region = []
	X = ()
	Classification = {}
	RedSignal = {}
	RS = {}
	RS1 = ()
	RS2 = ()
	RS3 = ()
	RS4 = ()
	RS5 = ()
	RS6 = ()
	RS7 = ()
	RS8 = ()
	RS9 = ()
	RS10 = ()
	GS1 = ()
	GS2 = ()
	GS3 = ()
	GS4 = ()
	GS5 = ()
	GS6 = ()
	GS7 = ()
	GS8 = ()
	GS9 = ()
	GS10 = ()
	Cells = ()
	Cells2 = ()
	RedSignals = ()
	RedSignals_2 = ()
	GreenSignals = ()
	GreenSignals_2 = ()
	CS1 = ()
	CS2 = ()
	CS3 = ()
	CS4 = ()
	CS5 = ()
	CS6 = ()
	CS7 = ()
	CS8 = ()
	CS9 = ()
	CS10 = ()
	Patient_name = ()
	Hospital = ()
	NHS = ()
	Checker = ()
	Imbalance = ()

	# POST method used in index.html to retrieve data from the form.

	if request.method == 'POST':

	# Retrieving Patient information 

		Patient_name = request.POST.get("Patient")
		Hospital = request.POST.get("Hospital")
		NHS = request.POST.get("NHS")
		Checker = request.POST.get("Checker")

	#return render(request, 'calculator/index.html', {'PN': Patient_name})

	# List of number of cells with signals 
		Cells = (request.POST.get("No. of cells1"),
		request.POST.get("No. of cells2"),
		request.POST.get("No. of cells3"),
		request.POST.get("No. of cells4"),
		request.POST.get("No. of cells5"),
		request.POST.get("No. of cells6"),
		request.POST.get("No. of cells7"),
		request.POST.get("No. of cells8"),
		request.POST.get("No. of cells9"),
		request.POST.get("No. of cells10"))  

	# Replace any empty fields in the list above and replace with 0, this avoids int() errors. 

		Cells2= [int(0) if v is '' else int(v) for v in Cells]

		CS1 = Cells2[0]
		CS2 = Cells2[1]
		CS3 = Cells2[2]
		CS4 = Cells2[3]
		CS5 = Cells2[4]
		CS6 = Cells2[5]
		CS7 = Cells2[6]
		CS8 = Cells2[7]
		CS9 = Cells2[8]
		CS10 = Cells2[9]

	#return render(request, 'calculator/index.html', {'X': CS4})

	#List containing total Red signals 

		RedSignals = (request.POST.get("Red Signals1"),
		request.POST.get("Red Signals2"),
		request.POST.get("Red Signals3"),
		request.POST.get("Red Signals4"),
		request.POST.get("Red Signals5"),
		request.POST.get("Red Signals6"),
		request.POST.get("Red Signals7"),
		request.POST.get("Red Signals8"),
		request.POST.get("Red Signals9"),
		request.POST.get("Red Signals10"))

		RedSignals_2= [int(0) if v is '' else int(v) for v in RedSignals]

		RS1 = RedSignals_2[0]
		RS2 = RedSignals_2[1]
		RS3 = RedSignals_2[2]
		RS4 = RedSignals_2[3]
		RS5 = RedSignals_2[4]
		RS6 = RedSignals_2[5]
		RS7 = RedSignals_2[6]
		RS8 = RedSignals_2[7]
		RS9 = RedSignals_2[8]
		RS10 = RedSignals_2[9]

		SumRS = (RS1 + RS2 + RS3 + RS4 + RS5 + RS6 + RS7 + RS8 + RS9 + RS10)

	#return render(request, 'calculator/index.html', {'X': RS4})	

		GreenSignals = (request.POST.get("Green Signals1"),
		request.POST.get("Green Signals2"),
		request.POST.get("Green Signals3"),
		request.POST.get("Green Signals4"),
		request.POST.get("Green Signals5"),
		request.POST.get("Green Signals6"),
		request.POST.get("Green Signals7"),
		request.POST.get("Green Signals8"),
		request.POST.get("Green Signals9"),
		request.POST.get("Green Signals10"))

		GreenSignals_2 = [int(0) if v is '' else int(v) for v in GreenSignals]

		GS1 = GreenSignals_2[0]
		GS2 = GreenSignals_2[1]
		GS3 = GreenSignals_2[2]
		GS4 = GreenSignals_2[3]
		GS5 = GreenSignals_2[4]
		GS6 = GreenSignals_2[5]
		GS7 = GreenSignals_2[6]
		GS8 = GreenSignals_2[7]
		GS9 = GreenSignals_2[8]
		GS10 = GreenSignals_2[9]

		SumGS = (GS1 + GS2 + GS3 + GS4 + GS5 + GS6 + GS7 + GS8 + GS9 + GS10)


	#return render(request, 'calculator/index.html', {'X': GreenSignals_2})

	# Dictionary containing all input values, ready to be processed

		Form = {Cells2[0]: (RS1, GS1),
		Cells2[1]: (RS2, GS2),
		Cells[2]: (RS3, GS3),
		Cells2[3]: (RS4, GS4),
		Cells2[2]: (RS3, GS3),
		Cells2[3]: (RS4, GS4),
		Cells2[4]: (RS5, GS5),
		Cells2[5]: (RS6, GS6),
		Cells2[6]: (RS7, GS7),
		Cells2[7]: (RS8, GS8),
		Cells2[8]: (RS9, GS9),
		Cells2[9]: (RS10, GS10)}

	#return render(request, 'calculator/index.html', {'X': Form})

	# Probe names, to used later on.
		Probe = (request.POST.get("Red"),
		request.POST.get("Green"))
		
	# Validating the sum of Cells is 50 
		Sumofcells = sum(Cells2)
		if Sumofcells < 50:
			Error['validation'] = "Error: Minimum of 50 cells need to be checked!"
			return render(request, 'calculator/index.html', Error)
	# If total is 50 find signals in more than 25% of cells 
		elif Sumofcells >= 50:
			pass
		for i in Cells2:
			if i >= 12.5:
				HighestSignal = i
		high = HighestSignal

	# create a dictionary using the highest signal as key to grab respective red and green signals
		if HighestSignal in Form: 
			Finalsignal = Form[HighestSignal]

	# Identifying whch probe has been affected

		for i in Finalsignal:
			if Finalsignal[0] > Finalsignal[1]:
				Region = Probe[0]
			else:
				Region = Probe[1] 
	#return render(request, 'calculator/index.html', {'Probe': Region})

	# Classifing any oberved ratio, according to specification 
		Imbalance = (SumRS/SumGS)

		for i in Finalsignal:
			if Finalsignal[0] == 2 and Finalsignal[1] == 2:
				X = 'No evidence of 1p/19q co-deletion'
			elif Finalsignal[0] == 1 and Finalsignal[1] == 2:
				X = 'Absolute deletion'
			elif Finalsignal[0] == 2 and Finalsignal[1] == 1:
				X = 'Loss of Control'
			elif (Finalsignal[0]/Finalsignal[1]) == 2:
				X = 'Absolute deletion'
			elif (Finalsignal[0]/Finalsignal[1]) == 0.5:
					X = 'Relative deletion'
			elif (Finalsignal[0]/Finalsignal[1]) == 1:
				X = 'Polysomy'
			else:
				X = 'Imbalance'
	
		if X == 'Imbalance' and Imbalance < 0.8:
			X = 'Imbalance'
		else:
			X = 'No evidence of 1p/19q co-deletion'


		#Second = request.POST.get("Second checker")
		#if Second == True 

		if X == 'Imbalance':
			Classification = str(X) + " " + 'of'+ " "+str(Region)+" "+'in'+" "+str(high)+" "+'out of 50 cells'
		else:
			Classification = 'No evidence of 1p/19q co-deletion'

	return render(request, 'calculator/index.html', {'X': Classification, 'RS1': RS1, 'RS2': RS2, 'RS3': RS3, 'RS4': RS4, 'RS5': RS5, 'RS6': RS6, 'RS7': RS7, 
		'RS8': RS8, 'RS9': RS9, 'RS10': RS10, 'GS1': GS1, 'GS2': GS2, 'GS3': GS3, 'GS4': GS4, 'GS5': GS5, 'GS6': GS6,
		'GS7': GS7, 'GS8': GS8, 'GS9': GS9, 'GS10': GS10, 'CS1': CS1, 'CS2': CS2, 'CS3': CS3, 'CS4': CS4, 'CS5': CS5, 
		'CS6': CS6, 'CS7': CS7, 'CS8': CS8, 'CS9': CS9, 'CS10': CS10, 'PN': Patient_name, 'H': Hospital,
		'NHS': NHS, 'Checker': Checker})


def second(request):
	Patient_name = ()
	Hospital = ()
	NHS = ()
	DOB = ()
	Error = {}
	Form = {}
	HighestSignal = []
	Sumofcells = []
	Results = []
	Finalsignal = []
	high = {}
	Probe = []
	MainProbe = {}
	Region = []
	X ={}
	Classification = {}
	RedSignal = {}
	RS1 = ()
	RS2 = ()
	RS3 = ()
	RS4 = ()
	RS5 = ()
	RS6 = ()
	RS7 = ()
	RS8 = ()
	RS9 = ()
	RS10 = ()
	RS11 = ()
	RS12 = ()
	RS13 = ()
	RS14 = ()
	RS15 = ()
	RS16 = ()
	RS17 = ()
	RS18 = ()
	RS19 = ()
	RS20 = ()
	GS1 = ()
	GS2 = ()
	GS3 = ()
	GS4 = ()
	GS5 = ()
	GS6 = ()
	GS7 = ()
	GS8 = ()
	GS9 = ()
	GS10 = ()
	GS11 = ()
	GS12 = ()
	GS13 = ()
	GS14 = ()
	GS15 = ()
	GS16 = ()
	GS17 = ()
	GS18 = ()
	GS19 = ()
	GS20 = ()
	Cells = ()
	Cells2 = ()
	RedSignals = ()
	RedSignals_2 = ()
	GreenSignals = ()
	GreenSignals_2 = ()
	CS1 = ()
	CS2 = ()
	CS3 = ()
	CS4 = ()
	CS5 = ()
	CS6 = ()
	CS7 = ()
	CS8 = ()
	CS9 = ()
	CS10 = ()
	CS11 = ()
	CS12 = ()
	CS13 = ()
	CS14 = ()
	CS15 = ()
	CS16 = ()
	CS17 = ()
	CS18 = ()
	CS19 = ()
	CS20 = ()
	CellsSC = ()
	Signals =()
	RedSignalsSC = ()
	RedSignals_SC2 = ()
	SumRS_SC = ()
	GreenSignalsSC = ()
	GreenSignals_SC2 = ()
	SumGS_SC = ()
	Form_SC = ()
	HighestSignal_SC = ()
	Finalsignal_SC = ()
	Classification_SC = ()
	Checker = ()
	Final_Interpretation = ()
	Region_SC = ()
	Y = ()
	FinalX = ()
	FinalY = ()

	if request.method == 'POST':

	# Retrieving Patient information 

		Patient_name = request.POST.get("Patient")
		Hospital = request.POST.get("Hospital")
		NHS = request.POST.get("NHS")
		Checker = request.POST.get("Checker")
		DOB = request.POST.get("Date")

	# List of number of cells with signals 
		Cells = (request.POST.get("No. of cells1"),
		request.POST.get("No. of cells2"),
		request.POST.get("No. of cells3"),
		request.POST.get("No. of cells4"),
		request.POST.get("No. of cells5"),
		request.POST.get("No. of cells6"),
		request.POST.get("No. of cells7"),
		request.POST.get("No. of cells8"),
		request.POST.get("No. of cells9"),
		request.POST.get("No. of cells10"))

		CellsSC = (request.POST.get("No. of cells11"),
		request.POST.get("No. of cells12"),
		request.POST.get("No. of cells13"),
		request.POST.get("No. of cells14"),
		request.POST.get("No. of cells15"),
		request.POST.get("No. of cells16"),
		request.POST.get("No. of cells17"),
		request.POST.get("No. of cells18"),
		request.POST.get("No. of cells19"),
		request.POST.get("No. of cells20"))

	# Replace any empty fields in the list above and replace with 0, this avoids int() errors. 

		Cells2= [int(0) if v is '' else int(v) for v in Cells]
		CellsSC2= [int(0) if v is '' else int(v) for v in CellsSC]

		CS1 = Cells2[0]
		CS2 = Cells2[1]
		CS3 = Cells2[2]
		CS4 = Cells2[3]
		CS5 = Cells2[4]
		CS6 = Cells2[5]
		CS7 = Cells2[6]
		CS8 = Cells2[7]
		CS9 = Cells2[8]
		CS10 = Cells2[9]
		CS11 = CellsSC2[0]
		CS12 = CellsSC2[1]
		CS13 = CellsSC2[2]
		CS14 = CellsSC2[3]
		CS15 = CellsSC2[4]
		CS16 = CellsSC2[5]
		CS17 = CellsSC2[6]
		CS18 = CellsSC2[7]
		CS19 = CellsSC2[8]
		CS20 = CellsSC2[9]

	#List containing total Red signals 

		RedSignals = (request.POST.get("Red Signals1"),
		request.POST.get("Red Signals2"),
		request.POST.get("Red Signals3"),
		request.POST.get("Red Signals4"),
		request.POST.get("Red Signals5"),
		request.POST.get("Red Signals6"),
		request.POST.get("Red Signals7"),
		request.POST.get("Red Signals8"),
		request.POST.get("Red Signals9"),
		request.POST.get("Red Signals10"))

		RedSignalsSC = (request.POST.get("Red Signals11"),
		request.POST.get("Red Signals12"),
		request.POST.get("Red Signals13"),
		request.POST.get("Red Signals14"),
		request.POST.get("Red Signals15"),
		request.POST.get("Red Signals16"),
		request.POST.get("Red Signals17"),
		request.POST.get("Red Signals18"),
		request.POST.get("Red Signals19"),
		request.POST.get("Red Signals20"))


		RedSignals_2= [int(0) if v is '' else int(v) for v in RedSignals]
		RedSignals_SC2= [int(0) if v is '' else int(v) for v in RedSignalsSC]

		RS1 = RedSignals_2[0]
		RS2 = RedSignals_2[1]
		RS3 = RedSignals_2[2]
		RS4 = RedSignals_2[3]
		RS5 = RedSignals_2[4]
		RS6 = RedSignals_2[5]
		RS7 = RedSignals_2[6]
		RS8 = RedSignals_2[7]
		RS9 = RedSignals_2[8]
		RS10 = RedSignals_2[9]
		RS11 = RedSignals_SC2[0]
		RS12 = RedSignals_SC2[1]
		RS13 = RedSignals_SC2[2]
		RS14 = RedSignals_SC2[3]
		RS15 = RedSignals_SC2[4]
		RS16 = RedSignals_SC2[5]
		RS17 = RedSignals_SC2[6]
		RS18 = RedSignals_SC2[7]
		RS19 = RedSignals_SC2[8]
		RS20 = RedSignals_SC2[9]

		SumRS = (RS1 + RS2 + RS3 + RS4 + RS5 + RS6 + RS7 + RS8 + RS9 + RS10)
		SumRS_SC = (RS11 + RS12 + RS13 + RS14 + RS15 + RS16 + RS17 + RS18 + RS19 + RS20)

		GreenSignals = (request.POST.get("Green Signals1"),
		request.POST.get("Green Signals2"),
		request.POST.get("Green Signals3"),
		request.POST.get("Green Signals4"),
		request.POST.get("Green Signals5"),
		request.POST.get("Green Signals6"),
		request.POST.get("Green Signals7"),
		request.POST.get("Green Signals8"),
		request.POST.get("Green Signals9"),
		request.POST.get("Green Signals10"))

		GreenSignalsSC = (request.POST.get("Green Signals11"),
		request.POST.get("Green Signals12"),
		request.POST.get("Green Signals13"),
		request.POST.get("Green Signals14"),
		request.POST.get("Green Signals15"),
		request.POST.get("Green Signals16"),
		request.POST.get("Green Signals17"),
		request.POST.get("Green Signals18"),
		request.POST.get("Green Signals19"),
		request.POST.get("Green Signals20"))

		GreenSignals_2 = [int(0) if v is '' else int(v) for v in GreenSignals]
		GreenSignals_SC2 = [int(0) if v is '' else int(v) for v in GreenSignals]

	#return render(request, 'calculator/secondchecker.html', {'X': GreenSignals_2})

		GS1 = GreenSignals_2[0]
		GS2 = GreenSignals_2[1]
		GS3 = GreenSignals_2[2]
		GS4 = GreenSignals_2[3]
		GS5 = GreenSignals_2[4]
		GS6 = GreenSignals_2[5]
		GS7 = GreenSignals_2[6]
		GS8 = GreenSignals_2[7]
		GS9 = GreenSignals_2[8]
		GS10 = GreenSignals_2[9]
		GS11 = GreenSignals_SC2[0]
		GS12 = GreenSignals_SC2[1]
		GS13 = GreenSignals_SC2[2]
		GS14 = GreenSignals_SC2[3]
		GS15 = GreenSignals_SC2[4]
		GS16 = GreenSignals_SC2[5]
		GS17 = GreenSignals_SC2[6]
		GS18 = GreenSignals_SC2[7]
		GS19 = GreenSignals_SC2[8]
		GS20 = GreenSignals_SC2[9]

	#return render(request, 'calculator/secondchecker.html', {'X': GS10})

		SumGS = (GS1 + GS2 + GS3 + GS4 + GS5 + GS6 + GS7 + GS8 + GS9 + GS10)
		SumGS_SC = (GS11 + GS12 + GS13 + GS14 + GS15 + GS16 + GS17 + GS18 + GS19 + GS20)

	# Dictionary containing all input values, ready to be processed

		Form = {Cells2[0]: (RS1, GS1),
		Cells2[1]: (RS2, GS2),
		Cells[2]: (RS3, GS3),
		Cells2[3]: (RS4, GS4),
		Cells2[4]: (RS5, GS5),
		Cells2[5]: (RS6, GS6),
		Cells2[6]: (RS7, GS7),
		Cells2[7]: (RS8, GS8),
		Cells2[8]: (RS9, GS9),
		Cells2[9]: (RS10, GS10)}

		Form_SC = {Cells2[0]: (RS11, GS11),
		Cells2[1]: (RS12, GS12),	
		Cells[2]: (RS13, GS13),
		Cells2[3]: (RS14, GS14),
		Cells2[4]: (RS15, GS15),
		Cells2[5]: (RS16, GS16),
		Cells2[6]: (RS17, GS17),
		Cells2[7]: (RS18, GS18),
		Cells2[8]: (RS19, GS19),
		Cells2[9]: (RS20, GS20)
		}

	#return render(request, 'calculator/secondchecker.html', {'X': Signals})

	# Probe names, to used later on.
		Probe = (request.POST.get("Red"),
		request.POST.get("Green"))
		
	# Validating the sum of Cells is 50 
		Sumofcells = (sum(Cells2) + sum(CellsSC2))

	#return render(request, 'calculator/secondchecker.html', {'X': Sumofcells})

		if Sumofcells < 100:
			Error['validation'] = "Error: Minimum of 100 cells need to be checked!"
			return render(request, 'calculator/secondchecker.html', Error)

	# If total is 50 find signals in more than 25% of cells 
		elif Sumofcells >= 100:
			pass
		for i in Cells2:
			if i >= 25:
				HighestSignal = i
		for i in CellsSC2:
			if i >= 25:
				HighestSignal_SC = i 
		high = HighestSignal + HighestSignal_SC

	# create a dictionary using the highest signal as key to grab respective red and green signals
		if HighestSignal in Form: 
			Finalsignal = Form[HighestSignal]
	#return render(request, 'calculator/secondchecker.html', {'X': GreenSignals_2})


		if HighestSignal_SC in Form_SC:
			Finalsignal_SC = Form_SC[HighestSignal_SC]
	# Identifying whch probe has been affected

		for i in Finalsignal:
			if Finalsignal[0] > Finalsignal[1]:
				Region = Probe[0]
			else:
				Region = Probe[1] 

		for i in Finalsignal_SC:
			if Finalsignal_SC[0] > Finalsignal_SC[1]:
				Region_SC = Probe[0]
			else:
				Region_SC = Probe[1]
	
	# Classifing any oberved ratio, according to specification 
		Imbalance = (SumRS/SumGS)
		Imbalance_SC = (SumRS_SC/SumGS_SC)
	

		for i in Finalsignal:
			if Finalsignal[0] == 2 and Finalsignal[1] == 2:
				X = 'No evidence of 1p/19q co-deletion'
			elif Finalsignal[0] == 1 and Finalsignal[1] == 2:
				X = 'Absolute deletion'
			elif Finalsignal[0] == 2 and Finalsignal[1] == 1:
				X = 'Loss of Control'
			elif (Finalsignal[0]/Finalsignal[1]) == 2:
				X = 'Absolute deletion'
			elif (Finalsignal[0]/Finalsignal[1]) == 0.5:
				X = 'Relative deletion'
			elif (Finalsignal[0]/Finalsignal[1]) == 1:
				X = 'Polysomy'
			else:
				X = 'Imbalance' 
	
		if X == 'Imbalance' and Imbalance < 0.8:
			Classification = 'No evidence of 1p/19q co-deletion'
		else:
			Classification = str(X) + " " + 'of'+ " "+str(Region)+" "+'in'+" "+str(HighestSignal)+" "+'out of 50 cells'

	#return render(request, 'calculator/secondchecker.html', {'X': X})

		for i in Finalsignal_SC:
			if Finalsignal_SC[0] == 2 and Finalsignal_SC[1] == 2:
				Y = 'No evidence of 1p/19q co-deletion'
			elif Finalsignal_SC[0] == 1 and Finalsignal_SC[1] == 2:
				Y = 'Absolute deletion'
			elif Finalsignal_SC[0] == 2 and Finalsignal_SC[1] == 1:
				Y = 'Loss of Control'
			elif (Finalsignal_SC[0]/Finalsignal_SC[1]) == 2:
				Y = 'Absolute deletion'
			elif (Finalsignal_SC[0]/Finalsignal_SC[1]) == 0.5:
				Y = 'Relative deletion'
			elif (Finalsignal_SC[0]/Finalsignal_SC[1]) == 1:
				Y = 'Polysomy'
			else:
				Y = 'Imbalance'

		if Y == 'Imbalance' and Imbalance_SC < 0.8:
			Classification_SC = 'No evidence of 1p/19q co-deletion'
		else:
			Classification_SC = str(Y) + " " + 'of'+ " "+str(Region_SC)+" "+'in'+" "+str(HighestSignal_SC)+" "+'out of 50 cells'
				
		if X == Y and Imbalance > 0.8 and Imabalance > 0.8:
			Final_Interpretation = str(X) + " " + 'of'+ " "+str(Region)+" "+'in'+" "+str(high)+" "+'out of 100 cells'
		else:
			Final_Interpretation = Classification + " " + 'of'+ " "+str(Region)+" "+'in'+" "+str(HighestSignal)+" "+'out of 50 cells'+" "+ 'and'+ " "+ Classification_SC + " " + 'of'+ " "+str(Region_SC)+" "+'in'+" "+str(HighestSignal_SC)+" "+'out of 50 cells'


	return render(request, 'calculator/secondchecker.html', {'X': Classification, 'Y': Classification_SC, 'RS1': RS1, 'RS2': RS2, 'RS3': RS3, 'RS4': RS4, 'RS5': RS5, 'RS6': RS6, 'RS7': RS7, 
		'RS8': RS8, 'RS9': RS9, 'RS10': RS10, 'RS11': RS11, 'RS12': RS12, 'RS13': RS13, 'RS14': RS14, 'RS15': RS15, 'RS16': RS16, 'RS17': RS17, 
		'RS18': RS18, 'RS19': RS19, 'RS20': RS20, 'GS1': GS1, 'GS2': GS2, 'GS3': GS3, 'GS4': GS4, 'GS5': GS5, 'GS6': GS6,
		'GS7': GS7, 'GS8': GS8, 'GS9': GS9, 'GS10': GS10, 'GS11': GS11, 'GS12': GS12, 'GS13': GS13, 'GS14': GS14, 'GS15': GS15, 'GS16': GS16,
		'GS17': GS17, 'GS18': GS18, 'GS19': GS19, 'GS20': GS20, 'CS1': CS1, 'CS2': CS2, 'CS3': CS3, 'CS4': CS4, 'CS5': CS5, 
		'CS6': CS6, 'CS7': CS7, 'CS8': CS8, 'CS9': CS9, 'CS10': CS10, 'CS11': CS11, 'CS12': CS12, 'CS13': CS13, 'CS14': CS14, 'CS15': CS15, 
		'CS16': CS16, 'CS17': CS17, 'CS18': CS18, 'CS19': CS19, 'CS20': CS20, 'PN': Patient_name, 'H': Hospital,
		'NHS': NHS, 'Checker': Checker, 'Interpretation': Final_Interpretation, 'Classification_SC': Classification_SC})



									
									
	



	