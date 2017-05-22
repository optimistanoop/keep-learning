Hashing is a common technique for storing data in such a way that the data can be inserted and retrieved very quickly. Hashing uses a data structure called a hash table. Although hash tables provide fast insertion, deletion, and retrieval, they perform poorly for operations that involve searching, such as finding the minimum and maximum values in a data set. For these operations, other data structures such as the binary search tree are more appropriate. We’ll learn how to implement a hash table in this chapter and learn when it’s appropriate to use hashing as a data storage and retrieval technique.

## An Overview of Hashing
The hash table data structure is designed around an array. The array consists of elements 0 through some predetermined size, though we can increase the size when necessary. Each data element is stored in the array based on an associated data element called the key, which is similar to the concept of the key we examined with the dictionary data structure. To store a piece of data in a hash table, the key is mapped into a number in the range of 0 through the hash table size, using a hash function.
Ideally, the hash function stores each key in its own array element. However, because there are an unlimited number of possible keys and a limited number of array elements (theoretical in JavaScript), a more realistic goal of the hash function is to attempt to distribute the keys as evenly as possible among the elements of the array.

Even with an efficient hash function, it is possible for two keys to hash (the result of the hash function) to the same value. This is called a collision, and we need a strategy for handling collisions when they occur. We’ll discuss how to deal with collisions in detail later in the chapter.

The last thing we have to determine when creating a hash function is how large an array to create for the hash table. One constraint usually placed on the array size is that it should be a prime number. We will explain why this number should be prime when we
examine the different hash functions. After that, there are several different strategies for determining the correct array size, all of them based on the technique used to handle collisions, so we will examine this issue when we discuss handling collisions. Figure 8-1 illustrates the concept of hashing using the example of a small phone book.

## A Hash Table Class
We need a class to represent the hash table. The class will include functions for com‐ puting hash values, a function for inserting data into the hash table, a function for retrieving data from the hash table, and a function for displaying the distribution of data in the hash table, as well as various utility functions we might need.
Here is the constructor function for our HashTable class:

```javascript
function HashTable() { 
 this.table = new Array(137); 
 this.simpleHash = simpleHash; 
 this.showDistro = showDistro;                 
 this.put = put;
 //this.get = get;
}
```
          
The get() function is commented out for now; we’ll describe its definition later in the chapter.

## Choosing a Hash Function

The choice of a hash function depends on the data type of the key. If your key is an integer, then the simplest hash function is to return the key modulo the size of the array. There are circumstances when this function is not recommended, such as when the keys all end in 0 and the array size is 10. This is one reason the array size should always be a prime number, such as 137, which is the value we used in the preceding constructor
function. Also, if the keys are random integers, then the hash function should more evenly distribute the keys. This type of hashing is known as modular hashing.

In many applications, the keys are strings. Choosing a hash function to work with string keys proves to be more difficult and should be chosen carefully.

A simple hash function that at first glance seems to work well is to sum the ASCII value of the letters in the key. The hash value is then that sum modulo the array size. Here is the definition for this simple hash function:
function simpleHash(data) {
```javascipt
var total = 0;
for (var i = 0; i < data.length; ++i) {
          total += data.charCodeAt(i);
   }
return total % this.table.length; 
}
```
We can finish up this first attempt at the HashTable class with definitions for put() and showDistro(), which place the data in the hash table and display the data from the hash table respectively. Here is the complete class definition:
function HashTable() { this.table = new Array(137); this.simpleHash = simpleHash; this.showDistro = showDistro; this.put = put;
```javascipt
//this.get = get;
}
function put(data) {
var pos = this.simpleHash(data); this.table[pos] = data;
}
function simpleHash(data) {
var total = 0;
for (var i = 0; i < data.length; ++i) {
          total += data.charCodeAt(i);
       }
return total % this.table.length; }
function showDistro() { varn=0;
for (var i = 0; i < this.table.length; ++i) { if (this.table[i] != undefined) {
print(i + ": " + this.table[i]); }
} }
```
Example 8-1 demonstrates how the simpleHash() function works. Example 8-1. Hashing using a simple hash function
load("HashTable.js");
```javascipt
var someNames = ["David", "Jennifer", "Donnie", "Raymond",
"Cynthia", "Mike", "Clayton", "Danny", "Jonathan"]; var hTable = new HashTable();
for (var i = 0; i < someNames.length; ++i) { hTable.put(someNames[i]);
}
hTable.showDistro();
```
Here is the output from Example 8-1:
    35: Cynthia
    45: Clayton
    57: Donnie
    77: David
    95: Danny
    116: Mike
    132: Jennifer
    134: Jonathan
The simpleHash() function computes a hash value by summing the ASCII value of each name using the JavaScript function charCodeAt() to return a character’s ASCII value. The put() function receives the array index value from the simpleHash() function and stores the data element in that position. The showDistro() function displays where the names are actually placed into the array using the hash function. As you can see, the data is not particularly evenly distributed. The names are bunched up at the beginning and at the end of the array.
There is an even bigger problem than just the uneven distribution of names in the array, however. If you pay close attention to the output, you’ll see that not all the names in the original array of names are displayed. Let’s investigate further by adding a print() statement to the simpleHash() function:
```javascipt
function simpleHash(data) {
var total = 0;
for (var i = 0; i < data.length; ++i) {
          total += data.charCodeAt(i);
       }
       print("Hash value: " + data + " -> " + total);
return total % this.table.length; }
```
When we run the program again, we see the following output:
    Hash value: David -> 488
    Hash value: Jennifer -> 817
    Hash value: Donnie -> 605
    Hash value: Raymond -> 730
    Hash value: Cynthia -> 720
    Hash value: Mike -> 390
    Hash value: Clayton -> 730
    Hash value: Danny -> 506
    Hash value: Jonathan -> 819
    35: Cynthia
    45: Clayton
    57: Donnie
    77: David
    95: Danny
    116: Mike
    132: Jennifer
    134: Jonathan
    
The problem is now apparent—the strings "Clayton" and "Raymond" hash to the same value, causing a collision. Because of the collision, only "Clayton" is stored in the hash table. We can improve our hash function to avoid such collisions, as discussed in the next section.
