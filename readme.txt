Lab4 UDP Socket progamming
code written by: Indiana Hooser

data file tested "data"

Client:
The client will be receiving data from a file or form the keyboard. It is up to the user. This data will then be encrypted and sent to the Server. Then it will receive a reply form the server about its most recent data receiving.
-arguments
	Client_number Server_IP-adress Server-port_Number Key_for_this_client
	(example and tested)
	1 10.1.224.247 6790 data 5
-notes
	1) The data file with the original data must be in same folder as the script
	2) The client number, and key is going to be connected. The server has a set key for each client
	3) to have a specific client send multiple files to the server then just run the client again.
Server:
The server will receive data from a client. This data will contain a encrypted message, Ip_address, Port number, client number, and the time stamp of the client. The server will then save that information and send it back to the client after decoding the data. Along with the past five information received.
-arguments
	Server_port_number
	(example and tested)
	6790
	(note) this port number must be the same Server port number stated in the client.
-notes
	1) If there is no key for the specific client then an error message is sent back to the client and the stored messages are not changed
	2) if the key of the client and the server don’t match then the data is decoded incorrectly but it is still saved
	3) Every time data is received it is save4d up to five times. If a sixth data is sent then it is deleted.
