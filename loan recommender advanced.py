application_name=input("enter Applicant's Name: ")
fuliza_limit=float(input("enter fuliza limit:"))
monthly_salary=int(input("enter monthly salary: "))
CRB_status=str(input("enter your CRB status(listed or not listed): "))
desired_loan_amount=int(input("Enter  desired loan amount"))

if fuliza_limit>10000 and monthly_salary>50000 and CRB_status=="not listed":
    loan_category="platinum"
    max_loan=1000000
    interest_rate=10
    remarks="Excellent borrower"
    interest=(desired_loan_amount*10)/100
    total_repayment=desired_loan_amount+interest

elif 5000<=fuliza_limit<=10000 and monthly_salary>30000 and CRB_status=="not listed":
    loan_category="Gold"
    max_loan=500000
    interest_rate=13
    remarks="Reliable borrower"
    interest=(desired_loan_amount*13)/100
    total_repayment=desired_loan_amount+interest

elif fuliza_limit<5000 and monthly_salary<30000 and CRB_status=="not listed":
    loan_category="Silver"
    max_loan=100000
    interest_rate=15
    remarks="Fair borrower"
    interest=(desired_loan_amount*15)/100
    total_repayment=desired_loan_amount+interest

else :
     fuliza_limit<0 and monthly_salary<0 and CRB_status=="listed"
     loan_category="Not eligible"
     max_loan=0
     interest_rate=0
     remarks="CRB issues detected"
     print("loan denied")
     exit()
print("--LOAN RECOMMENDATION RESULT--")
print("Applicant Name:",application_name)  
print("fuliza limit: ",fuliza_limit)
print("salary: ",monthly_salary)
print("LOAN CATEGORY: ",loan_category)
print("Maximum loan limit:",max_loan)
print("Interest rate:",interest_rate)
print("Loan principal:",desired_loan_amount)
print("Interest:",interest)
print("Total repayment amount",total_repayment)
print("remarks: ",remarks)
