CC = python3
CFLAGS = -B 
TARGET =
SRC = main.py
ARG = sample.txt

ALL: $(SRC)
	$(CC) $(CFLAGS) $(SRC) $(ARG) 

clean:
