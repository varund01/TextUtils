# file created
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return render(request,'index.html')

def analyze(request):

	djtext=request.POST.get('text','default')
	removepunc=request.POST.get('removepunc','off')
	fullcaps=request.POST.get('uppercase','off')
	newlineremover=request.POST.get('newlineremover','off')
	punctutations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

	if(djtext==''):
		return HttpResponse("<h1>You didn't enter anything!!</h1>")

	analyzed=""
	c=0
	
	if removepunc=='on':
		for char in djtext:
			if char not in punctutations:
				analyzed=analyzed+char
		djtext=analyzed
		c=c+1


	if fullcaps=='on':
		analyzed=""
		for char in djtext:
			analyzed = analyzed + char.upper()
		djtext=analyzed
		c=c+1


	if newlineremover=='on':
		analyzed=""
		for char in djtext:
			if char!='\n' and char!='\r':
				analyzed=analyzed+char
		djtext=analyzed
		c=c+1

	if c==0:
		return HttpResponse("<h1>You did not choose anything</h1>");

	params={'purpose':'remove punctutaions' , 'analyzed_text':djtext}
	return render(request,'analyze.html',params)