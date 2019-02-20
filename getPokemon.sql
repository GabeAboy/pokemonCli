/**********************************************************************/
/* This is how to search for just the Pokemon, regardless of location */

SELECT Name, Location, Percent FROM tblPokemon WHERE Name LIKE '%userInput%';

