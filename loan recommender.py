application_name=input("enter Applicant's Name: ")
fuliza_limit=int(input("enter fuliza limit"))
monthly_salary=int(input("enter monthly salary: "))
CRB_status=str(input("enter your CRB status(listed or not listed): "))
if fuliza_limit>10000:
    if monthly_salary>50000:
            CRB_status="not_listed"
            loan_category="platinum loan"
            max_loan_limit=1000000
            remarks="exellent borrower"
elif 5000<=fuliza_limit<=10000:
            if 30000<=monthly_salary<=50000:
                 CRB_status="not_listed"

                 loan_category="gold loan"
                 max_loan_limit=500000
                 remarks="reliable borrower"
elif fuliza_limit<5000:
         if monthly_salary<30000:
                  CRB_status="not_listed"
                  loan_category="silver loan"
                  max_loan_limit=100000
                  remarks="fair borrower"  
else: 
                    
         if monthly_salary<0:
                CRB_status="listed"
                loan_category="not eligibe"
                max_loan_limit=0
                remarks="CRB issue detected" 

print("LOAN RECOMMENDATION")

print("applicant name: ",application_name)                  
print("fuliza limit: ",fuliza_limit)
print("salary: ",monthly_salary)
print("LOAN CATEGORY: ",loan_category)
print("MAXIMUM LOAN LIMIT: ",max_loan_limit)
print("remarks: ",remarks)

