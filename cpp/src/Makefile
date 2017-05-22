CXX = g++
CXXFLAGS = -g -O2 -std=c++11 -Wall

all: do

do: main.cpp dim.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^


infTR: main2.cpp dim.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ -D TR

infWC: main2.cpp dim.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ -D WC

loopInfTR: infTR
	rm -f TR*.txt
	@for i in {10,50,100,150,500,1000,10000}; do ./infTR $$i >> TR_$$i.txt; done
	@for i in {10,50,100,150,500,1000,10000}; do cat TR_$$i.txt >> TR.txt; done
	rm -f TR_*.txt


loopInfWC: infWC
	rm -f WC*.txt
	@for i in {10,50,100,150,500,1000,10000}; do ./infWC $$i >> WC_$$i.txt; done
	@for i in {10,50,100,150,500,1000,10000}; do cat WC_$$i.txt >> WC.txt; done
	rm -f WC_*.txt

testing:
	@for i in {10,50,100,150,500,1000,10000}; do echo "./infTR $$i"; done

.PHONY: clean

clean:
	rm -f do infTR infWC


