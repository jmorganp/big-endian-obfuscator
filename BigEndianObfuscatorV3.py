#!/usr/bin/env python3
# Big Endian Obfuscator
import sys
import base64
import time
import random
import hashlib
from urllib.parse import quote

def obfuscate(split_array):
    encoded = []
    var_name = get_name()
    for string in split_array:
        encoding = int.from_bytes(bytes(string, "utf-8"), byteorder="big")
        encoded.append(encoding)
    obfuscated_content = f"var {var_name} = new Array;{var_name} = ["

    for num in range(len(encoded)):
        obfuscated_content += f'{encoded[num]},'
    obfuscated_content += "];var op = '';for(i=0;i<" + var_name + ".length;i++){tmp = " + var_name + "[i];if(Math.floor((tmp/Math.pow(256,3)))>0){op += String.fromCharCode(Math.floor((tmp/Math.pow(256,3))));};tmp = tmp - (Math.floor((tmp/Math.pow(256,3))) * Math.pow(256,3));if(Math.floor((tmp/Math.pow(256,2)))>0){op += String.fromCharCode(Math.floor((tmp/Math.pow(256,2))));};tmp = tmp - (Math.floor((tmp/Math.pow(256,2))) * Math.pow(256,2));if(Math.floor((tmp/Math.pow(256,1)))>0){op += String.fromCharCode(Math.floor((tmp/Math.pow(256,1))));};tmp = tmp - (Math.floor((tmp/Math.pow(256,1))) * Math.pow(256,1));if(Math.floor((tmp/Math.pow(256,0)))>0){op += String.fromCharCode(Math.floor((tmp/Math.pow(256,0))));};};document.write(op);"

    return obfuscated_content

def output(file_name, content):
    with open(file_name, "a", encoding="utf-8") as output_file:
        output_file.write(content)

def random_hash():
    randomy = random.randint(29384393,89239473278329) # dumb random integer generation ;)
    hashy = hashlib.md5(bytes(str(randomy), "utf-8")).hexdigest()
    return hashy

def url_encode(content):
    url_encoded_string = ''
    for char in content:
        if int(ord(char)) > 32 and int(ord(char)) < 126: # ASCII Printable characters Range
            url_encoded_string += f"%{format(ord(char),'x').upper()}"
            continue
        else:
            url_encoded_string += quote(char)
            continue

    return url_encoded_string

def get_name():
    s_name = ''
    for i in range(3):
        s_name += random.choice('bcdfghjklmnpqrstvwxyz')
    return s_name


def main():
    input_file = input("[+] Enter input file: ")
    print("[+] Select Output mode:\n\n 1. Inline Javascript(Single file)\n 2. External Javascript (two file outputs)\n")
    output_mode = input("[+] Enter 1 or 2 to select: ")

    with open(input_file, "r", encoding="utf-8") as file_:
        content = file_.read()

        url_encoded_string = url_encode(content)
        html_output = f"<script language=javascript>document.write(decodeURIComponent('{url_encoded_string}'))</script>"
        content_length = len(html_output)
        split_array = []
        start, end = 0, 4

        # Determine big endian ranges(multiples of 4)
        if content_length % 4 == 0:
            quad_range = int(content_length/4)

        elif content_length % 4 != 0:
            quad_range = int(content_length/4) + 1

        for i in range(quad_range):
            # temp = content[start:end]
            temp = html_output[start:end]
            split_array.append(str(temp))
            start = end
            end += 4

        obfuscated_content = obfuscate(split_array)

        if output_mode == '1':
            single_output = f'<script language="Javascript">\n{obfuscated_content}\n</script>'
            output("obfuscated.html", single_output)

        elif output_mode == '2':
            hashy = random_hash()
            external = f'<script language="Javascript" src="/{hashy}.js"></script>'
            output("rename.html", external)
            output(f"{hashy}.js", obfuscated_content)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted, exiting", end="")
        for i in "...":
            time.sleep(0.1)
            print(i, end='')
        sys.exit(1)