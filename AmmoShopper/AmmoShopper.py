from config import *
from LuckyGunnerNav import *
from OutDoorLimitedNav import *
from TargetSportsUSANav import *
print(Sites.LuckyGunner, ' It works. ', Sites.LuckyGunnerLinks)
if(Sites.LuckyGunner):
    ScrapeLuckyGunner()
if(Sites.OutdoorLimited):
    ScrapeOutdoorLimited()
if(Sites.TargetSportsUSA):
    ScrapeTargetSportsUSA()