The Traffic Counter is a proof of concept for a University level meeting with a professor. 

The concept is to ingest a simple video feed of traffic, and count the cars every "X" seconds. 
- You'll have to do the math and geometry to determine the number of seconds for your application.
- The code is written to ingest multiple types of video feeds (3 open video feeds included for testing).
- To build this up to production would require a kernel which removes the background (the road & surroundings).

Manifest for countertc.py:
    This code was built in Python 3.9.6 using these package versions:
    - opencv-python v 4.5.3.56  (known bug within newer 4.6.X)
    - matplotlib.pyplot v 3.4.3 
    - cvlib v 0.2.6 
    - tensorflow v 2.7.0
    - datetime v 4.3
    - time v 0.0.1