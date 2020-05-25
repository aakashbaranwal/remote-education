from django.http import HttpResponse 
from django.shortcuts import render
import operator


def home(request):
	return render(request,'home.html')

def count(request):
	fulltext= request.GET['fulltext']
	letterlist=fulltext.split()
	wordict={}
	letterdict={}
	finalcount=0
	for word in letterlist:
		count=0
		for letter in word:
			count+=1
		letterdict[word]=count
		finalcount+=count

	for word in letterlist:
		count=0
		if word in wordict:
			wordict[word]+=1
		else:
			wordict[word]=1
	print(wordict)
	sortedletters=sorted(wordict.items(),key=operator.itemgetter(1))
	sortedwords=sorted(letterdict.items(),key=operator.itemgetter(1))
	return render(request,'count.html',{'showtext':fulltext,'count':finalcount,'countword':len(letterlist),'details':letterdict.items(),'detailsword':wordict.items(),'wordlist':sortedletters,'letterlist':sortedwords})