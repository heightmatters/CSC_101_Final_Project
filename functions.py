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

#Purpose: to create a function that calculates the year to year percent change for a given category and returns a list of from_year, to_year, & percent_change
def percent_change(waterlist:list[data.WaterRecord],category: str) -> list[tuple[int,int,float]]:
    def get_year(record: data.WaterRecord) -> int:
        return record.year
    ordered = sorted(waterlist, key=get_year)
    changes = []
    for i in range(len(ordered) - 1):
        prev = ordered[i]
        curr = ordered[i + 1]
        prev_val = match_category(prev, category)
        curr_val = match_category(curr, category)
        if prev_val == 0:
            continue
        change = ((curr_val - prev_val) / prev_val) * 100
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


