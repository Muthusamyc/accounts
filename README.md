@login_required
def add_new_bookings(request):
    projects = Project.objects.all()
    landdetail = LandDetails.objects.all()
    exectiv = User.objects.filter(role='Executive')
    # bookingamount=Bookings.objects.filter(booking_id = )
    errors = []
    filter_value ={}
    userdetail={}
    usernomieedetail ={}
    mobile_no = request.POST.get('mobile_no')
    if request.method == 'POST':
        mobile_no = request.POST.get('mobile_no')
        action = request.POST.get('action')
        if action == "Filter":
            try:
                filter_value = User.objects.get(mobile_no = mobile_no )
                userdetail = UserDetail.objects.get(user = filter_value.id)
                usernomieedetail = UserNominee.objects.get(user= filter_value.id)
            except User.DoesNotExist:
                messages.error(request, 'Invalid Moblie No')
                filter_value = {} 
        if action == "Submit Application":
            mobile_no = request.POST.get('mobile_no')
            if User.objects.filter(mobile_no = mobile_no):
                user_id = User.objects.get(mobile_no= mobile_no)
                id = user_id.id
                user = User.objects.get(id=id)
                userdetails = UserDetail.objects.get(user=id)
                nominee = UserNominee.objects.get(user=id)
                familydetails = UserFamilyDetails.objects.get(user=id)
            else :
                user = User()
                userdetails = UserDetail()
                nominee = UserNominee()
                familydetails = UserFamilyDetails()
            first_name = request.POST.get('first_name')
            mobile_no = request.POST.get('mobile_no')
            seniority_id = request.POST.get('seniority_id')
            if errors:
                for error in errors:
                    messages.error(request, error)
                return render(request, 'new_bookings/add_new_bookings.html', {'landdetail': landdetail, 'projects': projects})
        try:
            user = user
            user.first_name = first_name
            user.last_name = request.POST.get('last_name')
            user.mobile_no = request.POST.get('mobile_no','').strip()
            user.password = make_password(request.POST.get('password', '').strip())
            user.role = "Customer"
            seniority_id=seniority_id
            user.save()
            details = userdetails
            details.user = user
            details.dob = request.POST.get('dob')
            details.age = request.POST.get('age')
            details.email = request.POST.get('email')
            details.alternate_no = request.POST.get('alternate_no')
            details.aadhhaarno = request.POST.get('aadharno')
            details.aadhar_proof = request.POST.get('aadhar_proof')
            details.panno = request.POST.get('panno')
            details.pan_proof = request.POST.get('pan_proof')
            details.profile = request.POST.get('profile')
            details.address = request.POST.get('address')
            details.city = request.POST.get('city')
            details.state = request.POST.get('state')
            details.pincode = request.POST.get('pincode')
            details.save()

            nominee = nominee
            nominee.user = user
            nominee.nominee_name = request.POST.get('nominee_name')
            nominee.nominee_age = request.POST.get('nominee_age')
            nominee.address = request.POST.get('address1')
            nominee.city = request.POST.get('city1')
            nominee.state = request.POST.get('state1')
            nominee.nominee_relationship = request.POST.get('nominee_relationship')
            nominee.save()

            check_input_no = request.POST.get('check_input_no')
            for val in range(int(check_input_no)):
                member_name_key = f'member_name{val + 1}'
                member_age_key = f'member_age{val + 1}'
                member_relation_key = f'member_relation{val + 1}'

                family = familydetails
                family.user = user
                family.member_name = request.POST.get(member_name_key)
                family.member_age = request.POST.get(member_age_key)
                family.member_relation = request.POST.get(member_relation_key)
                family.save()

            get_last_number = PaymentDetails.objects.all().order_by('-id')[:1]
            if get_last_number:
                auto_generate = "AM-" + str(get_last_number[0].id + 1).zfill(5)
            else:
                auto_generate = "AM-00001"  
            project_id = request.POST.get('projectname')
            dimension_id = request.POST.get('selectDimension')
            land_details = LandDetails.objects.filter(project_id=project_id, plotsize_id=dimension_id).first()

            exective_id = request.POST.get('executive')
            if not exective_id:

                messages.error(request, 'Please select an executive.')
                return render(request, 'new_bookings/add_new_bookings.html', {'landdetail': landdetail, 'exectiv': exectiv, 'projects': projects})
            value = User.objects.get(id=exective_id)
            get_execute = Executive.objects.get(user_id=value.id)
            team_lead_user = get_execute.teamlead.user
        
            # teamlead = User.objects.get(id=teamlead_id)
            project_lead_id = get_execute.teamlead.sr_team.project_head.id
            project_lead = User.objects.get(id=project_lead_id)
        
            book = Bookings()
            book.user = user
            book.mobile_no = mobile_no
            book.membership_id = request.POST.get('member_id')
            book.seniority_id = request.POST.get('seniority_id')
            book.land_details = land_details
            book.total_site_value = request.POST.get('total_site_value')
            book.downpayment = request.POST.get('downpayment')
            book.site_refer = request.POST.get('site_refer')
            book.am_no = auto_generate
            book.executive = value
            book.teamlead = team_lead_user
            book.projhead = project_lead
            book.save()

            split_amount = int(book.total_site_value) / 4

            paid_amount =  request.POST.getlist('amount[]')
            payment_mode = request.POST.getlist('payment_mode[]')
            bank = request.POST.getlist('bank[]')
            branch = request.POST.getlist('branch[]')
            cheque_no = request.POST.getlist('cheque_no[]')
            transaction_id = request.POST.getlist('transaction_id[]')
            ddno=request.POST.getlist('dd_no[]')
            check = request.POST.get('check')
            dateofreceipt = request.POST.getlist('payment_date[]')


            get_number = PaymentDetails.objects.all().order_by('-id')[:1]
            if get_number:
                get_number = "634" + str(get_number[0].id + 1)
            else:
                get_number = "63421"    
            print("len",len(payment_mode))
            if check == 'true':
                membership_fee = PaymentDetails()
                membership_fee.booking = book
                membership_fee.payment_mode = payment_mode[0]
                membership_fee.bank = bank[0]
                membership_fee.branch = branch[0]
                membership_fee.cheque_no = cheque_no[0]
                membership_fee.transaction = transaction_id[0]
                membership_fee.ddno = ddno[0]
                membership_fee.user = user
                membership_fee.dateofreceipt = date.today()
                membership_fee.amount = 2600
                membership_fee.paymentname = "Membership"
                membership_fee.receipt_no = get_number
                membership_fee.save()
                start_index = 1
            else:
                start_index = 0
                print("start_index",start_index)
                for count in range(start_index, len(payment_mode)):
                    payment_amount = int(paid_amount[count]) - 2600
                    membership_fee = PaymentDetails()
                    membership_fee.booking = book
                    membership_fee.payment_mode = payment_mode[count]
                    membership_fee.bank = bank[count]
                    membership_fee.branch = branch[count]
                    membership_fee.cheque_no = cheque_no[count]
                    membership_fee.transaction = transaction_id[count]
                    membership_fee.ddno = ddno[count]
                    membership_fee.user = user
                    membership_fee.dateofreceipt = date.today()
                    membership_fee.amount = 2600
                    membership_fee.paymentname = "Membership"
                    membership_fee.receipt_no = get_number
                    membership_fee.save()
                
            for count in range(start_index, len(payment_mode)):
                if check == 'true':
                    payment_amount = int(paid_amount[count])
                else :
                    payment_amount = int(paid_amount[count])-2600
                print("It Working O cont",count)
                if count <= 1:
                    print("It Working O cont")
                    for i in range(4):
                        if i == 3:
                            status = 7
                            paymentname = 'ThirdInstallment'
                        elif i == 2:
                            status = 5
                            paymentname = 'SecondInstallment'
                        elif i == 1:
                            status = 3
                            paymentname = 'FirstInstallment'
                        else :
                            paymentname = 'DownPayment'
                            status = 1
                        print(paymentname)
                        if split_amount < payment_amount :
                            print("1 Is Working")
                            payments = PaymentDetails()
                            payments.booking = book
                            payments.payment_mode = payment_mode[count]
                            payments.bank = bank[count]
                            payments.branch = branch[count]
                            payments.cheque_no = cheque_no[count]
                            payments.transaction = transaction_id[count]
                            payments.ddno = ddno[count]
                            payments.user = user
                            #payments.payment_data = request.POST.get('payment_data')
                            payments.paymentname = paymentname
                            payments.amount = int(split_amount)
                            payments.receipt_no = get_number
                            payments.dateofreceipt = date.today()
                            payments.save()
                            book.payments_status = status
                            book.total_paid_amount = int(book.total_paid_amount) + int(paid_amount[count])
                            book.save()
                        elif payment_amount > 0 :
                            print("2 Is Working")
                            payments = PaymentDetails()
                            payments.booking = book
                            payments.payment_mode = payment_mode[count]
                            payments.bank = bank[count]
                            payments.branch = branch[count]
                            payments.cheque_no = cheque_no[count]
                            payments.transaction = transaction_id[count]
                            payments.ddno = ddno[count]
                            payments.user = user
                            #payments.payment_data = request.POST.get('payment_data')
                            payments.paymentname = paymentname
                            payments.amount = int(payment_amount) 
                            payments.receipt_no = get_number
                            payments.dateofreceipt = date.today()
                            payments.save()
                            book.payments_status = status
                            book.total_paid_amount = int(book.total_paid_amount) + int(paid_amount[count])
                            book.save()
                            break
                elif count > 1:
                    print("It Working 1 contwq")
                    for i in range(4):
                        amount = int(customers.total_site_value) / 4
                        split_amount = int(amount)
                        customers = Bookings.objects.get(seniority_id=request.POST.get('seniority_id'))
                        payment = PaymentDetails.objects.filter(booking_id=customers.id).aggregate(Sum('amount'))['amount__sum']
                        pay = payment-2600
                        print("customers",customers)
                        print("payment",payment)
                        print("pay",pay)
                        paymentname = ''
                        if i == 0 and pay < split_amount:
                                paymentname = 'DownPayment'
                                status = 1
                        elif i == 1:
                            projectval = int(book.total_site_value) / 2
                            splitamount = int(projectval)
                            if pay <  splitamount:
                                status = 3
                                paymentname = 'FirstInstallment'
                        elif i == 2:
                            pays = splitamount+split_amount
                            if pay < pays:
                                status = 5
                                paymentname = 'SecondInstallment'
                        elif i == 3:
                            if  pay < int(book.total_site_value):
                                    status = 7
                                    paymentname = 'ThirdInstallment'
                                    continue
                            else:
                                messages.error(request,"All Payment is Already Completed.Please Conside with Admin")
                                continue
                        if split_amount <= int(payment_total):
                            payment_total = payment_total - split_amount 
                            paid_amt_bal = split_amount
                        else:
                            paid_amt_bal = (split_amount - payment_total)
                            payment_total = 0
                        if paymentname:
                            if paid_amt_bal >= int(paid_amount[count]):
                                if paid_amt_bal > int(paid_amount[count]):
                                    payment_name = 'Half'
                                else:
                                    payment_name = 'Full'
                                    status += 1
                                payment_amount = int(paid_amount[count])
                            else:
                                payment_amount = paid_amt_bal
                                payment_name = ''
                            payments = PaymentDetails()
                            payments.booking = book
                            payments.payment_mode = payment_mode[count]
                            payments.bank = bank[count]
                            payments.branch = branch[count]
                            payments.cheque_no = cheque_no[count]
                            payments.transaction = transaction_id[count]
                            payments.ddno = ddno[count]
                            payments.dateofreceipt = dateofreceipt
                            payments.paymentname = paymentname+' '+payment_name
                            payments.amount = payment_amount
                            payments.receipt_no = get_number
                            payments.save()
                            book.payments_status = status
                            book.total_paid_amount = int(book.total_paid_amount) + payment_amount
                            book.save()
                            if paid_amt_bal >= int(paid_amount[count]):
                                break
                            else:
                                paid_amount[count] = str(int(paid_amount[count]) - payment_amount)
                        else:
                            continue
                messages.success(request, 'Successfully Saved')
        except Exception as e:
            messages.error(request,'')
    context ={
        'landdetail': landdetail,
        'exectiv':exectiv,
        'projects': projects,
        'book':filter_value,
        'Add_details':userdetail,
        'usernomieedetail':usernomieedetail,
        }
    return render(request, 'new_bookings/add_new_bookings.html', context)
