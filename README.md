# python-redis-crud simple code

This repository presents a simple CRUD code using Python and Redis.
The algorithm objective is to elaborate a product database with 
products names, prices, and stash. The script has 7 functions 
that work together to: **list all products**, **insert a product**,
**update a product**, or **delete a product**.

## List function 

The list function is responsible to present every product
registred in the DB.

## Insert function

The insert function requests the product name to be inserted in
the DB, among with its price and stash. It will simple insert
the product in a non-taken key of the DB.

## Update function

The update function is responsible for modifying any product that
already exists in the database. The user is request to prompt
which product to update, and if the product is not in the DB,
the function will not execute.

## Delete function

The delete function takes a product name and delete it from de DB.
