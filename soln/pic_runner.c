#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

typedef HANDLE(WINAPI *fpCreateFile)(
	LPCSTR lpFileName,
	DWORD dwDesiredAccess,
	DWORD dwShareMode,
	LPSECURITY_ATTRIBUTES lpSecurityAttributes,
	DWORD dwCreationDisposition,
	DWORD dwFlagsAndAttributes,
	HANDLE hTemplateFile
	);

typedef VOID (WINAPI *fpPic)();

extern BYTE PIC_BYTES[];
extern ULONG SIZE_OF_PIC;
extern fpCreateFile PIC_fpCreateFile;

void main()
{
	int tmp;
	fpPic pPic = NULL;
	
	PIC_fpCreateFile = (fpCreateFile)GetProcAddress(GetModuleHandleA("Kernel32"), "CreateFileA");

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