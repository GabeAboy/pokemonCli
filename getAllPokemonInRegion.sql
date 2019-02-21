
/*********************************************/
/* This is how to search regions for Pokemon */

SELECT tblPokemon.Name, tblPokemon.Location, tblPokemon.Percent FROM tblPokemon JOIN tblPosition ON tblPokemon.Route = tblPosition.Location WHERE tblPosition.Location LIKE '%userInput%';
