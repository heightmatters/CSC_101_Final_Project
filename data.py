#class for inputting water data

class WaterRecord:
    #simplifying some of the terms for easier use in code
    #remember to apply proper meanings of each term when creating presentation
    #intializing each attribute to be equivalent to a part of the table (one column each)
    def __init__(self,
                 year:int,
                 bawsca:float,
                 bawsca_total_use:float,
                 ebmud:float,
                 drought:bool):
        self.year = year
        self.bawsca = bawsca
        self.bawsca_total_use = bawsca_total_use
        self.ebmud = ebmud
        self.drought = drought

    #making a simple repr dunder method
    def __repr__(self):
        return (
            "Water Record("
            "Year: {}, "
            "BAWSCA SF RWS Purchases: {}, "
            "BAWSCA Total Use: {}, "
            "EBMUD Gross Water Production: {}, "
            "Drought: {}"
            ")"
        ).format(
            self.year,
            self.bawsca,
            self.bawsca_total_use,
            self.ebmud,
            self.drought,
        )

#use this class to make a list in the intial code



