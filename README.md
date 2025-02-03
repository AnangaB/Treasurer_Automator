## Treasurer Role Automator

This python program was created by me, in order to speed up my tasks as a Treasurer in the SFU Math Student Union. As a treasurer, tasks can get very tedious, as it involves filling out a lot of reimbursement forms for other executives in my union, with essentially similar information each time. To address this, the program automates the process by referencing commonly used data files and generating the required forms efficiently.

### Note: Due to certain issues with pypdf, the filled PDFs may not display correctly in some viewers. In my experience, opening the PDF in Microsoft Edge or Chrome and printing it to PDF resolves the problem.

This program requires 4 things:

- **A CSV file of reimbursement requests**: This file contains the details of each reimbursement, such as the requester, amount, purpose, the meeting minutes the reimbursement was motioned for and whether this reimbursement's forms have been created yet. This file will be constantly changing, as new reimbursement data is created.
- **A CSV file of executive data**: This data is used to fill out specific details in forms. The reimbursement request CSV mentioned above only contains the full name of an individual/executive, and this name is used to fetch the rest of their relevant data from this CSV file.
- **Meeting minutes**: A directory containing meeting minutes in pdf format. Specific meeting minutes here get appended to matching reimbursement form.
- **An output directory**: A folder where the program will generate the completed reimbursement forms.

This program also comes equipped with two forms my school's student society, Simon Fraser Student Society (SFSS) uses, which I got from [here](https://sfss.ca/how-tos-clubs/). These two forms are filled in, based on values in the reimbursement requests csv file, and outputed to the output directory:

- **SFSS Cheque Requistion Form**: This form is filled and in used for eall reimburesement requests.
- **Event & Project Summary Form**: This form is required when a reimbursement request is supposed to be coming from a SFSS grant.

## Folder Structure

The project is typically organized as follows:
```
Treasurer_Automator/
│
├── Reimbursement Data/              # Contains all input data and generated outputs
│   ├── Blank Forms/                 # Directory containing SFSS Cheque Requistion Form and the Event & Project Summary Form
│   ├── Meeting Minutes/             # Directory with meeting minutes pdfs
│   ├── Output/                      # Directory where completed reimbursement forms are saved
│   ├── cheque_req_requests.csv      # CSV file with reimbursement request details. This has to be constantly updated, as new reimbursemnt data comes in.
│   ├── common_info.json             # JSON file with common information used across forms. For eg. all Cheque Requistion Forms require the full name and official position name, of the treasurer. 
│   ├── exec_data.csv                # CSV file with executive data (e.g., names, roles, and contacts)
│
├── .gitignore                       # Specifies files and directories to ignore in version control
├── do_cheque_req.py                 # Main script to run the program to fill out reimbursement forms
├── fill_reimbursement_form.py       # Helper script for processing and filling forms
├── LICENSE                          # Project license information
├── README.md                        # Documentation for the project

```

## Running the program

1. **Clone the Repository**

```
git clone https://github.com/AnangaB/Treasurer_Automator.git
cd Treasurer_Automator
```

2. **Install Required Dependencies.** Ensure you have Python installed, then install any necessary libraries using:
```
pip install -r requirements.txt
```
3. **Run the Script**

Use the following command to execute the main script:

```
python .\do_cheque_req.py './Reimbursement Data/cheque_req_requests.csv' './Reimbursement Data/exec_data.csv' './Reimbursement Data/Meeting Minutes' './Reimbursement Data/Output'
```


Above you can replace the current sample datas (e.g., ./Reimbursement Data/cheque_req_requests.csv) with your own relevant data.

- cheque_req_requests.csv: Delete the current sample dummy data here and update with your own reimbursement request details here. When you are adding a new row for a reimbursement, set it's "Form Created" value to FALSE, so when program runs, it will generate forms for this row.
- exec_data.csv: Update this file with the relevant executive and other people's information, such as names, roles, and contact details, so whenever their full name appears in the cheque_req_requests.csv file, the program can fetch more details about them for the forms.
- Meeting Minutes/: Replace this folder with meeting minutes specific to your society or student union.


4. **Review Outputs.** Completed reimbursement forms will be saved in the output directory, passed in step 3.

- File Naming Convention: Each PDF will be named with the current date in the format YYYY-MM-DD, followed by the type of reimbursement (eg. core or grant).
- Core Reimbursements: All reimbursements originating from the union or club’s core will be appended into a single PDF. Relevant meeting minutes are included after each cheque requisition form in the PDF.
- Grant-Based Reimbursements: Reimbursements involving grants are grouped by grant number. Each group is saved as a separate PDF, with the grant number included in the file name. These PDFs also include an Event Summary Form appended at the end.

### Managing Reimbursements for Multiple Clubs or Societies

To manage reimbursements for multiple clubs or societies, simply create a separate folder for each club following the same structure as the ```Reimbursement Data/``` folder. Then, when running the program in Step 3 above, use the new folder's paths as input parameters.
