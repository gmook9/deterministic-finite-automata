import itertools

class DfaClass:
    def __init__(self):
        possibleStringList = []
        dictionaryCounter = {}
        counterList = []
        counterList.append(0)
        counterForDict = 0
        possibleStringList.append("")
        for i in range(1, 6):
            for str in itertools.product("abcd", repeat=i):
                someString = ""
                someString = someString.join(str)
                possibleStringList.append(someString)
                counterForDict = counterForDict + 1
                counterList.append(counterForDict)               
        for aString in possibleStringList: 
            key = possibleStringList.index(aString)
            dictionaryCounter[key] = aString
        self.possibleStringList = possibleStringList
        next = [0] * len(self.possibleStringList)
        self.prev = [1] * len(self.possibleStringList)
        self.next = [0] * len(self.possibleStringList)
        self.dictionaryCounter = dictionaryCounter
        
        def grabStateNum(self,inputString):
            CharactersOfTheString = []
            stateNum = 0
            if (inputString == ""):
                return 0
            for char in inputString:
                CharactersOfTheString.append(char)
            for i in range(0, len(CharactersOfTheString)):
                if CharactersOfTheString[i] == 'a':
                    stateNum = stateNum + 1 * pow(4, (len(CharactersOfTheString) - 1) - i)

                elif CharactersOfTheString[i] == 'b':
                    stateNum = stateNum + 2 * pow(4, (len(CharactersOfTheString) - 1) - i)

                elif CharactersOfTheString[i] == 'c':
                    stateNum = stateNum + 3 * pow(4, (len(CharactersOfTheString) - 1) - i)

                elif CharactersOfTheString[i] == 'd':
                    stateNum = stateNum + 4 * pow(4, (len(CharactersOfTheString) - 1) - i)
                else:
                    print("ERROR: NO a,b,c, or d detected")
                    exit(9)
            return stateNum