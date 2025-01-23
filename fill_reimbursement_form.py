from pypdf import PdfWriter, PdfReader

# file path for the blank cheque req
raw_cheque_req_form_path =r'./Reimbursement Data/Blank Forms/raw_cheque_req_form.pdf'



"""Fills a single cheque req form and returns it as a pypdf PageObject
"""
def get_single_filled_req_form(common_info, payee_details,exec_email, page_number):

    #fix the forms first

    form_data = {'Today s Date':(common_info["date_today"]),
                'Group Name' : common_info["group_name"],
                'Cheque Payable To print legibly': payee_details["Requester"],
                'In The Amount Of':str(-1* payee_details["Amount"]),
                'Describe the request andor provide additional information if necessary': str(payee_details["Reason"]), 
                'Requested By': common_info["requested_by"], 
                'Position':common_info["position"],
                'Picked up by':payee_details["Requester"],
                'Email':exec_email
                }

    #create a filled in cheque req form and append to pdf_writer
    reader = PdfReader(raw_cheque_req_form_path)
    writer = PdfWriter()

    writer.append(reader)

    # Get the first page
    page = writer.pages[0]
    
    # Update the fields with the form_data
    writer.update_page_form_field_values(page, form_data, auto_regenerate=False)
   
    return writer.pages[0]
