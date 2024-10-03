thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
key = list(thisdict.keys())
value = list(thisdict.values())

position = value.index(1964)
print(key[position])
