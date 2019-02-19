
/*********************************************/
/* This is how to search regions for Pokemon */

SELECT tblPokemon.Name, tblPokemon.Location, tblPokemon.Percent FROM tblPokemon JOIN tblPosition tblPokemon.Route = tblPostition.Location WHERE tblPosition.Location LIKE '%userInput%';
