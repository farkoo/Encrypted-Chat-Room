# Encrypted-Chat-Room
In this program we want to create an unlimited chatroom based on tcp/ip between the client and the server.

* After executing the server file, the server listens on the port to connect the client.
* After connecting the client to the server, both parties can send unlimited messages to each other.
* When the message from one of the two parties is "Good bye", the connection between them ends.

In this program, the exchanged messages are encrypted using the monoalphabetic method and are decrypted and displayed on the other side.

### Execute server
```python
python _server.py
```

### Execute client in other instance
```python
python _client.py
```
