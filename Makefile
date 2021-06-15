FILENAME = main
ARG = sample

default: compile

compile:
	python3 -B $(FILENAME).py $(ARG).txt

clean:
	rm $(ARG).bin
