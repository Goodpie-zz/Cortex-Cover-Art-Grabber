#Copyright ReallyGoodPie 2014
#I take no ownership of the site used to download the images themselves

import urllib.request, os
from PIL import Image

#Fetching the image and saving it to appropriate place
def getImageFromSteam(appID):
	
	originalLink = ("http://cdn.akamai.steamstatic.com/steam/apps/%s/header.jpg" % str(appID))
	saveFolder = (str(appID) + ".jpg")
	try:
		urllib.request.urlretrieve(originalLink, saveFolder)
	except:
		print("Failed to laod image for %s. Possibly. The image may not be on the servers." % (str(appID)))

#Resizing and saving the new images.
def resizeImage(appID):
	
	#Setting some initial variables
	imageSize = width, height = 864, 486
	imageName = str(appID) + ".jpg"
	newImageName = "R_" + imageName

	#Downscaling the image using ANTIALIAS method because I know nothing about image processing and ANTIALIAS sounded good. Probably wrong but who cares?
	try:
		openImage = Image.open(imageName)
		downscaledImage = openImage.resize((imageSize), Image.ANTIALIAS)
		downscaledImage.save(newImageName)
	except:
		pass
	
steamDir = input("Please input your SteamApps directory: ")

appArray = []
steamAppList = os.listdir(steamDir)

#Seperating the filenames and getting the integers from the SteamApps folder. To be used as AppID.
for app in steamAppList:
	initSep = app.split("_")

	#Try method will seperate the other files from the steam app ID's
	try:
		finSep = initSep[1].split(".")
		appArray.append(finSep[0])
	except:
		pass

appIDAmount = len(appArray)
print("There are %d images are being downloaded. Please wait." % appIDAmount)

#Doing shit
for i in range(0, appIDAmount):
	getImageFromSteam(appArray[i])
	resizeImage(appArray[i])
