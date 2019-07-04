# PrecisionFarming
This is a final year project work by Prince Alfred Gyan and Dennis Effa Amponsah. It  employs the use of IOT to monitor, store and analyse soil conditions in a green house to enhance crop production. The microcontroller used is the raspberry pi.

# Abstract
As per the advancement pattern of current agriculture and the prerequisites for science and technology. The conventional farming chiefly depend on common assets and low work costs. It’s troublesome and inefficient, and the remaining task at hand is heavy. So it cannot meet the necessities of present day agriculture which is high-yield, high quality, efficient, safe and ecological. Because the IOT (Internet of Things) innovation was connected to agriculture, the modernization and the data innovation of farming have been significantly improved. The paper presents the idea of IOT and outlines applications in the cutting edge breeding, crop growth, quality and safety of agricultural products checking with IOT to concentrate on its several technologies. The paper calls attention to issues of IOT applications in horticulture and prospects for what’s to come. Today agriculture is embedded with advanced service like GPS, sensors that empower to communicate to one another examine the information and furthermore exchange information among them. IT gives services such as cloud to agriculture. Agriculture cloud and IT services gives an extraordinary expertise administration to farmers] with respect to cultivation of crops, pricing, fertilizers ,diseases detail method of cure to be used Scientist working on agriculture will provide their discoveries, in regards to present day techniques for cultivation ,utilization of composts can acquire the historical backdrop of the locale. 

# User Manual.
This project is composed of two major parts the assembly of the hardware and the software running on the hardware. In case you cannot find answers to your questions in this manual, feel free to send us a mail at princealfredgyan@gmail.com and kamponsah.amponsah@gmail.com.

# Assembly of The Hardware.
All components making up the hardware is connected to the PCB and the PCB is connected to the raspberry pi. For the sake of confusion of polarity of some of the sensors such as soil moisture and soil temperature there are markings in the PCB indicating the polarity of the sensors.
# Getting The Software up and Running.
Before this step, please ensure that all the sensors are connected to the PCB and the PCB is fixed on the raspberry pi. Ensure that the raspberry pi is connected to a power source and has internet connectivity.
1.	Navigate into the project directory. Currently on in “Desktop/CANS/Precision Farming”.
2.	Change directory into “dashboard” and then type “python app.py”. This should start the server running the web application.
The server generates a url which is used to access data from the sensors locally. To make this local server available to the WWW, we employ the use of ngrok.

# To start ngrok,
1.	Navigate into the downloads folder and type “ngrok http 5000”.
2.	The above command generates unique url which exposes applications running on port 5000. The above generated url can then be shared.
Due to thread issues, user would have to start up the code that reads the data from sensors as well. 
To do this, open a new terminal and navigate into “Desktop/CANS/Precision\Farming/dashboard/combined code” and run the file combined.py.
The above command initiates the thread which reads data from sensors to the web page.



# Sensors in Use
### 1.[DS18B20 - Soil Temperature](https://github.com/princegyan/Precision-Farming/blob/master/webTemplate/qbgrow.com/magen/iot-admin/ds18b20.py) 
### 2.[Capacitive Soil Moisture ](https://github.com/princegyan/Precision-Farming/blob/master/webTemplate/qbgrow.com/magen/iot-admin/moisture.py)
### 3.GY21P - [Humidity](https://github.com/princegyan/Precision-Farming/blob/master/webTemplate/qbgrow.com/magen/iot-admin/gy21.py) & [Temperature ](https://github.com/princegyan/Precision-Farming/blob/master/webTemplate/qbgrow.com/magen/iot-admin/temp2.py)
### 4.E201-C - pH sensor [Code Here]()
### [Combined Code ](https://github.com/princegyan/Precision-Farming/blob/master/webTemplate/qbgrow.com/magen/iot-admin/combined%20code/combined.py)

# Contributing
This project is not open for contributions yet.
