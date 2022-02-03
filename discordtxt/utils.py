from typing import Dict, List
import re
from .cmds import openFile

def parseLine(line: str) -> None:
    """Parses one line of the txt file"""

def parseConfig(file_data: str) -> Dict:
    return_dict = {}
    file_lines = file_data.split('\n')
    for i in file_lines:
        if "client" in i:
            if "presencetext" in i:
                return_dict["presencetext"] = re.compile("client presencetext (.*)").findall(i)[0]
            else: return_dict[(i.split(' '))[1]] = (i.split(' '))[2]

    return return_dict

def parseCommands(file_data: str) -> List:
    return_list = []
    file_lines = file_data.split('\n')
    for i in file_lines:
        if i.startswith("command"):
            name = re.compile("command (.*)").findall(i)[0]
            ret = parseCommandArgs(file_data, name)
            ret["name"] = name 
            return_list.append(ret)
    return return_list
        
def parseCommandArgs(file_data: str, cmdname: str) -> Dict:
    return_dict = {}
    file_lines = file_data.split('\n')
    for i in file_lines:
        if i.startswith(cmdname):
            split_cmd = i.split(' ')
            if split_cmd[1] == "description": return_dict["description"] = re.compile(f"{cmdname} description (.*)").findall(i)[0]
            # elif split_cmd[1] == "arguments": return_dict["args"] = re.compile(f"{cmdname} arguments (.*)").findall(i)[0]
            elif split_cmd[1] == "message": return_dict["message"] = re.compile(f"{cmdname} message (.*)").findall(i)[0]
            elif split_cmd[1] == "aliases": return_dict["aliases"] = re.compile(f"{cmdname} aliases (.*)").findall(i)[0]

    return return_dict

def parseRunLine(file_data: str) -> str:
    file_lines = file_data.split('\n')
    for i in file_lines:
        if i.startswith("run openfile"):
            location = re.compile("run openfile (.*)").findall(i)[0]
            token_data = openFile(location)
            return token_data
        elif i.startswith("run"):
            token_data = i.split(" ")[1]
            return token_data
