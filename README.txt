The first line of the barcodes.txt file defines which line ending will be used for barcodes. 
	0 - No Line End
	1 - CR Line End (\r)
	2 - CRLF Line End (\r\n)

The default IP and port being used are 127.0.0.1 : 8889. There isn't currently any way to change this. 

The program waits for a connection to be established, waits five seconds, then starts looping through the barcodes.txt file, sending them line by line to the client. There is a delay of 5 seconds between each code being sent. 

No error reporting has been built in as it's only being used to replicate a line scanner in our testing. 