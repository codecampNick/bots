import re

patterns = []
# city, state code zip short description - 'Denver, CO 80209 (Washington Park area)'
# city, state code zip - 'Highlands Ranch, CO 80129'
patterns.append('^([^,]+),\s*([A-Z]{2}\s*([\d]{5})).*')
#Castle Rock, CO
patterns.append('^\s*([^,]+),\s*([A-Z]{2})\s*$')

class Job:
    def __init__(self):
        self.Id = ''
        self.CompanyName = ''
        self.Title = ''
        self.Headline = ''
        self.Description = ''
        self.Specialty = ''
        self.Salary = ''
        self.City = ''
        self.State = ''
        self.Country = ''
        self.Zip = ''
        self.UrlToPosting = ''
        self.RecruiterName = ''
        self.RecruiterID = None
    
#def dictClear(self):
#    for key, value in self.__dict__.items():
#        print(k)

#formats matched
# city, state code zip short description - 'Denver, CO 80209 (Washington Park area)'
# city, state code zip - 'Highlands Ranch, CO 80129'
    
    def get_city(self, sLocation):
        for p in patterns:
            m = re.search(p,sLocation)
            if m :
                match =  re.match(p, sLocation)
                #print(match.group(1))
                print('matched')
                return m.group(1)

    def get_state(self, sLocation):
        for p in patterns:
            m = re.search(p,sLocation)
            if m and (len(m.groups()) == 3 or len(m.groups()) == 2):
                match =  re.match(p, sLocation)
                #print(match.group(1))
                print('matched')
                return m.group(2)

    def get_country(self, sLocation):
        for p in patterns:
            m = re.search(p,sLocation)
            if m and len(m.groups()) == 3:
                match =  re.match(p, sLocation)
                print('matched')
                return m.group(0)

    def get_zip(self, sLocation):
        for p in patterns:
            m = re.search(p,sLocation)
            if m and len(m.groups()) == 3:
                match =  re.match(p, sLocation)
                print('matched')
                return m.group(3)

    def clear(self):
        self.Id = ''
        self.CompanyName = ''
        self.Title = ''
        self.Headline = ''
        self.Description = ''
        self.Specialty = ''
        self.Salary = ''
        self.City = ''
        self.State = ''
        self.Country = ''
        self.Zip = ''
        self.UrlToPosting = ''
        self.RecruiterName = ''
        self.RecruiterID = 0

