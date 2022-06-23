from flask import Flask,render_template,request,redirect,session
from DBConnection import Db
import datetime
import re

import pandas as pd
import numpy as np
import  array as arr

from prediction import *



import matplotlib.pyplot as plt
app = Flask(__name__)
app.secret_key="abc"

def getsimilarity(dictl, dict2) :
    all_words_list= []
    for  key in dictl:
        all_words_list.append(key)
    for key in dict2:
           all_words_list.append(key)
    all_words_list_size = len(all_words_list)

    v1 = np.zeros(all_words_list_size, dtype=np.int)
    v2 = np.zeros(all_words_list_size, dtype=np.int)
    i = 0
    for (key) in all_words_list:
        v1[i] = dictl.get(key, 0)
        v2[i] = dict2.get(key, 0)
        i = i+1
    return cos_sim(v1, v2)
def cos_sim(a, b):
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        return dot_product / (norm_a * norm_b)


@app.route('/login',methods=['get','post'])
def login():

    if request.method=="POST":
        username=request.form['textfield']
        password=request.form['textfield2']
        db=Db()
        ss=db.selectOne("select * from login where user_name='"+username+"' and password='"+password+"'")
        if ss is not None:
            session['log'] = "log"
            if ss['user_type']=='admin':
                return redirect('/admin home')
            elif ss['user_type']=='user':
                session['u_id']=ss['login_id']
                return redirect('/user home')
            else:
                return '''<script> alert('User Not Found');window.location="/"</script>'''
        else:
            return '''<script> alert('User Not Found');window.location="/"</script>'''
    else:
        return render_template("index.html")
@app.route('/')
def home():
    return render_template("mainhome.html")

@app.route('/approve')
def approve():
    if session['log']=='log':
        db = Db()
        ss = db.select("select * from user,login where login.login_id=user.user_id and login.user_type='pending'")
        return render_template("Admin/approve-user.html", data=ss)
    else:
        return redirect('/')

@app.route('/approveuser/<id>')
def approveuser(id):
    if session['log'] == 'log':
        db=Db()
        ss=db.update("update login set user_type='user' where login_id='"+str(id)+"'")
        return '''<script> alert('User Approved');window.location="/approve"</script>'''
    else:
        return redirect('/')

@app.route('/rejectuser/<id>')
def rejectuser(id):
    if session['log'] == 'log':
        db=Db()
        ss=db.delete("delete from  login  where login_id='"+str(id)+"'")
        ss=db.delete("delete from  user  where user_id='"+str(id)+"'")
        return '''<script> alert('User Rejected');window.location="/approve"</script>'''
    else:
        return redirect('/')

@app.route('/view user')
def viewuser():
    if session['log'] == 'log':
        db = Db()
        ss = db.select("select * from user,login where login.login_id=user.user_id and login.user_type='user'")
        return render_template("Admin/view-approved-user.html",data=ss)
    else:
        return redirect('/')
@app.route('/view profile')
def viewprofile():
    if session['log'] == 'log':
        db = Db()
        uid=session['u_id']
        ss = db.selectOne("select * from user where user_id='"+str(uid)+"'")
        return render_template("user/view-profile.html",data=ss)
    else:
        return redirect('/')
@app.route('/register',methods=['get','post'])
def register():
    if request.method == "POST":

        name=request.form['textfield']
        age=request.form['textfield2']
        dob=request.form['textfield3']
        gender=request.form['RadioGroup1']
        email=request.form['textfield4']
        phoneno=request.form['textfield5']
        place=request.form['textfield6']
        post=request.form['textfield7']
        pin=request.form['textfield8']
        occupation=request.form['textfield9']
        religion=request.form['RadioGroup2']
        caste=request.form['textfield10']
        qualification=request.form['textfield11']
        edulevel=request.form['textfield17']
        familystatus=request.form['textfield12']
        height=request.form['textfield13']
        weight=request.form['textfield14']
        complexion=request.form['textfield15']
        bodytype=request.form['textfield16']
        photo=request.files['fileField']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        photo.save(r"C:\Users\user\PycharmProjects\matrimony\static\\"+date+'.jpg')
        photo1="/static/"+date+'.jpg'
        password=request.form['passwordj']
        db=Db()
        ss=db.insert("insert into login VALUES('','"+email+"','"+password+"','pending')")
        print("==========")
        print(ss)
        db.insert("insert into user VALUES('"+str(ss)+"','"+name+"','"+email+"','"+phoneno+"','"+dob+"','"+age+"','"+occupation+"','"+place+"','"+religion+"','"+post+"','"+pin+"','"+qualification+"','"+familystatus+"','"+height+"','"+weight+"','"+complexion+"','"+bodytype+"','"+gender+"','"+photo1+"','"+edulevel+"','"+caste+"')")
        status=request.form['RadioGroup3']
        if(status=='No'):
          return '''<script> alert('User Registered');window.location="/"</script>'''
        else:
            session['u_id']=ss
            return redirect('/preference')
    else:
        return render_template('userregistration.html')
