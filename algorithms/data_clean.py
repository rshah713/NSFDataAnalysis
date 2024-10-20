import pandas as pd

class BaseReader():
    def __init__(self):
        pass

    def _get_attribute(self, row,  attr: str, range=None) -> str:
        if range is None:
            if pd.notnull(row[attr]):
                return row[attr]
            elif pd.notnull(row[f'{attr}.1']):
                return row[f'{attr}.1']
            return row[f'{attr}.2']
        else:
            for i in range[:2]:
                if pd.notnull(row[f'{attr}.{i}']):
                    return row[f'{attr}.{i}']
            return row[f'{attr}.{range[2]}']

    def scan_contents(self):
        '''
        schema: 
        [
            {
                "batch": "fall 2015",
                "date created": "2015-09-14 19:28:45",
                "Student First Name": "Robert",
                "Student Last Name": "Giola",
                "Gender": "Male",
                "Race": "White"
            },
            {
                "batch": "fall 2016",
                "date created": "2015-09-14 19:28:45",
                "Student First Name": "Bob",
                "Student Last Name": "Smith",
                "Gender": "Male",
                "Race": "Non-White"
            }
        ]
        '''
        contents = []

        entry = {}
        df = pd.read_excel('data/fall+2015++nsf+i-corps+at+njit_entries.xlsx')
        for index, row in df.iterrows():
            entry = {}
            
            entry['first name'] = row['Student Entrepreneur Name ']
            entry['last name'] = row['Last']
            entry['gender'] = self._get_attribute(row, 'Student Entrepreneur \nDemographic Information - \n\nGender')
            entry['race'] = self._get_attribute(row, 'Race')
            entry['ethnicity'] = self._get_attribute(row, 'Ethnicity')
            entry['faculty advisor gender'] = self._get_attribute(row, 'Faculty Advisor\nDemographic Information - \n\nGender')
            entry['faculty advisor race'] = self._get_attribute(row, 'Race', range=(3, 4, 5))
            entry['faculty advisor ethnicity'] = self._get_attribute(row, 'Ethnicity', range=(3,4,5))
            entry['entreprenuer mentor gender'] = self._get_attribute(row, 'Entrepreneurial Mentor\nDemographic Information - \n\nGender')
            entry['entreprenuer mentor race'] = self._get_attribute(row, 'Race', range=(6,7,8))
            entry['entreprenuer mentor ethnicity'] = self._get_attribute(row, 'Ethnicity', range=(6,7,8))
            
            entry['batch'] = 'Fall 2015'
            # print(entry)
            contents.append(entry)

        # finished 2015 sheet above
        # try to replicate here for other sheets
        # heres some psuedocode:

        # read excel sheet (filename)
        # loop thru rows:
        #   create a new entry dict
        #   store whatever you want, try to be consistent with the naming like above
        # add entry object to contents list
        # 
        #
        # do whatever stats you want in calculate_trends.py
            
        return contents
    

        




if __name__ == "__main__":
    BaseReader().scan_contents()
