/*
 PIC Code runner capable of doing external function calls.
 Author: Francis Murray
 Date: 19 OCT 2018
 Rev: 28 AUG 2019
 */

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

typedef HANDLE(WINAPI *fpFxn)(
	/* Fill this stuff in for the fxn call */
	);

typedef VOID (WINAPI *fpPic)();

extern BYTE PIC_BYTES[];
extern ULONG SIZE_OF_PIC;
extern fpFxn PIC_fpFxn;

void main()
{
	int tmp;
	fpPic pPic = NULL;
	
	PIC_fpFxn = (fpFxn)GetProcAddress(GetModuleHandleA("IMPORT_FROM_THIS"), "WHAT_ARE_YOU_IMPORTING");

	pPic = (fpPic)VirtualAlloc(NULL, SIZE_OF_PIC, MEM_COMMIT, PAGE_EXECUTE_READWRITE);

	if (pPic)
	{
		memcpy(pPic, PIC_BYTES, SIZE_OF_PIC);
		pPic();
		VirtualFree(pPic, 0, MEM_RELEASE);
		pPic = NULL;
	}
	return;
}
