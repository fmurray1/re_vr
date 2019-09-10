BITS 32
segment .data

GLOBAL _SIZE_OF_PIC,_PIC_BYTES
GLOBAL _PIC_fpCreateFile


_PIC_BYTES:
	jmp call_code

shellcode:
	pop eax
	
	xor ecx, ecx ; hTemplateFile
	push ecx ; NULL

	xor ecx, ecx ; dwFlagsAndAttributes
	mov ch, 8 ;  file attribute normal 0x80
	push ecx

	xor ecx, ecx ; dwCreationDisposition
	mov cl, 2 ; create always
	push ecx

	xor ecx, ecx ; lpSecurityAttributes
	push ecx ; NULL

	xor ecx, ecx ; dwShareMode
	push ecx ; 0

	xor ecx, ecx ; dwDesiredAccess
	mov cl, 3 ; generic_read | generic_write (acess mask format see msdn)
	shl ecx, 30
	push ecx

	lea ecx, [eax+PIC_DATA_OFFSET_FILE] ; lpFileName
	push ecx

	call [eax] ; create file was stored in eax after the jmp-call-pop
	
	ret
	
call_code:
	call shellcode

PIC_DATA_OFFSET_0:
_PIC_fpCreateFile dd 0

PIC_DATA_OFFSET_FILE equ $-PIC_DATA_OFFSET_0
filename db "C:\\path\\to\\put\\someFile.txt", 0x00
	
_SIZE_OF_PIC dd $-_PIC_BYTES