;32-bit x86 Shellcode jmp-call-pop example
;Author: Francis Murray
;Date: 19 OCT 2018
;rev: 28 AUG 2019

BITS 32
segment .data

GLOBAL _SIZE_OF_PIC,_PIC_BYTES
GLOBAL _PIC_fpFxn


_PIC_BYTES:
	jmp call_code

shellcode:
	pop eax
	
	//Shell Code Goes here
	
call_code:
	call shellcode

PIC_DATA_OFFSET_0:
_PIC_fpFxn dd 0

PIC_DATA_OFFSET_1 equ $-PIC_DATA_OFFSET_0
myString db "Fxn Input data maybe ?? ;)", 0x00
	
_SIZE_OF_PIC dd $-_PIC_BYTES
