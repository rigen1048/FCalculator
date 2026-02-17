
""" The structure of this code is very simple.
we use function to validate the input, therfore no malicious input like unexecpted numbers or type cannot be given.
we ask for input with the help of function.
we automate our input handling via class's atttributes inhertience system
depending on the context, we use if condition to guide us further

The code is invalid proof as all the actions are taken from specific interaction
this code is easily mainable by the use of robust functions, classes and if statement
this code is easily scalable in terms of adding new methods for counting but not in robust manner, as it's a calculator
not a tracker
"""


# questions need to be asked before continuing
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Invalid input. Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.\nHint: Don't add any words.")

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Invalid input. Please enter a positive number.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a valid number.\nHint: Don't add any words.")

def get_valid_option(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <=0 or value > 2:
                print("Invalid input. Please choose a number shown above")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.\nHint: Don't add any words.")


# asking for inputs
principle = get_valid_int("What's the loan amount, sir/madam?")

interest = get_valid_float("sir/madam interest amount")

I = float(interest/100) # I is simply formatted interest

years = get_valid_int("duration of the debt for ___Year")

installment = get_valid_option("Sir/Madam, is the loan Given in installment?\n 1 for yes \n 2 for no")

loan_type = get_valid_option("""Choose the loan type from the following sir:
1 for Simple Interest
2 for Compound interest""")



# automating the calculation proccess by class
class Loan:
    """Class for compound interest used"""
    def __init__(self, p, i, m, n):
        self.p = p # principle
        self.i = i # interest
        self.m = m # compounding period
        self.n = n # years

    def total_debt(self):
        """calculates total debt if no payment was made"""
        self.fv = self.p * (1 + self.i / self.m)** (self.m*self.n)
        print(f"total debt:{self.fv}")
        return
    def total_interest(self):
        """calculates total interest if no payment was made"""
        fv_i = self.fv - principle # it's intentional, to calculate installment interest
        print(f"total interest:{fv_i}")
        return
    def year_debt(self):
        """calculates this year debt if no payment was made"""
        self.n =1
        self.total_debt() # to ensure it's recalcualte
        self.fv_ii = self.fv
        print(f"this year total debt:{self.fv_ii}")
        return
    def year_interest(self):
        """ calculates this year interest if no payment was made"""
        fv_iii = self.fv_ii- self.p
        print(f"this year interest:{fv_iii}")
        return

class Simple(Loan):
    """Class for simple interest
    everything with same name does same as parent class, except it's in simple interest"""
    def __init__(self,p,i,n):
        super().__init__(p, i,1, n) #m is irreleveant here
    def total_debt(self):
        self.fv = self.p * (1 + self.i*self.n)
        print(f"total debt:{self.fv}")
        return
    def total_interest(self):
        fv_i = self.fv - self.p
        print(f"total interest:{fv_i}")
        return
    def year_debt(self):
        self.n = 1
        self.total_debt()
        self.fv_ii = self.fv
        print(f"this year debt:{self.fv_ii}")
        return
    def year_interest(self):
        self.n = 1
        fv_iii = self.fv_ii - self.p
        print(f"this year interest:{fv_iii}")
        return

#####3assinging or conencting class
if installment == 2 or loan_type == 1 :
    if loan_type == 1: #simple loan
        usr_loan = Simple(principle, I, years)
    if loan_type == 2:
        # simple interest cannot have multiple compounding period
        compounding_periods = get_valid_float(" number of compound interest apply in year? \n (hint: if it says every 3 months then do 12/3) \n if none such agreement has been made then it means 1 \n")
        usr_loan = Loan(principle, I, compounding_periods, years)

    if years > 1: # those result are unnessary if input year = 1
        usr_loan.total_debt()
        usr_loan.total_interest()
    usr_loan.year_debt()
    usr_loan.year_interest()

elif installment == 1:
    # getting all the value prepared
    inst_numbers = get_valid_int("sir/madam, number of installment?")
    compounding_periods = get_valid_float(" number of compound interest apply in year? \n (hint: if it says every 3 months then do 12/3)")
    p_inis = float(principle / inst_numbers)

    x = int(12 / inst_numbers)
    c = int(12 / compounding_periods)
    dmonth = [q for q in range(0, 12, x)] # means month of installment debt, by assuming the first installment is given on 0 month
    cmonth = [q for q in range(c, 13, c)] # every c months compound interest applies

    installment_m = [] # this creates a list of m per installment by comparing the month of debt and month of ccompound
    for m_num in dmonth:
        installment_m.append(sum([1 for q in cmonth if dmonth < cmonth]))

    # time to calculate the debt
    amounts = [p_inis * (1 + I / m) ** m for m in installment_m] #here the n should be 1 therefore not written
    finalized_debt = sum(amounts)
    # let calculate the interest
    finalized_interest = finalized_debt - principle

    print(f"this year debt:{finalized_debt}")
    print(f"this year interest:{finalized_interest}")
    if years > 1: #those result are unnessary if input year = 1
        inis_year = years - 1
        usr_loan = Loan(finalized_debt,I,compounding_periods,inis_year)
        usr_loan.total_debt()
        usr_loan.total_interest()
