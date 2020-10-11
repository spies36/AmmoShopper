# Set webpages to watch for availability
# Possible sites to watch: LuckyGunner

class Sites:
    # LuckyGunner
    LuckyGunner = False #True to search, False to ignore
    LuckyGunnerLinks = ['https://www.luckygunner.com/223-rem-55-grain-fmjbt-federal-american-eagle-400-rounds','https://www.luckygunner.com/223-rem-62-grain-fbhp-nosler-varmageddon-20-rounds','https://www.luckygunner.com/fiocchi-223-ammo-for-sale-223rem55fmjfiocchi-1000']
    LuckyGunnerQuantity = [2,2,3]
    LuckyGunnerMaxPricePerItem = [30,25,30] #per item NOT round
    #OutDoorLimited
    OutdoorLimited = False #True to search, False to ignore
    OutdoorLimitedLinks = ['https://www.outdoorlimited.com/specials/bulk-ammo-case-pricing/sellier-bellot-9mm-luger-ammunition-sb9b-124-grain-full-metal-jacket-case-1000-rounds/','https://www.outdoorlimited.com/rifle-ammo/223-remington-ammo/pmc-223-rem-ammunition-bronze-pmc223a-55-grain-full-metal-jacket-boat-tail-20-rounds/','https://www.outdoorlimited.com/rifle-ammo/300-aac-blackout-ammo/sellier-bellot-300-aac-blackout-ammunition-subsonic-300blksuba-200-grain-full-metal-jacket-case-of-1-000-rounds/']
    OutdoorLimitedQuantity = [2,2,3]
    OutdoorLimitedMaxPricePerItem = [800,30,1000] #per item NOT round
    #TargetSportsUSA
    TargetSportsUSA = True
    TargetSportsUSALinks = ['https://www.targetsportsusa.com/fiocchi-shooting-dynamics-9mm-luger-ammo-147-grain-fmj-9apd-p-2961.aspx', 'https://www.targetsportsusa.com/federal-american-eagle-223-remington-ammo-55-grain-fmj-bulk-1000-rounds-ae223bk-p-1478.aspx', 'https://www.targetsportsusa.com/tula-ammo-7-62-39mm-ammo-124-grain-full-metal-jacket-steel-case-ul076209-p-109805.aspx']
    TargetSportsUSAQuantity = [1,1,1]
    TargetSportsUSAMaxPricePerItem = [25,700,200] #per item NOT round
    TargetSportsUSAEmail = 'dylan.spies36@gmail.com'
    TargerSportsUSAPassword = 'hereIsMyCode12'

class PurchaseInfo:
    FirstName = 'FirstName'
    LastName = 'LastName'
    Address = '1920 Nightwalk ct.'
    Address2 = None
    ZipCode = '37130'
    City = 'Murfreesboro'
    State = 'Tennessee'
    Phone = '615-456-7890'
    EmailAddress = 'myEmail@email.com'

class PurchaseParameters:
    CurrentSpent = 0.00 #Do not edit this field
    Allowance = 1000.00    #Use format of 0.00 Do not use $


class WebInterface:
    #Add path below
    path = ('C:\Program Files (x86)\chromeDriver.exe')
