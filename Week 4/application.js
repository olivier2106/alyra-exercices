let dapp={};

async function createMetaMaskDapp() {
 try {
   // Demande à MetaMask l'autorisation de se connecter
   const addresses = await ethereum.enable();
   const address = addresses[0]
   // Connection au noeud fourni par l'objet web3
   const provider = new ethers.providers.Web3Provider(ethereum);
   dapp = { address, provider };
   console.log(dapp);
 } catch(err) {
   // Gestion des erreurs
   console.error(err);
 }
}

/*async function enableMetaMask() {
if (ethereum) {
 try {
   const [ address ] = await ethereum.enable();
   return address;
 } catch (err) {
   throw err;
 }
} else {
 alert('This super awesome app need MetaMask to work. Install it and come back');
 throw new Error('Ethereum is not available here');
}
}
async function createMetaMaskDapp() {
try {
 const address = await enableMetaMask();
 const provider = new ethers.providers.Web3Provider(ethereum);
 const signer = provider.getSigner();
 dapp = { address, provider };
   console.log(dapp)
 } catch(err) {
   // Gestion des erreurs
   console.error(err);
 }
}
*/