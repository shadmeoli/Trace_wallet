import json
from requests import *

# getting use generated keys
from wallet import Wallet

# random words generation
from random import randint
import random
from nltk import *

# 2Factor authentication
import africastalking


AFRICASTALKING_API_KEY =API_KEY
AFRICASTALKING_USERNAME = API_USERNAME

# API initilization
africastalking.initialize(AFRICASTALKING_USERNAME, AFRICASTALKING_API_KEY)


# 4 digit OTP generation
def OTPGeneration():
    # random 4 digit integers
    generatedOTP = r = random.randint(1111,9999)

    return generatedOTP

# writing the generated keys to a json file
class Response:

    # getting the keys from the users registration
    def UserKeys(self):
        pass

# mail the cretendtials to the users mail
class TwoFactorAuth:

    # sending the OTP with Africastalking API
    def OTP(self):

        """
        API
        """

        # users key
        wlt = Wallet

        # self.vKey = wlt.verificationKey() 
        # definng a random int and attaching it to a json file
        self.GeneratedOTP = OTPGeneration()

        self.Auth = {
            self.GeneratedOTP : wlt.verificationKey
        }

        # otp generation
        the_OTP = self.GeneratedOTP
        # phone number
        phoneNumber = ["+254705379181"]

        # sms
        self.sms = africastalking.SMS
        # response
        self.OTPMessage = self.sms.send(f"Here is your OTP {the_OTP} do not share it with anyone", ["+254705379181"])  # user defined phone number

        return self.OTPMessage


if __name__ == "__main__":
    tf = TwoFactorAuth()
    tf.OTP()
