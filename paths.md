# Path Generator Overview

## Setup
### MVP
Create Fresh Temp Folder/Files:
- temp_default/
- temp_default/failures.txt

## Run Individual Tests - Track Coverage, failures
### MVP
Iterate over tests
- create unique cover file for each 
  - temp/test_\[class\]_\[test_number\] subdirectory? Or
  - figure out how to name/limit cover files
- record failures

## Analyze individual covers / Form Weighted Paths based on cover analyses
### MVP
Iterate over results
- Given a line id and success/failure result,
- For each line, add_positive/negative weight to the path 

## Output Weighted Path
### MVP
Output trace object 
- json dump? write to file?

## Cleanup
### MVP
Nothin