@app.route('/preference',methods=['get','post'])
def preference():
    if request.method == "POST":
        u_id=session['u_id']
        print(u_id)
        agemax=request.form['textfield20']
        agemin=request.form['textfield19']
        education=request.form['textfield21']
        family=request.form['textfield22']
        db=Db()
        ss=db.insert("insert into preference values ('','"+str(u_id)+"','"+family+"','"+education+"','"+agemax+"','"+agemin+"')")
        return "<script>alert('Registration completed!!');window.location='/'</script>"
    else:
        return render_template('user/preferences.html')
@app.route('/view matches')
def viewmatches():
    if session['log'] == 'log':
        db=Db()
        ss=db.selectOne("select age,gender,caste from user where user_id='"+str(session['u_id'])+"'")
        print(ss)
        ss1=db.selectOne("select * from answers where user_id='"+str(session['u_id'])+"'")
        print(ss1)
        if ss1 is None:
            return "<script>alert('Please Take the Personality Test!!');window.location='/test'</script>"
        else:
            db=Db()
            q="select * from preference where u_id='"+str(session['u_id'])+"'"
            print(q)
            res_val=db.selectOne(q)
            l1=["below average","average","above average","high"]
            l2=["SSLC","Higher secondary","graduation","post graduation"]
            if res_val is None:
                if ss['gender']=="Male":
                    query="SELECT * FROM answers WHERE user_id IN(SELECT user_id FROM USER WHERE caste='"+ss['caste']+"' AND gender='Female' AND age<='"+str(ss['age'])+"')"
                    res=db.select(query)
                    md={"ex":ss1['extraversion'],"agr":ss1['agreeableness'],"con":ss1['conscientious'],"neu":ss1['neuroticism'],"ope":ss1['openness']}
                    print(res)
                    print("=================")
                    for i in res:
                        ms={"ex":i['extraversion'],"agr":i['agreeableness'],"con":i['conscientious'],"neu":i['neuroticism'],"ope":i['openness']}
                        print(md,ms)
                        sim=getsimilarity(md,ms)
                        sim=sim*100
                        print(sim)
                        qr="select * from matching where user_id='"+str(session['u_id'])+"' and r_id='"+str(i['user_id'])+"'"
                        res1=db.selectOne(qr)
                        if res1 is  None:
                            db.insert("insert into matching VALUES('','" + str(session['u_id']) + "','" + str(i['user_id']) + "','"+str(sim)+"')")
                    query="SELECT user.*,matching.score FROM USER JOIN matching ON user.user_id=matching.r_id WHERE matching.user_id='"+str(session['u_id'])+"' ORDER BY score DESC"
                    res2=db.select(query)
                    return render_template("user/view-matches.html", data=res2)
                else:
                    query = "SELECT * FROM answers WHERE user_id IN(SELECT user_id FROM USER WHERE caste='" + ss[ 'caste'] + "' AND gender='Male' AND age>='" + str(ss['age']) + "')"
                    res = db.select(query)
                    md = {"ex": ss1['extraversion'], "agr": ss1['agreeableness'], "con": ss1['conscientious'],
                          "neu": ss1['neuroticism'], "ope": ss1['openness']}
                    print(res)
                    print("=================")
                    for i in res:
                        ms = {"ex": i['extraversion'], "agr": i['agreeableness'], "con": i['conscientious'],
                              "neu": i['neuroticism'], "ope": i['openness']}
                        print(md, ms)
                        sim = getsimilarity(md, ms)
                        sim = sim * 100
                        print(sim)
                        qr = "select * from matching where user_id='" + str(session['u_id']) + "' and r_id='" + str(
                            i['user_id']) + "'"
                        res1 = db.selectOne(qr)
                        if res1 is None:
                            db.insert("insert into matching VALUES('','" + str(session['u_id']) + "','" + str(
                                i['user_id']) + "','" + str(sim) + "')")
                    query = "SELECT user.*,matching.score FROM USER JOIN matching ON user.user_id=matching.r_id WHERE matching.user_id='" + str(
                        session['u_id']) + "' ORDER BY score DESC"
                    res2 = db.select(query)
                    return render_template("user/view-matches.html", data=res2)
            else:
                fs=[]
                ind=l1.index(res_val['family_status'])
                for i in range(ind,len(l1)):
                    fs.append("'"+l1[i]+"'")
                ed = []
                ind = l2.index(res_val['education'])
                for i in range(ind, len(l2)):
                    ed.append("'"+l2[i]+"'")
                fs=','.join(fs)
                ed=','.join(ed)
                if ss['gender'] == "Male":
                    query = "SELECT * FROM answers WHERE user_id IN(SELECT user_id FROM USER WHERE caste='" + ss[
                        'caste'] + "' AND gender='Female' AND ( age between  '" + str(res_val['age_min']) + "' and '"+str(res_val['age_max'])+"') and family_status in ("+fs+") and edu_level in ("+ed+"))"
                    print(query)
                    res = db.select(query)
                    print(res)
                    md = {"ex": ss1['extraversion'], "agr": ss1['agreeableness'], "con": ss1['conscientious'],
                          "neu": ss1['neuroticism'], "ope": ss1['openness']}
                    print(res)
                    print("=================")
                    for i in res:
                        ms = {"ex": i['extraversion'], "agr": i['agreeableness'], "con": i['conscientious'],
                              "neu": i['neuroticism'], "ope": i['openness']}
                        print(md, ms)
                        sim = getsimilarity(md, ms)
                        sim = sim * 100
                        print(sim)
                        qr = "select * from matching where user_id='" + str(session['u_id']) + "' and r_id='" + str(
                            i['user_id']) + "'"
                        res1 = db.selectOne(qr)
                        if res1 is None:
                            db.insert("insert into matching VALUES('','" + str(session['u_id']) + "','" + str(
                                i['user_id']) + "','" + str(sim) + "')")
                    query = "SELECT user.*,matching.score FROM USER JOIN matching ON user.user_id=matching.r_id WHERE matching.user_id='" + str(
                        session['u_id']) + "' ORDER BY score DESC"
                    res2 = db.select(query)
                    return render_template("user/view-matches.html", data=res2)
                else:
                    query = "SELECT * FROM answers WHERE user_id IN(SELECT user_id FROM USER WHERE caste='" + ss[
                        'caste'] + "' AND gender='Male' AND ( age between  '" + str(res_val['age_min']) + "' and '"+str(res_val['age_max'])+"') and family_status in ("+fs+") and edu_level in ("+ed+"))"
                    res = db.select(query)
                    md = {"ex": ss1['extraversion'], "agr": ss1['agreeableness'], "con": ss1['conscientious'],
                          "neu": ss1['neuroticism'], "ope": ss1['openness']}
                    print(res)
                    print("=================")
                    for i in res:
                        ms = {"ex": i['extraversion'], "agr": i['agreeableness'], "con": i['conscientious'],
                              "neu": i['neuroticism'], "ope": i['openness']}
                        print(md, ms)
                        sim = getsimilarity(md, ms)
                        sim = sim * 100
                        print(sim)
                        qr = "select * from matching where user_id='" + str(session['u_id']) + "' and r_id='" + str(
                            i['user_id']) + "'"
                        res1 = db.selectOne(qr)
                        if res1 is None:
                            db.insert("insert into matching VALUES('','" + str(session['u_id']) + "','" + str(
                                i['user_id']) + "','" + str(sim) + "')")
                    query = "SELECT user.*,matching.score FROM USER JOIN matching ON user.user_id=matching.r_id WHERE matching.user_id='" + str(
                        session['u_id']) + "' ORDER BY score DESC"
                    res2 = db.select(query)
                    return render_template("user/view-matches.html", data=res2)
    else:
        return redirect('/')
