pragma solidity 0.5.3;
contract Assemblee{
    
    //ma liste de membres
    address[] membres;
    uint indicator=0;
    
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
}

