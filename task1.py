def register():
  username=input('Please Enter Username or EmailID: ')
  for i in range(0,len(username)):
    if ((i==0 and username[i]=='@')or(username[i]=='@' and username[i+1]=='.')or(i==0 and username[i].isdigit())or(i==0 and (username[i]=='&' or username[i]=='!' or username[i]=='%' or username[i]=='#'))):
      print('Invalid Username Please Enter Valid Username')
      register()
  password=input('Enter Password: ')
  digit=0
  special_char=0
  small_letters=0
  capital_letters=0
  for i in range(0,len(password)):
    if(password[i]=='!' or password[i]=='%' or password[i]=='#' or password[i]=='&' or password[i]=='@' ):
      special_char+=1
    if(password[i].isupper()):
      capital_letters+=1
    if(password[i].islower()):
      small_letters+=1
    if(password[i].isdigit()):
      digit+=1
  if((len(password)>5 and len(password)<16) and special_char>=1 and digit>=1 and small_letters>=1 and capital_letters>=1):
    print('Registered Successfully!!!!')
    db=open("login.txt", "a")
    data=username+','+password
    db.write(data)
    db.write('\n')
    db.close()
    db=open("login.txt", "r")
    print(db.read())
    
  else:
    print('Password is not matching Kindly Register Again')
    register()
    
    
ss='false'
i=input('Welcome to our Shop.\n If you are a new USER enter y to register else n: ')
if i=='y':
  register()
if i=='n':
  i=input('Would you like to login? enter y or n?: ')
  if i=='n':
    print('No Action is Taken')
  if i=='y':
    user_name=input('Please Enter Username/EmailID: ')
    pass_word=input('Please Enter the Password: ')
    db=open("login.txt", "r")
  
    for s in db:
      a,b=s.split(",")
      b=b.strip()
      if(user_name==a and pass_word==b):
        print('Login Successfull!!!')
        ss='true'
        exit()
      if(user_name==a and pass_word!=b):
        print('Your Password is Wrong.')
        l=input('Would you like to click Forgot Password. enter y/n')
        if l=='y':
          print('Your Password is ',b)
          ss='true'
          break
        else:
          print('No Forgot Password is requested')
          ss='true'
          break
    if(ss=='false'):
      print('Your Credentials is not found. Kindly Register')
