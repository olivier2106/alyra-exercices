pragma solidity 0.5.3;

contract Assemblee{
    
    //ma liste de membres
    address[] membres;
    uint indicator=0;
    
    // autres variables pour 3.2 
    //string[] public descriptionDecision;
    //mapping(string => votesTotal) descriptionDecision;
    //string[] public descriptionsDecision;
    
    //uint[] public voteTotal;
    struct VotesTotal
    {
          string[] Description;
          address[] votesPour;
          address[] votesContre;
        //uint start_time;
        //address[] votesPour;
        //address[] votes_against;
        //bool initialized;
        //bool closed;
    }
    
    VotesTotal[] votesTotals;
    
    function comptabiliser(uint indice) public view returns(int){
        return int(votesTotals[indice].votesPour.length - votesTotals[indice].votesContre.length);
    }
      
    function EstMembre(address membre) public returns(bool) {
        
        //we create an indicator variable
        for (uint i=0; i<=membres.length; i++) {
            if (msg.sender!=membres[i]) {
            indicator=indicator;
            }
            else {
                indicator=1;
            }
        }
        // if no new then bool
        if (indicator==1){
            return true;
        }
        else{
            membres.push(msg.sender);
            return false;
        }
    }
    
    function proposerDecision(string memory text) public {
        if(EstMembre(msg.sender)){
            votesTotals.Description.push(text);
            votesTotals.votesConte.push(0);
            votesTotals.votesPour.push(0);
        }
    }
    
    function 
    
    //Définir la fonction voter, qui prend pour paramètres l’indice d’une proposition 
    //de décision et un entier pour déterminer le sens du vote (0 : contre, 1: pour)
    //et incrémente le tableau votePour ou voteContre
    
    function voter(uint indice_proposition, uint sens_vote) public{
        if (sens_vote==1){
        votesTotals.votesPour[indice_proposition].push(msg.sender);
        }
        else{
        votesTotals.votesContre.push(msg.sender);
        }
    }
    
}

