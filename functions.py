import data

#Purpose: To create a function that will calculate the average usage of water given a list of waterrecord objects
#It should separate it by whether there was a drought or not so that it can be used for meaningful comparison
def water_use_average(waterlist:list[data.WaterRecord],category:str,drought:bool)->float:
    total=0
    count=0
    for record in waterlist:
        if record.drought == drought:
            find=match_category(record,category)
            total=total+find
            count=count+1
    return round((total/count),2)

#matches each category which is passed in as a string to the appropriate attribute within the class of WaterRecord.
#this ensures that proper matching occurs and correct values are pulled from each object.
def match_category(record,category):
    match category:
        case 'BAWSCA SF RWS Purchases':
            return record.bawsca
        case 'BAWSCA Total Use':
            return record.bawsca_total_use
        case 'EBMUD Gross Water Production':
            return record.ebmud



