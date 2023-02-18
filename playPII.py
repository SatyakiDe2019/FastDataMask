#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 12-Feb-2023                     ####
#### Modified On 16-Feb-2023                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### newly created light data masking class.     ####
####                                             ####
#####################################################

import pandas as p
import clsL as cl
from clsConfigClient import clsConfigClient as cf
import datetime

from FastDataMask import clsCircularList as ccl

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

######################################
### Get your global values        ####
######################################
debug_ind = 'Y'
charList = ccl.clsCircularList()

CurrPath = cf.conf['SRC_PATH']
FileName = cf.conf['FILE_NAME']
######################################
####         Global Flag      ########
######################################

######################################
### Wrapper functions to invoke    ###
### the desired class from newly   ###
### built class.                   ###
######################################
def mask_email(email):
    try:
        maskedEmail = charList.maskEmail(email)
        return maskedEmail
    except:
        return ''

def mask_phone(phone):
    try:
        maskedPhone = charList.maskPhone(phone)
        return maskedPhone
    except:
        return ''

def mask_name(flname):
    try:
        maskedFLName = charList.maskFLName(flname)
        return maskedFLName
    except:
        return ''

def mask_date(dt):
    try:
        maskedDate = charList.maskDate(dt)
        return maskedDate
    except:
        return ''

def mask_uniqueid(unqid):
    try:
        maskedUnqId = charList.maskSSN(unqid)
        return maskedUnqId
    except:
        return ''

def mask_sal(sal):
    try:
        maskedSal = charList.maskSal(sal)
        return maskedSal
    except:
        return ''
######################################
### End of wrapper functions.      ###
######################################

def main():
    try:
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('*'*120)
        print('Start Time: ' + str(var))
        print('*'*120)

        inputFile = CurrPath + FileName

        print('Input File: ', inputFile)

        df = p.read_csv(inputFile)

        print('*'*120)
        print('Source Data: ')
        print(df)
        print('*'*120)

        hdr = list(df.columns.values)
        print('Headers:', hdr)

        df["MaskedFirstName"] = df["FirstName"].apply(mask_name)
        df["MaskedEmail"] = df["Email"].apply(mask_email)
        df["MaskedPhone"] = df["Phone"].apply(mask_phone)
        df["MaskedDOB"] = df["DOB"].apply(mask_date)
        df["MaskedSSN"] = df["SSN"].apply(mask_uniqueid)
        df["MaskedSal"] = df["Sal"].apply(mask_sal)

        # Dropping old columns
        df.drop(['FirstName','Email','Phone','DOB','SSN', 'Sal'], axis=1, inplace=True)

        # Renaming columns
        df.rename(columns={'MaskedFirstName': 'FirstName'}, inplace=True)
        df.rename(columns={'MaskedEmail': 'Email'}, inplace=True)
        df.rename(columns={'MaskedPhone': 'Phone'}, inplace=True)
        df.rename(columns={'MaskedDOB': 'DOB'}, inplace=True)
        df.rename(columns={'MaskedSSN': 'SSN'}, inplace=True)
        df.rename(columns={'MaskedSal': 'Sal'}, inplace=True)

        # Repositioning columns of dataframe
        df = df[hdr]

        print('Masked DF: ')
        print(df)

        print('*'*120)
        var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('End Time: ' + str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
