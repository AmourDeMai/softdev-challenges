C = gcc
RM = rm
Month = $(shell date '+%B')
CFLAGS = -Wall

all: strange_app

strange_app: strange_app.c ${Month}.o strange_app.h
	${CC} ${CFLAGS} strange_app.c ${Month}.o -o strange_app

${Month}.o: ${Month}.c
	${CC} -c ${Month}.c -o ${Month}.o

clear:
	${RM} -f *.o

