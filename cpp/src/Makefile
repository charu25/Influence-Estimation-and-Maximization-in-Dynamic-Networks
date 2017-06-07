# 'lable' can be appended to output file by passing label=<some label>

CXX = g++
CXXFLAGS = -g -O2 -std=c++11 -Wall

all: do

do: main.cpp dim.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^


infTREnron: main2.cpp dim.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ -D TR -D ENRON

infWCEnron: main2.cpp dim.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ -D WC -D ENRON

infTRDigg: main2.cpp dim.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ -D TR -D DIGG

infWCDigg: main2.cpp dim.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ -D WC -D DIGG

loopInfTREnron: infTREnron
	@Echo Generating TR for Enron $(label)
	rm -f TR_Enron*.txt
	@for i in {10,50,100,150,500,1000,10000}; do ./infTREnron $$i >> TR_Enron_$$i.txt; done
	@for i in {10,50,100,150,500,1000,10000}; do cat TR_Enron_$$i.txt >> TR_Enron$(label).txt; done
	rm -f TR_Enron_*.txt


loopInfWCEnron: infWCEnron
	@Echo Generating WC for Enron $(label)
	rm -f WC_Enron*.txt
	@for i in {10,50,100,150,500,1000,10000}; do ./infWCEnron $$i >> WC_Enron_$$i.txt; done
	@for i in {10,50,100,150,500,1000,10000}; do cat WC_Enron_$$i.txt >> WC_Enron$(label).txt; done
	rm -f WC_Enron_*.txt

loopInfTRDigg: infTRDigg
	@Echo Generating TR for Digg $(label)
	rm -f TR_Digg*.txt
	@for i in {10,50,100,150,500,1000,10000}; do ./infTRDigg $$i >> TR_Digg_$$i.txt; done
	@for i in {10,50,100,150,500,1000,10000}; do cat TR_Digg_$$i.txt >> TR_Digg$(label).txt; done
	rm -f TR_Digg_*.txt


loopInfWCDigg: infWCDigg
	@Echo Generating WC for Digg $(label)
	rm -f WC_Digg*.txt
	@for i in {10,50,100,150,500,1000,10000}; do ./infWCDigg $$i >> WC_Digg_$$i.txt; done
	@for i in {10,50,100,150,500,1000,10000}; do cat WC_Digg_$$i.txt >> WC_Digg$(label).txt; done
	rm -f WC_Digg_*.txt


runall: loopInfWCDigg loopInfTRDigg loopInfWCEnron loopInfTREnron
	mv *$(label)* build/

testing:
	@for i in {10,50,100,150,500,1000,10000}; do echo "./infTR $$i"; done

.PHONY: clean

clean:
	rm -f do infTR infWC
