.SUFFIXES: .c .h .o

CC	= g++
INCLDIR	= include/
BINDIR	= bin/
SRCDIR	= src/

_BIN	= a.out
BIN	= $(addprefix $(BINDIR), $(_BIN))

SRC	= $(wildcard src/*.c)

CFLAGS = -Wall -std=c++11 -pedantic -g -I$(INCLDIR) -lm -lcurl #-fsanitize=address -fsanitize=undefined 

$(BINDIR)/$(_BIN): $(SRC)
	@$(CC) $(SRC) $(CFLAGS) -o $@

gendir: 
	@mkdir include bin src

clean: 
	@rm bin/a.out

.PHONY: gendir
.PHONY: clean
