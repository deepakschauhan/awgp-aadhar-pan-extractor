from awgp_aadhar_pan_extractor import Aadhar_Info_Extractor,Pan_Info_Extractor
import argparse

# YOU CAN FETCH ON AADHAR CARD DATA SO YOU WILL USE THIS classmethod

# python test_adhar.py -a AADHAR

# YOU CAN FETCH ON PAN CARD DATA SO YOU WILL USE THIS classmethod

# python test_adhar.py -p PAN

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pan", required=False,help="please pan card call -p")
ap.add_argument("-a", "--aadhar", required=False,help="please aadhar card call -a")
args = vars(ap.parse_args())
# print(args["pan"])

if args["pan"] == 'PAN':
    pan = Pan_Info_Extractor()
    result = pan.info_extractor('pan.jpeg')
    print(result)
elif args["aadhar"] == "AADHAR":
    aadhar = Aadhar_Info_Extractor()
    result = aadhar.info_extractor('adhar_card1212.jpg')
    print(result)


