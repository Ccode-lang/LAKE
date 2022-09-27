import LAKE
cyphertext = LAKE.encrypt("helloworld", "agoodkey")
plaintext = LAKE.decrypt(cyphertext, "agoodkey")
print(plaintext)