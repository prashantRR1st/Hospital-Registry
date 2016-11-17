#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      student
#
# Created:     15/05/2015
# Copyright:   (c) student 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import pickle
import os
class patient():
    def __init__(self):
        self.name='Null'
        self.age=0
        self.phone=0
        self.pat_code=0
        self.ailm='Null'
        self.spec='Null'
        self.doctor='Null'

    def get(self):
        flag,f=0,0
        self.name=raw_input('Enter Patient Name')
        self.age=input('Enter Patient Age')
        self.phone=input('Enter Patient Phone Number')
        self.pat_code=input('Enter Issued Patient Code')
        self.ailm=raw_input('Enter Ailment/Purpose of Treatment')
        self.spec=raw_input('Enter Specialization Required')
        self.doctor=raw_input('Enter Preferred Doctor')
        ofile=open('doc_data.log','rb')
        try:
            while True:
                d=pickle.load(ofile)
                if self.spec==d.spec1:
                    print '1st if'
                    if self.doctor==d.name1:
                        print '2nd if'
                        if d.curr<d.cons:
                            print '3rd if'
                            print "Your Preffered Doctor is Availible"
                            print "Your Appointment is Confirmed"
                            ofile.close()
                            d.mod(1,d.name1)
                            f=1
                            break
                        else:
                            print 'Your Preferred Doctor is Booked Completely'
                            flag=1
        except EOFError:
            if f==0:
                print 'Your Doctor Under That Specialization does not Exist'
            ofile.close()
        finally:
            ofile.close()
        ''' while True:
                if flag==1 and self.spec==d.spec1:
                    print 'Your Doctor is Unavailible, You May be booked under', d.name1
                    x= raw_input('Should the Appointment be Booked? (yes/no)')
                    if x=='yes':
                        print 'Your Appointment Has Been Booked'
                        d.mod(1)
                        f=1
                        break
                    elif x=='no':
                        print 'Sorry, Please Return Another Day!'
                        break
                    '''



    def disp(self):
        print '________________________________________________________________________________'
        print 'Patient Name:',self.name
        print 'Patient Age:',self.age
        print 'Patient Phone Number:',self.phone
        print 'Patient Code:',self.pat_code
        print 'Ailment/Purpose of Treatment:',self.ailm
        print 'Department Specialization:',self.spec
        print 'Name of Preferred Doctor:',self.doctor
        print '________________________________________________________________________________'
        print

    def wtf(self):
        self.get()
        ofile=open("pat_data.log",'ab')
        pickle.dump(p,ofile)
        print "Patient Data Entered"
        ofile.close()

    def rff(self):
        ifile=open("pat_data.log",'rb')
        count=0
        try:
            while True:
                p=pickle.load(ifile)
                p.disp()
                count+=1
        except EOFError:
            ifile.close()
        finally:
            print "Number of Patients in Registry:",count
            ifile.close()

    def search(self):
        ifile=open("pat_data.log",'rb')
        na=raw_input("Enter Patient Name to be Found")
        try:
            while True:
                p=pickle.load(ifile)
                if na==p.name:
                    p.disp()

        except EOFError:
            ifile.close()
        finally:
            ifile.close()
            print 'Patient Not Found'

    def dele(self):
        ifile=open("pat_data.log",'rb')
        ofile=open("temp",'ab')
        dlt=raw_input("Enter Name of Patient to be Deleted")
        try:
            while True:
                p=pickle.load(ifile)
                if dlt!=p.name:
                    pickle.dump(p,ofile)
        except EOFError:
            ifile.close()
            ofile.close()
            os.remove("pat_data.log")
            os.rename("temp","pat_data.log")

    def mod(self):
        ifile=open("pat_data.log",'rb')
        ofile=open("temp",'ab')
        na=raw_input("enter the name to be modified")
        try:
            while True:
                p=pickle.load(ifile)
                if na!=p.name:
                    pickle.dump(p,ofile)
                else:
                    c=0
                    c1=''
                    ch_mod=0
                    if ch_mod==0:
                        ch_mod= input('Number;Modification: 1;Age,2;Phone,3;Patient Code,4;Purpose of Visit,5;Specialization,6;Preferred Doctor ')
                    while c==0:
                        if ch_mod==1:
                            p.age=input('Enter New Patient Age')
                            c1=raw_input('Continue Modification?(yes/no)')
                            if c1=='no':
                                c=1
                        elif ch_mod==2:
                            p.phone=input('Enter New Patient Phone Number')
                            c1=raw_input('Continue Modification?(yes/no)')
                            if c1=='no':
                                c=1
                        elif ch_mod==3:
                            p.pat_code=input('Enter New Issued Patient Code')
                            c1=raw_input('Continue Modification?(yes/no)')
                            if c1=='no':
                                c=1
                        elif ch_mod==4:
                            p.ailm=raw_input('Enter New Ailment/Purpose of Treatment')
                            c1=raw_input('Continue Modification?(yes/no)')
                            if c1=='no':
                                c=1
                        elif ch_mod==5:
                            p.spec=raw_input('Enter New Specialization Required')
                            c1=raw_input('Continue Modification?(yes/no)')
                            if c1=='no':
                                c=1
                        elif ch_mod==6:
                            p.doctor='Dr.'+raw_input('Enter New Preferred Doctor')
                            c1=raw_input('Continue Modification?(yes/no)')
                            if c1=='no':
                                c=1
                pickle.dump(p,ofile)
        except EOFError:
            ifile.close()
            ofile.close()
        finally:
            ifile.close()
            ofile.close()
            os.remove("pat_data.log")
            os.rename("temp","pat_data.log")
