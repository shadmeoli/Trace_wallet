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


AFRICASTALKING_API_KEY = "531e953c6f3b65c5ef99258e2d568d6d15d7822c61de6396caf4a93823022cab"
AFRICASTALKING_USERNAME = "pllkenya"

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
        phoneNumber = []

        # sms
        self.sms = africastalking.SMS
        # response
        self.OTPMessage = self.sms.send(f"Here is your OTP {the_OTP} do not share it with anyone", phoneNumber)  # user defined phone number

        return (self.OTPMessage, wlt.verificationKey)
