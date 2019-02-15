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

	//function transfer
	function transfer(address destinataire, uint256 valeur) public {
  
		// critères de transfert de bons points: 
    	require(bonsPoints[msg.sender] > valeur, "Vous ne pocedez pas assez de bons points à transferer!");
		require(bonsPoints[destinataire] > 0, "Seul un destinataire ayant déjà des bons points peut en recevoir!");

		bonsPoints[msg.sender] -= valeur;
		bonsPoints[destinataire] += valeur;
	}

	//function combien de points
	function pointAllocation(address devoirs, uint256 valeur) public returns(uint256 position) {

	//we need a pointer for order of arrival
	uint256 devoirs_rendus=devoirs.length;

	//verifications
	//deja rendu un devoir

	require (bonPoints[msg.sender].value == 0); //je veux qu il n ait pas de points  
	//la variable est elle par degaut a 0
	
	//le devoir a t il deja ete rendu?
	//pour savoir on va comparer l input avec les devoirs 
	//si pas deja la then je le rajoute
	for (uint i = 0; i < devoirs_rendus; i++)
		{
			require(devoirs_hash != devoirs[i], "Bien Tenté!"); //il me faut la derniere entree
		}
	devoirs.push(devoirs_hash);
	
	//si mes verifications sont OK
	//we poitn allocate based on order arrival
	for (uint i = 0; i < nb_devoirs; i++)
		{
		if (nb_devoirs==0)	{
			bonsPoints[msg.sender]==30
		}
		else if(nb_devoirs==1)	{
			bonsPoints[msg.sender]==20
		}
		else{
			bonsPoints[msg.sender]==10
		}
		}
		

	}
	