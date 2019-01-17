# DDDthird
import from excel file: new scan range, new intermonth charge, new intercomm charge. Then recalculate 25% risk capital requirement
This is for purpose impact testing

### 
a bit change of plan: 
- create a MAIN / Centralised risk capital script, so that it can be imported into other scripts in the future. 
- therefore, the Main() function inthe Centralised Risk Capital script should have variables from outside as well. 
- define 25% as a variable instead of a fix number
- create log in the Main RC script (later stage)
