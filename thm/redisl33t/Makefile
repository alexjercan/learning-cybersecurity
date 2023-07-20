.PHONY: all clean

all: main

main:
	gcc -shared main.c -o main -Wl,-e,entry -fPIC

clean:
	rm main
