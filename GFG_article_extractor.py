#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import os


AllTags = ['Greedy-Algorithm']

path = ''

def ExtractMainLinks(AllTags,path):
	for i in AllTags:
		newpath = path + i 
		os.mkdir(newpath)
		url = "http://www.geeksforgeeks.org/tag/" + i +"/"
		data = urllib2.urlopen(url).read()
		soup = BeautifulSoup(data,"html.parser")
		allLinks = soup.findAll("h2",class_="entry-title")
		listofLinks = []
		for link in allLinks:
			mainLink = str(link.findAll("a")[0]).split("<a href=")[1].split('rel="bookmark"')[0].strip('"').split('"')[0]
			listofLinks.append([mainLink,mainLink.split('/')[3]])
		Extract_And_Save_Page_Data(listofLinks)
		


def Extract_And_Save_Page_Data(listofLinks):
	No = 0
	for item in listofLinks:
		pageData = urllib2.urlopen(item[0]).read()
		filePath = item[1]+".html"
		No = No +1
		with open(filePath,"wb") as f:
			f.write(str(pageData))

ExtractMainLinks(AllTags,path)
