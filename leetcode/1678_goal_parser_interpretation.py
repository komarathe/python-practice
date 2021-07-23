class Solution:
    def interpret(self, command: str) -> str:
        new_str = ""
        for i in range(0, len(command)):
            if command[i] == "G":
                new_str = new_str + command[i]
            elif (command[i] == "(") and (command[i + 1] == ")"):
                new_str = new_str + "o"
            elif (command[i] == "(") and (command[i + 1] != ")"):
                new_str = new_str + "al"
        return new_str