@app.route('/admin home')
def adminhome():
    if session['log']=='log':
        return render_template("admin/home.html")
    else:
        return redirect('/')
@app.route('/user home')
def userhome():
    if session['log'] == 'log':
        return render_template("user/template.html")
    else:
        return redirect('/')

@app.route('/test',methods=['get','post'])
def test():
    if session['log'] == 'log':
        if request.method == "POST":
            q1=request.form['RadioGroup1']
            q2 = request.form['RadioGroup2']
            q3 = request.form['RadioGroup3']
            q4 = request.form['RadioGroup4']
            # q5 = request.form['RadioGroup5']
            q6 = request.form['RadioGroup6']
            q7 = request.form['RadioGroup7']
            q8 = request.form['RadioGroup8']
            q9 = request.form['RadioGroup9']
            # q10 = request.form['RadioGroup10']
            q11 = request.form['RadioGroup11']
            q12 = request.form['RadioGroup12']
            q13 = request.form['RadioGroup13']
            q14 = request.form['RadioGroup14']
            # q15 = request.form['RadioGroup15']
            q16 = request.form['RadioGroup16']
            q17 = request.form['RadioGroup17']
            q18 = request.form['RadioGroup18']
            q19 = request.form['RadioGroup19']
            # q20 = request.form['RadioGroup20']
            q21 = request.form['RadioGroup21']
            q22 = request.form['RadioGroup22']
            q23 = request.form['RadioGroup23']
            q24 = request.form['RadioGroup24']
            # q25 = request.form['RadioGroup25']
            l=[q1,q2,q3,q4,q6,q7,q8,q9,q11,q12,q13,q14,q16,q17,q18,q19,q21,q22,q23,q24,]
            # print(l)
            ex=int(q1)+int(q2)+int(q3)+int(q4)
            agr=int(q6)+int(q7)+int(q8)+int(q9)
            con=int(q11)+int(q12)+int(q13)+int(q14)
            neu=int(q16)+int(q17)+int(q18)+int(q19)
            op=int(q21)+int(q22)+int(q23)+int(q24)

            ex1 = int(ex/2)
            agr1 = int(agr/2)
            con1 = int(con/2)
            neu1 = int(neu/2)
            op1 = int(op/2)
            print("factors:",ex1,agr1,con1,neu1,op1)
            db = Db()

            res=db.selectOne("select * from user where user_id='"+str(session['u_id'])+"'")
            age=res['age']
            gender=res['gender']
            data = {'extraversion': int(ex1), 'agreeableness': int(agr1), 'conscientiousness': int(con1),
                    'neuroticism': int(neu1), 'openness': int(op1)}
            courses = list(data.keys())
            values = list(data.values())

            fig = plt.figure(figsize=(10, 5))

            # creating the bar plot
            plt.bar(courses, values, color='maroon',
                    width=0.4)

            plt.xlabel("Big Five Factors")
            plt.ylabel("Score")
            plt.title("Personality Test Score")
            plt.savefig(r"C:\Users\user\PycharmProjects\matrimony\static/sample.jpg")

            if gender=='Male':


                model = train_model()
                model.train()
                pred = prediction_result(('1', str(age),str(ex1) ,str(agr1),str(con1),str(neu1),str(op1)))
                # print("Hellooo  ")
                # aa = str(pred)
                # print(aa)

                l=str(pred)
                l1 = re.sub('[^A-Za-z]+', '', l)
                # print(l1)
                ss = db.insert("insert into answers VALUES('','"+str(ex)+"','"+str(agr)+"','"+str(con)+"','"+str(neu)+"','"+str(op)+"','"+str(session['u_id'])+"','" +l1+"')")
                return render_template('user/result.html',value=l1)
            else:
                model = train_model()
                model.train()
                pred = prediction_result(('0', str(age), str(ex1), str(agr1), str(con1), str(neu1), str(op1)))
                l = str(pred)
                l1 = re.sub('[^A-Za-z]+', '', l)
                # print(l1)
                # print("Hiiii   ")
                # print(type(pred))

                ss = db.insert(
                    "insert into answers VALUES('','" + str(ex) + "','" + str(agr) + "','" + str(con) + "','" + str(
                        neu) + "','" + str(op) + "','" + str(session['u_id']) + "','"+l1+"')")
                return render_template('user/result.html',value=l1)
        else:
             db=Db()
             ss=db.selectOne("select * from answers where user_id='"+str(session['u_id'])+"'")
             if ss is not None:
                 return "<script>alert('You Already Completed your test!!!');window.location='/user home'</script>"
             return render_template("user/questionnaire.html")
    else:
        return redirect('/')


@app.route('/viewscore')
def viewscore():
    if session['log'] == 'log':
        db=Db()
        ss = db.selectOne("select * from answers where user_id='"+str(session['u_id'])+"'")
        if ss is not None:
            return render_template('user/result.html',value=ss['result'])
        else:
            return "<script>alert('Take the Personality  test!!!');window.location='/test'</script>"
        # ex = ss['extraversion']
        # agr = ss['agreeableness']
        # con = ss['conscientious']
        # neu = ss['neuroticism']
        # op = ss['openness']
        # data = {'extraversion': int(ex), 'agreeableness': int(agr), 'conscientiousness': int(con),
        #         'neuroticism': int(neu),'openness':int(op)}
        # courses = list(data.keys())
        # values = list(data.values())
        #
        # fig = plt.figure(figsize=(10, 5))
        #
        # # creating the bar plot
        # plt.bar(courses, values, color='maroon',
        #         width=0.4)
        #
        # plt.xlabel("Big Five Factors")
        # plt.ylabel("Score")
        # plt.title("Personality Test Score")
        # plt.show()

    else:
       return redirect('/')


@app.route('/logout')
def logout():
    session['log']=""
    return redirect('/')




if __name__ == '__main__':
    app.run()