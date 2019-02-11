/**********************************************************************/
/* This is how to search for just the Pokemon, regardless of location */

SELECT tblPokemon.Name, tblPokemon.Location, tblPokemon.Percent FROM tblPokemon.Name WHERE tbl.Pokemon LIKE '%userInput%';


/*********************************************/
/* This is how to search regions for Pokemon */

SELECT tblPokemon.Name, tblPokemon.Location, tblPokemon.Percent FROM tblPokemon JOIN tblPosition tblPokemon.Route = tblPostition.Location WHERE tblPosition.Location LIKE '%userInput%';

/***************************/
/* Route Information Query */

SELET tblPosition.Connections, tblPosition.Location FROM tbl.Position WHERE tblPosition.Location LIKE '%userInput%'