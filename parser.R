library(readxl)
library(tidyverse)

inputData <- read_excel('../openelections-sources-mt/2017/2017-Special-Statewide-Results-by-Precinct.xlsx')

outputDf <- inputData %>%
  transmute(county=CountyName,
            precinct=PrecinctName,
            district=NA_character_,
            office=case_when(
              grepl(x=RaceName, pattern='UNITED STATES REPRESENTATIVE.+') ~ 'U.S. House',
              TRUE ~ RaceName
            ),
            party=case_when(
              PartyCode == 'REP' ~ 'Republican',
              PartyCode == 'DEM' ~ 'Democratic',
              PartyCode == 'LIB' ~ 'Libertarian',
              TRUE ~ NA_character_
            ),
            candidate=NameOnBallot,
            votes=Votes)

write_csv(outputDf, '2017/20170525__mt__special__general__precinct.csv', na = '')