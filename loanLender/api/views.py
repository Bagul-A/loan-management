from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User, Loan, Transaction
from .serializers import UserSerializer, LoanSerializer, TransactionSerializer

@api_view(['GET'])
def getStatement(request):
    transaction = Transaction.objects.filter(loan_id = request.data.get('loanId'))
    loan = Loan.objects.filter(id = request.data.get('loanId'))
    if loan is None:
        return Response("no loan avaialble")
    
    amountToBePaid = amortization_schedule(loan[0].loan_amount, loan[0].interest_rate, loan[0].term_period)
    serializer = TransactionSerializer(transaction, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    print(request.data)
    name = request.data.get('name')
    email = request.data.get('email')
    annual_income = request.data.get('annual_income')
    user = {'name': name, 'email': email, 'annual_income':annual_income}
    serializer = UserSerializer(data = user)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def applyLoan(request):
    userId = request.data.get('user_id')
    loanType = request.data.get('loan_type')
    loanAmount = request.data.get('loan_amount')
    interstRate = request.data.get('intrest_rate')
    termPeriod = request.data.get('term_period')
    disbursementDate = request.data.get('disbursement_date')
    rate = (interstRate/12)/100
    
    user = User.objects.filter(id = userId)
    if user is None:
        return Response("user does not exist")

    if user[0].annual_income/12 < 150000:
        return Response("monthly income is less than 150000")

    if loanType == "CAR" and loanAmount > 750000:
        return Response("loan limit exceeded for car loan. Limit is 750000")

    if loanType == "HOME" and loanAmount > 8500000:
        return Response("loan limit exceeded for home loan. Limit is 8500000")

    if loanType == "EDUCATIONAL" and loanAmount > 5000000:
        return Response("loan limit exceeded for education loan. Limit is 5000000")
    
    if loanType == "PERSONAL" and loanAmount > 1000000:
        return Response("loan limit exceeded for personal loan. Limit is 1000000")
    
    if interstRate < 14:
        return Response("interest rate less than 14%.")

    
    repaymentAmount = (loanAmount*rate*pow((1+rate),termPeriod))/(pow((1+rate), termPeriod-1))
    loan = {'user_id':userId, 'loan_type':loanType, 'loan_amount':loanAmount, 'repayment_amount':repaymentAmount,
            'intrest_rate':interstRate, 'term_period':termPeriod, 'status': True}
    serializer = LoanSerializer(data=loan)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#was not able to complete sorry
@api_view(['POST'])
def makePayment(request):
    loanId= request.data.get('id')
    amount = request.data.get('amount')
    loan = Loan.objects.filter(id = loanId)
    balance = loan[0].loan_amount

    return Response("hello")



def calculate_amortization_amount(principal, interest_rate, period):
    x = (1 + interest_rate) ** period
    return principal * (interest_rate * x) / (x - 1)

def amortization_schedule(principal, interest_rate, period):
    amortization_amount = calculate_amortization_amount(principal, interest_rate, period)
    number = 1
    balance = principal
    emi = []
    while number <= period:
        interest = balance * interest_rate
        principal = amortization_amount - interest
        emi.append(principal+interest)
        balance = balance - principal
        yield number, amortization_amount, interest, principal, balance if balance > 0 else 0
        number += 1
    return emi


