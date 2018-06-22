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
	X ={}
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

		for i in Finalsignal:
			if Finalsignal[0] == 2 and Finalsignal[1] == 2:
				X = 'Normal'
			elif Finalsignal[0] == 1 and Finalsignal[1] == 2:
				X = 'Absolute deletion'
			elif Finalsignal[0] == 2 and Finalsignal[1] == 1:
				X = 'Absolute deletion'
			elif (Finalsignal[0]/Finalsignal[1]) == 2:
				X = 'Absolute deletion'
			elif (Finalsignal[0]/Finalsignal[1]) == 0.5:
					X = 'Relative deletion'
			elif (Finalsignal[0]/Finalsignal[1]) == 1:
				X = 'Polysomy'
			else:
				X = 'Imbalance'

		#Second = request.POST.get("Second checker")
		#if Second == True 
			


		Classification = str(X) + " " + 'of'+ " "+str(Region)+" "+'in'+" "+str(high)+" "+'out of 50 cells'


	return render(request, 'calculator/index.html', {'X': Classification, 'RS1': RS1, 'RS2': RS2, 'RS3': RS3, 'RS4': RS4, 'RS5': RS5, 'RS6': RS6, 'RS7': RS7, 
		'RS8': RS8, 'RS9': RS9, 'RS10': RS10, 'GS1': GS1, 'GS2': GS2, 'GS3': GS3, 'GS4': GS4, 'GS5': GS5, 'GS6': GS6,
		'GS7': GS7, 'GS8': GS8, 'GS9': GS9, 'GS10': GS10, 'CS1': CS1, 'CS2': CS2, 'CS3': CS3, 'CS4': CS4, 'CS5': CS5, 
		'CS6': CS6, 'CS7': CS7, 'CS8': CS8, 'CS9': CS9, 'CS10': CS10, 'PN': Patient_name, 'H': Hospital,
		'NHS': NHS, 'Checker': Checker})


def second(request):
	second = request.POST.get("Second Checker")
	if second.checked == True:
		return render(request, 'calculator/secondchecker.html', {} )


 


									
									
	



	