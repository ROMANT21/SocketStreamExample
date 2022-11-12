# Socket Stream Example
This repo contains some code that mimicks how the Rover sends video frames to the computer at Mission Control on your local computer.

## Instructions to run
To run the code you'll need to install opencv (which handles all the images)  
Open a terminal and run:  
`pip install opencv-python`  
Next, we need imutils (which we use to resize frames):  
`pip install imutils`  

After that, we need to launch the Rover (server.py)  
Run the following command:  
`python .\Rover\server.py`  

Then we can launch mission control (client.py)  
In a **seperate terminal**, run:  
`python .\BayStation\client.py`  

By then, we should see two windows, one transmitting and one receiving frames!!  
To exit, just press 'Q' while hovering over one of the windows 👍
