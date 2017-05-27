## Handling Collisions

>A collision occurs when a hash function generates the same key for two or more values. 
There are two ways of collision resolution: separate chaining and linear probing.

### Separate Chaining
When a collision occurs, we still need to be able to store the key at the generated index, but it is physically impossible to store more than one piece of data in an array element. Separate chaining is a technique where each array element of a hash table stores another data structure, such as another array, which is then used to store keys. Using this technique, if two keys generate the same hash value, each key can be stored in a different position of the secondary array. Figure 8-2 illustrates how separate chaining works.
Figure 8-2. Separate chaining
To implement separate chaining, after we create the array to store the hashed keys, we call a function that assigns an empty array to each array element of the hash table. This creates a two-dimensional array. The following code defines a function, buildChains(), to create the second array (we’ll also refer to this array as a chain), as well as a small program that demon‐ strates how to use buildChains():

function buildChains() {
for (var i = 0; i < this.table.length; ++i) {
this.table[i] = new Array(); }
}
Add the preceding code, along with a declaration of the function, to the definition of the HashTable class.
A program to test separate chaining is shown in Example 8-5. Example 8-5. Using separate chaining to avoid collisions
load("HashTable.js");
var hTable = new HashTable();
hTable.buildChains();
var someNames = ["David", "Jennifer", "Donnie", "Raymond",
"Cynthia", "Mike", "Clayton", "Danny", "Jonathan"]; for (var i = 0; i < someNames.length; ++i) {
   hTable.put(someNames[i]);
}
hTable.showDistro();
In order to properly display the distribution after hashing with separate chaining, we need to modify the showDistro() function in the following way to recognize that the hash table is now a multidimensional array:
function showDistro() { varn=0;
for (var i = 0; i < this.table.length; ++i) { if (this.table[i][0] != undefined) {
print(i + ": " + this.table[i]); }
} }
When we run the program in Example 8-5, we get the following output:
    60: David
    68: Jennifer
    69: Mike
    70: Donnie,Jonathan
    78: Cynthia,Danny
    88: Raymond,Clayton
Next we need to define the put() and get() functions that will work with separate chaining. The put() function hashes the key and then attempts to store the data in the first cell of the chain at the hashed position. If that cell already has data in it, the function searches for the first open cell and stores the data in that cell. Here is the code for the put() function:
function put(key, data) {
var pos = this.betterHash(key);
var index = 0;
if (this.table[pos][index] == undefined) {
this.table[pos][index+1] = data; }
++index; else {
while (this.table[pos][index] != undefined) { ++index;
}
this.table[pos][index] = data; }
}
Unlike the example earlier when we were just storing keys, this put() function has to store both keys and values. The function uses a pair of the chain’s cells to store a key- value pair; the first cell stores the key and the adjacent cell of the chain stores the value.
The get() function starts out by hashing the key to get the position of the key in the hash table. Then the function searches the cells until it finds the key it is looking for. When it finds the correct key, it returns the data from the adjacent cell to the key’s cell. If the key is not found, the function returns undefined. Here is the code:
function get(key) {
var index = 0;
var hash = this.betterHash(key); if (this.table[pos][index] = key) {
return this.table[pos][index+1]; }
index += 2; else {
while (this.table[pos][index] != key) { index += 2;
}
return this.table[pos][index+1]; }
return undefined; }
