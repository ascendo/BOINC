### Notes before use

* Designed for large job batch submission
* Requires a token
* Test token before submitting tasks
* Server will not notify if the tasks have failed immediately
* For a job file submission, use the following curl method:  
	*curl -F file=@Example_multi_submit.txt http://SERVER_IP:5075/boincserver/v2/submit_known/token=TOKEN*  

----

### Reef Storage


* Designed to save files for future BOINC jobs, so that they may be called through wget or curl  
* Each individual user will receive a unique, personal sandbox assigned to their token  
* Users must create a directory before using it, use the following syntax:  
	*curl -d token=TOKEN  http://SERVER_IP:5060/boincserver/v2/create_sandbox*  
* Users may not have more than one directory
* Check all user files using the following syntax (files will be comma-separated):  
	*curl http://SERVER_IP:5060/boincserver/v2/all_files/token=TOKEN*
* Upload a file using the syntax:  
	*curl -F file=@FILE.txt http://SERVER_IP:5060/boincserver/v2/upload_reef/token=TOKEN*
* Delete a file using the syntax:
	*curl -d del=FILE_NAME  http://SERVER_IP:5060/boincserver/v2/delete_file/token=TOKEN*
* Download a file using curl/wget with the syntax:  
	*curl http://SERVER_IP:5060/boincserver/v2/reef/TOKEN/FILE_NAME*
* Get user allocation and space used with:
	*curl http://SERVER_IP:5060/boincserver/v2/reef_allocation_status/token=TOKEN*



**Summary**  
Using Reef, it is now possible to:  
	- Upload files to the cloud, favoring integration with local file systems  
	- Delete files when they are no longer useful
	- Maintain a sandbox of data for future BOINC projects
	- Download files using curl or wget
	- Check used disk space allocation, as of now, all user's are assigned 2 GB of space

----

### Two-Factor Token authorization  
Tokens can be assigned in 2 different ways:
1. Contact the server administrator and request a token
2. Apply from within an authorized organization  

If your organization wants to access the BOINC server and provide jobs for the volunteers, contact the server administrator and ask for an administrative organization account. If your request is approved, your organization will beprovided with a company token that individual researchers will use to apply for BOINC submission privileges.  
Note: The organization token cannot be used to submit jobs.  

Request a token via your organization is a 2 step process:
1. Submit a request using your organization's credentials; in some cases, your organization may provide a script that communicates to the API. Nonetheless, if you must do it alone, use the following syntax:
	*curl -F name=NAME -F last_name=LAST_NAME -F email=EMAIL  http://SERVER_IP:5054/boincserver/v2/api/request_user_token/ORG_TOKEN*
The server will then send an automated email with a temporary token, needed to request an actual token. Temporary tokens are valid for 24 hours.
Note: The name and emails provided do not necessarily have to be the same as the user's email. This allows for the organization details to be shared only to those deemed necessary. User must provide their actual name and email address on the second step of the process.  

2. Once you have received the token in a personal email account, follow the instructions in your company's script to receive a permanent token. You will be prompted to enter your name, last name, and email again. However, this time, your email address must be yours since that is where the results will be sent. You will be also asked about an allocation, with the maximum being your company's allocation.
If you must check your company's allocation, use the following syntax (returns company's max. allocation in GB):  
	*curl http://SERVER_IP:5054/boincserver/v2/api/check_company_allocation/ORG_TOKEN*
To add a user manually with the temporary token, do:
	*curl -F name=NAME -F last_name=LAST_NAME -F email=EMAIL -F allocation=ALLOCATION* http://SERVER_IP:5054/boincserver/v2/api/*authenticated_request_token/ORG_TOKEN/TEMPORARY_TOKEN*

-------

### MIDAS processing

MIDAS (Multiple Input Docker Automation System) is a TACC tool designed for automatic dockerization.  
For more information on MIDAS, consult the *processing_files* files directory, it contains example and a README guide.  
Use the following syntax to upload a file:  
	*curl -F file=@FILE http://SERVER_IP:5085/boincserver/v2/midas/token=TOKEN*

Users are each assigned an allocation and allowed to submit images and jobs as long as these allocation is not exceeded.  
To check the user's images, as well as their size, do:
	*curl http://SERVER_IP:5085/boincserver/v2/midas/user_images/token=TOKEN*

To delete an image, provide its name and tag (N:T), the name is the same as the user's token, or just the tag, using the syntax:  
	*curl -F del=TAG http://SERVER_IP:5085/boincserver/v2/midas/user_images/token=TOKEN*