#________________________________________________________________________________________________________________________

class doctor:
    def __init__(self):
        self.name1='Null' #Doctor's Name
        self.room_no=0 #Room No
        self.secretary='Null' #Name of Secretary
        self.phone1=0 #Secretary's Phone Number
        self.spec1='Null' #Specialization
        self.cons=0 #Consultations Taken Per Day
        self.curr=0 #Current Number of Bokkings

    def get(self):
        self.name1=raw_input('Enter Doctor Name')
        self.room_no=input('Room Number')
        self.secretary=raw_input('Enter Name of Secretary')
        self.phone1=input("Enter Secretary's Phone Number")
        self.spec1=raw_input('Enter Doctor Specialization')
        self.cons=input('Enter Number of Consultations Taken Per Day')

    def disp(self):
        print '__________________________________________________________________'
        print 'Doctor Name:',self.name1
        print 'Room Number:',self.room_no
        print 'Secretary Name:',self.secretary
        print 'Secretary Phone Number:',self.phone1
        print 'Specialization:',self.spec1
        print 'Consultation Per Day:',self.cons
        print 'Consultations Booked',self.curr
        print '__________________________________________________________________'
        print

    def wtf(self):
        self.get()
        ofile=open("doc_data.log",'ab')
        pickle.dump(d,ofile)
        print "Doctor Data Entered"
        ofile.close()

    def rff(self,m=0,n=''):
        ifile=open("doc_data.log",'rb')
        cnt=0
        if m==0:
            try:
                while True:
                    d=pickle.load(ifile)
                    d.disp()
                    cnt+=1
            except EOFError:
                ifile.close()
            except IOError:
                print 'The File Does Not Currently Exist'
            finally:
                print "Numbers of Doctors in Registry",cnt
                ifile.close()
        elif m==1:
            try:
                while True:
                    d=pickle.load(ifile)
                    if n==d.spec1:
                        d.disp()
                        cnt+=1
            except EOFError:
                ifile.close()
            finally:
                ifile.close()



    def search(self):
        ifile=open("doc_data.log",'rb')
        na=raw_input("Enter the Name of the Doctor to be Searched")
        try:
            while True:
                d=pickle.load(ifile)
                if na==d.n:
                    d.disp()
        except EOFError:
            ifile.close()
        finally:
            ifile.close()

    def dele(self):
        ifile=open("doc_data.log",'rb')
        ofile=open("temp",'ab')
        na=raw_input("Enter the Doctor's Name to be Deleted")
        try:
            while True:
                d=pickle.load(ifile)
                if na!=d.name1:
                    pickle.dump(d,ofile)
        except EOFError:
            ifile.close()
            ofile.close()
            os.remove("doc_data.log")
            os.rename("temp","doc_data.log")

    def mod(self,pol=0,doc_n=''):
            if pol==0:
                ifile=open("doc_data.log",'rb')
                ofile=open("temp",'ab')
                na=raw_input("Enter the Doctor's Name to be Modified")
                try:
                    while True:
                        d=pickle.load(ifile)
                        if na!=d.name1:
                            pickle.dump(d,ofile)
                        else:
                            c=0
                            c1=''
                            ch_mod= input('Number-Modification: 1-Room Number,2-Secretary Name,3-Secretary Phone Number,4-Specialization,5-Consultation Per Day')
                            while c==0:
                                if ch_mod==1:
                                    d.room_no=input('Enter New Room Number')
                                    c1=raw_input('Continue Modification?(yes/no)')
                                    if c1=='no':
                                        c=1
                                elif ch_mod==2:
                                    d.secretary=input('Enter Name of New Secretary')
                                    c1=raw_input('Continue Modification?(yes/no)')
                                    if c1=='no':
                                        c=1
                                elif ch_mod==3:
                                    d.phone1=input('Enter New Secretary Phone Number')
                                    c1=raw_input('Continue Modification?(yes/no)')
                                    if c1=='no':
                                        c=1
                                elif ch_mod==4:
                                    d.spec1=raw_input('Enter New Area of Specialization')
                                    c1=raw_input('Continue Modification?(yes/no)')
                                    if c1=='no':
                                        c=1
                                elif ch_mod==5:
                                    d.cons=raw_input('Enter New Number of Consultations per Day')
                                    c1=raw_input('Continue Modification?(yes/no)')
                                    if c1=='no':
                                        c=1
                    pickle.dump(p,ofile)
                except EOFError:
                    ifile.close()
                    ofile.close()
                finally:
                    ifile.close()
                    ofile.close()
                    os.remove("doc_data.log")
                    os.rename("temp","doc_data.log")

            elif pol==1:
                ifile=open("doc_data.log",'rb')
                ofile=open("temp",'ab')
                try:
                    while True:
                        d=pickle.load(ifile)
                        if doc_n!=d.name1:
                            pickle.dump(d,ofile)
                        else:
                            d.curr+=1
                            break
                except EOFError:
                    ifile.close()
                    ofile.close()
                finally:
                    ifile.close()
                    ofile.close()
                    os.remove("doc_data.log")
                    os.rename("temp","doc_data.log")



