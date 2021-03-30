#!/usr/bin/python

oldDict = {
  "path1": "hash1",
  "path2": "hash2",
  "path3": "hash3"#!/usr/bin/python

}

newDict = {
  "path1": "has1",
  "path2": "has2",
  "path4": "hash3",
  "path5": "hash5"
}
oldFilePaths = oldDict.keys() #list of keys
newFilePaths = newDict.keys() #list of keys
oldvalue = oldDict.values()
newvalue = newDict.values()
newvalue = newDict.values()

updateList = []
newList = []

for key in newFilePaths:
        if key not in oldFilePaths:
                newList.append({key,newDict[key]})
        else:
                if oldDict[key] == newDict[key]:
                        continue
                else:
                        updateList.append({key,newDict[key]})
