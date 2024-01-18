# USAGE
# python barcode_scanner_video.py

# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import pygame
import os

from pygame import mixer
from static.scripts.emai2l import enviar
mixer.init()


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
	help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# open the output CSV file for writing and initialize the set of
# barcodes found thus far
csv = open(args["output"], "w")
found = set()

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# find the barcodes in the frame and decode each of the barcodes
	barcodes = pyzbar.decode(frame)

	# loop over the detected barcodes
	for barcode in barcodes:
		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

		# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type

		# draw the barcode data and barcode type on the image
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

		if barcodeData =="palmeiras":
			mixer.music.stop()
			mixer.music.load("palmeiras.mp3")
			mixer.music.play()
			
		if barcodeData =="saopaulo":
			mixer.music.stop()
			mixer.music.load("saopaulo.mp3")
			mixer.music.play()
			
			

		if barcodeData =="corinthians":
			mixer.music.stop()
			mixer.music.load("corinthians.mp3")
			mixer.music.play()

		if barcodeData =="cruzeiro":
			mixer.music.stop()
			mixer.music.load("cruzeiro.mp3")
			mixer.music.play()

		if barcodeData =="santos":
			mixer.music.stop()
			mixer.music.load("santos.mp3")
			mixer.music.play()

		if barcodeData =="champions_league":
			mixer.music.stop()
			mixer.music.load("champions_league.mp3")
			mixer.music.play()

		if barcodeData =="naruto":
			mixer.music.stop()
			mixer.music.load("naruto.mp3")
			mixer.music.play()

		if barcodeData =="fogobixo":
			mixer.music.stop()
			mixer.music.load("fogobixo.mp3")
			mixer.music.play()

		if barcodeData =="jaula":
			mixer.music.stop()
			mixer.music.load("jaula.mp3")
			mixer.music.play()

		if barcodeData =="querocafe":
			mixer.music.stop()
			mixer.music.load("querocafe.mp3")
			mixer.music.play()

		if barcodeData =="funk":
			mixer.music.stop()
			mixer.music.load("sweetdreams.mp3")
			mixer.music.play()

		if barcode == "stop":
			pygame.mixer.pause()

		if barcodeData =="artic":
			mixer.music.stop()
			mixer.music.load("Arctic.mp3")
			mixer.music.play()

		if barcodeData =="copadomundo":
			mixer.music.stop()
			mixer.music.load("copadomundo.mp3")
			mixer.music.play()
			
		if barcodeData =="charlie":
			mixer.music.stop()
			mixer.music.load("charlie.mp3")
			mixer.music.play()

		if barcodeData =="joeSatriani":
			mixer.music.stop()
			mixer.music.load("joeSatriani.mp3")
			mixer.music.play()

		if barcodeData =="coldplay":
			mixer.music.stop()
			mixer.music.load("coldplay.mp3")
			mixer.music.play()


		if barcodeData =="coldplaychainsmoker":
			mixer.music.stop()
			mixer.music.load("coldplaychainsmoker.mp3")
			mixer.music.play()


		if barcodeData =="imagine1":
			mixer.music.stop()
			mixer.music.load("Imagine.mp3")
			mixer.music.play()


		if barcodeData =="marshmello":
			mixer.music.stop()
			mixer.music.load("Marshmello.mp3")
			mixer.music.play()


		if barcodeData =="panic":
			mixer.music.stop()
			mixer.music.load("panic.mp3")
			mixer.music.play()


		if barcodeData =="foto":
			
			cv2.imwrite("temp/figura.png" , frame)
			os.system("clear")
			print ("------------------------------ Envindo Email ------------------------------ ")
			print ("***************************************************************************\n\n")
			texto = raw_input("Digite o seu email...:")
			
			print("\n\n Aguarde o envio...")
			
			enviar(texto)
			
			print ("\n\n\n\n\n------------------------- EMAIL ENVIADO COM SUCESSO ------------------------")
			print ("****************************************************************************")


			


			

		
		if barcodeData =="https://www.unifeg.edu.br/webacademico/site/index.jsp":
			import webbrowser

			webbrowser.open("https://www.unifeg.edu.br/webacademico/site/index.jsp", new=0, autoraise=True)
 			time.sleep(5.0)

		# if the barcode text is currently not in our CSV file, write
		# the timestamp + barcode to disk and update the set
		if barcodeData not in found:
			csv.write("{},{}\n".format(datetime.datetime.now(),
				barcodeData))
			csv.flush()
			found.add(barcodeData)

	# show the output frame
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()