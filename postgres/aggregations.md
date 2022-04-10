1. `array_agg`
    - Returns the input values, pivoted into an ARRAY. If the input is empty, an empty ARRAY is returned.
    - `SELECT ARRAY_AGG(name) FROM person;`
        -> `{mike, jeff, tim}`

1. `bool_or`
    - Returns true if any non-null input value is true, otherwise false.

1. `bool_and`
    - Returns true if all non-null input values are true, otherwise false.

Examples: 
```
with sample_data (id, start_date) as (
   values 
      (1, current_date - 1), 
      (2, current_date + 1) 

)
select bool_or(start_date > CURRENT_DATE) AS or_result,
       bool_and(start_date > CURRENT_DATE) AS and_result
from sample_data;       
The above returns:

or_result | and_result
----------+----------
true      | false  
```
