    function EstOrga(address orga) public returns(bool) {
        
        //we create an indicator variable
        for (uint i=0; i<=orga.length; i++) {
            if (msg.sender!=orga[i]) {
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
            orga.push(msg.sender);
            return false;
        }
    }