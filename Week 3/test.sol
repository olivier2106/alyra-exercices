pragma solidity ^0.5.3;

import "github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

contract Credibilite {
  using SafeMath for uint256;
	mapping (address => uint256) public bonsPoints;
	bytes32[] private devoirs;
	address destinataire; 
	uint256 valeur; 
  
  // fonction de hachage au format bytes32: 
	function produireHash(string memory devoirs) public pure returns(bytes32 devoirs_hash) {
		return keccak256(bytes(devoirs));
	}

	function transfer(address destinataire, uint256 valeur) public {
  
		// critères de transfert de bons points: 
    	require(bonsPoints[msg.sender] > valeur, "Vous ne pocedez pas assez de bons points à transferer!");
		require(bonsPoints[destinataire] > 0, "Seul un destinataire ayant déjà des bons points peut en recevoir!");

		bonsPoints[msg.sender] -= valeur;
		bonsPoints[destinataire] += valeur;
	}

	function remettre(bytes32 devoirs_hash) public returns(uint position) {
  
  // verifier qu el'élève n'a pas encore rendu de devoir 
		require(bonsPoints[msg.sender] == 0, "Vous avez déjà rendu un devoir!");
		//cela aurait il marche? je veux pouvoir utiliser l info associé à l adresse
		require(bonsPoints[msg.sender].valeur == 0, "Vous avez déjà rendu un devoir!");
		//
		uint ordreDArrivee = devoirs.length;

		for (uint i = 0; i < ordreDArrivee; i++)
		{
   
   // verifier que le devoir est différent d'un autre déjà rendu 
    	require(devoirs_hash != devoirs[i], "Ce devoir a déjà été rendu par un autre élève!");
		}

		devoirs.push(devoirs_hash);

		if (ordreDArrivee == 0)
		{
			bonsPoints[msg.sender] = 30;
		}
		else if (ordreDArrivee == 1)
		{
			bonsPoints[msg.sender] = 20;
		}
		else if (ordreDArrivee > 1)
		{
			bonsPoints[msg.sender] = 10;
		}

		return ordreDArrivee + 1;
	}
}