#________________________________________________________________________________________________________________________

Menu1=input('Enter 1 To Access Patient Database and 2 to Access Doctor Database')
if Menu1==1:
    p=patient()
    d=doctor()
    choice='yes'
    spec_req=raw_input("Enter Specialization Required to See Doctors")
    d.rff(1,spec_req)
    while choice=='yes':
        ch=input("Patient Database:Enter 1 to Add Patient,2 to Display Patient Details, 3 to Search for a Patient,4 to Delete Data, 5 to Modify Data")
        if ch==1:
            p.wtf()
        elif ch==2:
            p.rff()
        elif ch==3:
            p.search()
        elif ch==4:
            p.dele()
        elif ch==5:
            p.mod()
        choice=raw_input("Continue in Patient Database?(yes/no)")

elif Menu1==2:
    d=doctor()
    choice='yes'
    while choice=='yes':
        ch=input("Enter Choice:Enter 1 to Add a Doctor,2 to Display Complete Doctor Registry, 3 to Search for a Doctor,4 to Delete a Doctor's Data, 5 to Modify a Doctor's Data")
        if ch==1:
            d.wtf()
        elif ch==2:
            d.rff()
        elif ch==3:
            d.search()
        elif ch==4:
            d.dele()
        elif ch==5:
            d.mod()
        choice=raw_input("Continue in Doctor Database?(yes/no)")
