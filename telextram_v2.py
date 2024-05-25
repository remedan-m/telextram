import json
import argparse


def get_one_way_txt():
    matches = []
    words = 0
    for message in json_to_python_obj["messages"]:
        try:
            if message["from"] == target_username:
                match = message['text']
                matches.append(match)
                words+=len(match)
        except:
            continue

    f = open(output_file+'.txt', 'w') 

    for i in matches:
        f.write(str(f">>> {i}\n"))

    f.close()
    print(f"[+] Line of message: {len(matches)}")
    print(f"[+] Words in a message: {words}")


def get_two_way_txt():
    matches = []
    words = 0
    for message in json_to_python_obj["messages"]:
        try:
            match = message['text']
            matches.append(match)
            words+=len(message)
        except:
            continue
        
    f = open(output_file+'.txt', 'w') 
    f.write(f"Total message conversation: {len(matches)}\n")
    for i in matches:
        f.write(str(f">>> {i}\n"))
    
    f.close()
    print(f"[+] Line of message: {len(matches)}")
    print(f"[+] Words in a message: {words}")


if __name__== "__main__":
    
    parser = argparse.ArgumentParser(description="> a tool to extract telegram chat messages from json data.")

    parser.add_argument("-f", "--file", type=str, 
                        help="Full path for the json data file.")
    parser.add_argument("-u", "--username", type=str,                
                        help="The Name of the user to extact the messages.")
    parser.add_argument("-o", "--out_file", type=str, default="result",
                        help="Provide a file name to save the messages.")
    parser.add_argument("-b", "--both", action="store_true",
                        help="Enables To extract both/every users messages.")

    args = parser.parse_args()

    json_data_obj = open(args.file, 'r')
    target_username = args.username
    output_file = args.out_file
    try:
        json_to_python_obj = json.load(json_data_obj)
    except:
        print("somthing wrong with the json file!")


banner = """
+-+-+-+-+-+-+-+-+-+
|T|e|l|e|x|t|r|a|m|.v2
+-+-+-+-+-+-+-+-+-+ 
            developed by github@remedan-m.
"""

if args.username:
    print(banner)
    print("[+] one way message enabled.")
    print(f"[+] using username {args.username}.")
    get_one_way_txt()
    print("."*10,"Done","."*10)
else:
    if args.both:
        pass
    else:
        print(banner)
        print("[!] No username is sepecified.")
if args.both:
    print(banner)
    print("[+] two way message enabled.")
    get_two_way_txt()
    print("."*10,"Done","."*10)
else:
    if args.username:
        pass
    else:
        print("[!] No -b/--both flag is provided.")
    print("use a -h/--help flag to see usage manual.")


