# creating the wallate with a payment key and payment address
from pycardano import Address, Network, PaymentSigningKey, PaymentVerificationKey

# users wallets
class Wallet:
    
    # cardano connection 
    # Connecting to the block chain  and creating an account for each new user
    # address
    def paymentKey(self):

        # sign in key generation
        self.payment_signin_key = PaymentSigningKey.generate()
        # saving the key in a keys file
        self.payment_signin_key.save("payment_key.skey")


        return self.payment_signin_key

    # verificationkey
    def verificationKey(self):

        self.key = self.paymentKey()
        # generating a verification key
        self.payment_verification_key = PaymentVerificationKey.from_signing_key(self.key)
        # saving the verification key
        self.payment_verification_key.save("verification_key.vkey")

        return self.payment_verification_key

    # # payment address
    def address(self, verification_key):

        # net type
        self.network = Network.TESTNET
        # attaching an address
        self.addres = Address(payment_part=verification_key.hash(), network=self.network)

        # getting the address
        return self.address