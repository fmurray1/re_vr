# RE/VR Basic Lab

## Assumptions

1. This lab is designed to run in Windows XP
1. This lab is in x86 i.e., 32-bit
1. The host machine has python2 installed
1. The host machine has an internet connection
1. The User has a basic understanding of the following languages:
	1. C\C++
	1. Intel Assembly (x86)
	1. Python 2

## Meat and Potatoes

This lab is designed in two (three) parts. 
1. The first part is that there is a vulnerable server, open it up in IDA (or other disassemblers) take a look. 
There is a bad practice you should be able to find. Once you think you've found it try to get it to crash ;). How does one get it to crash, there is a python Fuzzer/Exploiter.
Test your hypothesis by sending some data to the server.

2. Part two of the lab is to write some PIC code and get it to run from the C file labeled PIC_runner. This runner can do anything that you want it to but something usefull may be
to have some function calls that take in multiple arguments. Maybe some `windows` specific function calls.

3. For extra credit, combine parts one and two and get the server to run your PIC code.

## Questions

If you have any issues, you know where I sit come and find me and ask. :) I hope this helps.