[comment]: # "Auto-generated SOAR connector documentation"
# Recorded Future Sandbox

Publisher: Recorded Future  
Connector Version: 1\.0\.1  
Product Vendor: Recorded Future  
Product Name: Recorded Future Sandbox  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.3\.4  

App for Recorded Future Sandbox submissions

[comment]: # " File: README.md"
[comment]: # ""
[comment]: # "Copyright (c) 2022 Recorded Future, Inc."
[comment]: # ""
[comment]: # "This unpublished material is proprietary to Recorded Future. All"
[comment]: # "rights reserved. The methods and techniques described herein are"
[comment]: # "considered trade secrets and/or confidential. Reproduction or"
[comment]: # "distribution, in whole or in part, is forbidden except by express"
[comment]: # "written permission of Recorded Future."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
Recorded Future Sandbox allows clients to work smarter, respond faster, and strengthen their
defenses through automation and orchestration. The Recorded Future Sandbox App provides a number of
actions that enable the use of our sandbox solution.

This app requires a correctly set up Recorded Future API Token to use.

## Port Information

The app uses HTTP/ HTTPS protocol for communicating with the Recorded Future server. Below are the
default ports used by Splunk SOAR.

| Service Name | Transport Protocol | Port |
|--------------|--------------------|------|
| http         | tcp                | 80   |
| https        | tcp                | 443  |


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Recorded Future Sandbox asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**server** |  required  | string | Server IP/hostname
**api\_path** |  required  | string | API path
**api\_key** |  required  | password | The API key from the Recorded Future Sandbox account

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[detonate file](#action-detonate-file) - Run the file in the sandbox and retrieve the analysis results  
[fetch report](#action-fetch-report) - Fetch a Recorded Future Sandbox analysis report based on ID value  
[detonate url](#action-detonate-url) - Run a url in the sandbox and retrieve the analysis results  
[get status](#action-get-status) - Get the current status of a Recorded Future Sandbox analysis  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'detonate file'
Run the file in the sandbox and retrieve the analysis results

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**vault\_id** |  required  | Vault ID of file to detonate | string |  `vault id`  `sha1` 
**file\_name** |  required  | Filename to use | string |  `file name` 
**profile\_id** |  optional  | The profile to use \(standard if left empty\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.file\_name | string |  `file name` 
action\_result\.parameter\.profile\_id | string | 
action\_result\.parameter\.vault\_id | string |  `vault id`  `sha1` 
action\_result\.data\.\*\.analysis\_id | string | 
action\_result\.data\.\*\.target | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'fetch report'
Fetch a Recorded Future Sandbox analysis report based on ID value

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**analysis\_id** |  required  | ID given by Recorded Future Sandbox for the analysis to query | string |  `analysis id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.analysis\_id | string |  `analysis id` 
action\_result\.data\.\*\.report\.summary\.completed | string | 
action\_result\.data\.\*\.report\.summary\.created | string | 
action\_result\.data\.\*\.report\.summary\.custom | string | 
action\_result\.data\.\*\.report\.summary\.owner | string | 
action\_result\.data\.\*\.report\.summary\.sample | string | 
action\_result\.data\.\*\.report\.summary\.score | numeric | 
action\_result\.data\.\*\.report\.summary\.sha256 | string | 
action\_result\.data\.\*\.report\.summary\.status | string | 
action\_result\.data\.\*\.report\.summary\.target | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral1\.\*\.tags | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral1\.backend | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral1\.kind | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral1\.platform | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral1\.queue\_id | numeric | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral1\.resource | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral1\.score | numeric | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral1\.status | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral1\.target | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral2\.\*\.tags | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral2\.backend | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral2\.kind | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral2\.platform | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral2\.queue\_id | numeric | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral2\.resource | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral2\.score | numeric | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral2\.status | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.behavioral2\.target | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.static1\.\*\.tags | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.static1\.kind | string | 
action\_result\.data\.\*\.report\.summary\.tasks\.static1\.score | numeric | 
action\_result\.data\.\*\.report\.summary\.tasks\.static1\.status | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.\*\.description | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.\*\.pid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.\*\.procid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.\*\.procid\_target | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.at | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.cmd | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.image | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.kind | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.name | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.name | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.orig | boolean | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.pid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.pid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.ppid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.procid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.procid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.procid\_parent | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.\*\.started | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.\*\.features | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.\*\.tags | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.\*\.ttp | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.backend | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.max\_time\_kernel | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.max\_time\_network | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.platform | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.reported | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.resource | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.score | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.analysis\.submitted | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.\*\.protocols | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.dns\_request\.\*\.domains | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.dns\_request\.\*\.name | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.dns\_request\.\*\.type | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.domain | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.dst | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.first\_seen | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.flow | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.id | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.index | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.last\_seen | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.pid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.procid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.proto | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.rx\_bytes | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.rx\_packets | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.src | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.tx\_bytes | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.network\.\*\.tx\_packets | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.sample\.\*\.static\_tags | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.sample\.id | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.sample\.md5 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.sample\.score | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.sample\.sha1 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.sample\.sha256 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.sample\.sha512 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.sample\.size | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.sample\.submitted | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.sample\.target | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.task\.\*\.static\_tags | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.task\.md5 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.task\.sha1 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.task\.sha256 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.task\.sha512 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.task\.size | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.task\.target | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral1\.version | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.\*\.description | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.\*\.pid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.\*\.procid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.at | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.cmd | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.image | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.kind | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.name | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.name | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.orig | boolean | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.pid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.pid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.ppid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.procid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.procid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.procid\_parent | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.\*\.started | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.\*\.features | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.\*\.tags | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.\*\.ttp | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.backend | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.max\_time\_kernel | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.max\_time\_network | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.platform | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.reported | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.resource | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.score | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.analysis\.submitted | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.\*\.protocols | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.dns\_request\.\*\.domains | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.dns\_request\.\*\.name | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.dns\_request\.\*\.type | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.domain | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.dst | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.first\_seen | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.flow | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.id | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.index | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.last\_seen | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.pid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.procid | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.proto | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.rx\_bytes | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.rx\_packets | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.src | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.tx\_bytes | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.network\.\*\.tx\_packets | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.sample\.\*\.static\_tags | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.sample\.id | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.sample\.md5 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.sample\.score | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.sample\.sha1 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.sample\.sha256 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.sample\.sha512 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.sample\.size | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.sample\.submitted | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.sample\.target | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.task\.\*\.static\_tags | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.task\.md5 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.task\.sha1 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.task\.sha256 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.task\.sha512 | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.task\.size | numeric | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.task\.target | string | 
action\_result\.data\.\*\.report\.tasks\.behavioral2\.version | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'detonate url'
Run a url in the sandbox and retrieve the analysis results

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | URL to use | string |  `file url` 
**kind** |  required  | The kind of URL analysis to run, you can choose between 'url' and 'fetch'\. Url launches the url in the sandbox\. Fetch lets Recorded Future Sandbox download what's located at the URL and submit it as a file | string | 
**profile\_id** |  optional  | The profile to use \(standard if left empty\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.kind | string | 
action\_result\.parameter\.profile\_id | string | 
action\_result\.parameter\.url | string |  `file url` 
action\_result\.data\.\*\.analysis\_id | string | 
action\_result\.data\.\*\.target | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get status'
Get the current status of a Recorded Future Sandbox analysis

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**analysis\_id** |  required  | ID given by Recorded Future Sandbox for the analysis to query | string |  `analysis id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.analysis\_id | string |  `analysis id` 
action\_result\.data\.\*\.analysis\_id | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 