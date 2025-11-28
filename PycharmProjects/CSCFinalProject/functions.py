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

#Purpose: to create a function that calculates the year to year percent change for a given category and returns a list of
#from_year, to_year, & percent_change
def percent_change(waterlist:list[data.WaterRecord],category: str) -> list[tuple[int,int,float]]:
    #helper function to get the year of each WaterRecord object
    def get_year(record: data.WaterRecord) -> int:
        return record.year
    #sorts list of objects by the year
    ordered = sorted(waterlist, key=get_year)
    changes = []
    for i in range(len(ordered) - 1):
        #comparing year to year
        prev = ordered[i]
        curr = ordered[i + 1]
        #using previous helper function to target a specific attribute of the object
        prev_val = match_category(prev, category)
        curr_val = match_category(curr, category)
        #checking for divide by zero error
        if prev_val == 0:
            continue
        #finding the precent change and then appending it as a tuple which holds the two years compared and the
        #percent change.
        change = ((curr_val - prev_val) / prev_val) * 100
        #biggest difference between a tuple and any other kind of data storage is the fact that they are immutable
        #This makes it easier to store data that will never be changed. Along with this, it can store multiple different
        #data types which is useful for our purposes.
        changes.append((prev.year, curr.year, round(change, 2)))
    return changes

#Purpose: to compare the average drought vs non drought usage for a category. returns the percent difference (drought vs non drought)
def compare_water_use(waterlist:list[data.WaterRecord],category: str) -> float | None:
    avg_drought=water_use_average(waterlist,category,True)
    avg_nondrought=water_use_average(waterlist,category,False)
    if avg_nondrought==0:
        return None
    pct=((avg_drought-avg_nondrought)/avg_nondrought)*100
    return round(pct,2)





