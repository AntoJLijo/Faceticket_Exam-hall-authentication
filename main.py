from flask import Flask, render_template, flash, request,session
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import mysql.connector
import tkinter as tk
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time
#from __future__ import print_function
from flask import Flask, render_template, flash, request,session
import sys, fsdk, math, ctypes, time
from fsdk import FSDK
import mysql.connector
import datetime
import time
import numpy as np
import cv2 as cv
import yagmail


#from __future__ import print_function
import sys, fsdk, math, ctypes, time
from fsdk import FSDK
import mysql.connector
import datetime
import time

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')
@app.route("/addexam")
def addexam():
    return render_template('addexam.html')
@app.route("/addhall")
def addhall():
    return render_template('addhall.html')
@app.route("/addstud")
def addstud():
    return render_template('addstud.html')
@app.route("/addstaff")
def addstff():
    return render_template('addstaff.html')
@app.route("/adminhome")
def adminhome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
    cursor = conn.cursor()
    cursor.execute("select * from register")
    data = cursor.fetchall()

    return render_template('adminhome.html', data=data)

@app.route("/view")
def view():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
    cursor = conn.cursor()
    cursor.execute("select * from staffregister")
    data = cursor.fetchall()

    return render_template('view.html',data=data)

@app.route("/staff")
def staff():

    return render_template('staff.html')
@app.route("/student")
def student():

    return render_template('student.html')

@app.route("/adminlog",methods=['GET','POST'])
def adminlog():
    if request.method == 'POST':
        uname=request.form['uname']
        password=request.form['password']
        print(uname)
        print(password)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
        cursor = conn.cursor()
        cursor.execute("select * from admin where uname='"+uname+"' and password='"+password+"'")
        data=cursor.fetchone()
        if data is None:
            return "user name and password incorrect"
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
            cursor = conn.cursor()
            cursor.execute("select * from register")
            data = cursor.fetchall()

            return render_template('adminhome.html', data=data)
            #return render_template("adminhome.html")
@app.route("/addexam1",methods=['GET','POST'])
def addexam1():
    if request.method == 'POST':
        etype=request.form['etype']
        depart=request.form['depart']
        year=request.form['year']
        subject = request.form['subject']
        date = request.form['date']
        sess = request.form['sess']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
        cursor = conn.cursor()
        cursor.execute(
            "insert into exam values('','" + etype + "','" + depart + "','" + year + "','" + subject + "','" + date + "','" + sess + "')")
        conn.commit()
        conn.close()
        return render_template("addexam.html")


@app.route("/addhall1",methods=['GET','POST'])
def addhall1():
    if request.method == 'POST':
        etype=request.form['etype']
        regno=request.form['regno']
        hno=request.form['hall']
        subject = request.form['subject']
        date = request.form['date']
        sess = request.form['sess']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
        cursor = conn.cursor()
        cursor.execute(
            "insert into hall1 values('','" + etype + "','" + regno + "','" + hno + "','" + subject + "','" + date + "','" + sess + "')")
        conn.commit()
        conn.close()
        return render_template("Addhall.html")
@app.route("/addquestions",methods=['GET','POST'])
def addquestions():
    if request.method == 'POST':
        exam=request.form['exam']
        depart=request.form['depart']
        year=request.form['year']
        subject = request.form['subject']
        question = request.form['question']
        ans1 = request.form['ans1']
        ans2 = request.form['ans2']
        ans3 = request.form['ans3']
        ans4 = request.form['ans4']
        ans = request.form['anstrue']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
        cursor = conn.cursor()
        cursor.execute(
            "insert into questions values('','" + year + "','"+depart+"','" + exam + "','" + subject + "','" + question + "','" + ans1 + "','" + ans2 + "','" + ans3 + "','" + ans4 + "','" + ans + "')")
        conn.commit()
        conn.close()
        return render_template("adminhome.html")


@app.route("/studentregister",methods=['GET','POST'])
def studentregister():
    if request.method == 'POST':
        studentid=request.form['regno']
        name=request.form['name']
        gender=request.form['gender']
        dob = request.form['dob']
        depart = request.form['depart']
        year = request.form['year']
        sem = request.form['sem']
        class1 = request.form['class']
        address = request.form['address']
        email = request.form['email']
        pnumber = request.form['pnumber']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
        cursor = conn.cursor()
        cursor.execute(
            "insert into register values('','" + studentid + "','"+name+"','" + gender + "','" + dob + "','" + depart + "','" + year + "','" + email + "','" + pnumber + "','" + address + "','"+sem+"','"+class1+"')")
        conn.commit()
        conn.close()
        import LiveRecognition

        return render_template("addstud1.html")

@app.route("/staffregister",methods=['GET','POST'])
def staffregister():
    if request.method == 'POST':
        staffid=request.form['regno']
        name=request.form['name']
        gender=request.form['gender']
        dob = request.form['dob']
        depart = request.form['depart']
        year = request.form['year']
        sem = request.form['sem']
        class1 = request.form['class']
        address = request.form['address']
        email = request.form['email']
        pnumber = request.form['pnumber']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
        cursor = conn.cursor()
        cursor.execute(
            "insert into staffregister values('','" + staffid + "','"+name+"','" + gender + "','" + dob + "','" + depart + "','" + year + "','" + email + "','" + pnumber + "','" + address + "','"+sem+"','"+class1+"')")
        conn.commit()
        conn.close()
        return render_template("addstud1.html")

@app.route("/studentlogin",methods=['GET','POST'])
def studentlogin():
    if request.method == 'POST':
        uname=request.form['uname']
        password=request.form['password']
        session['sid']=password
        print(uname)
        print(password)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
        cursor = conn.cursor()
        cursor.execute("select * from register where name='"+uname+"' and studentid='"+password+"'")
        data=cursor.fetchone()
        print(data)
        if data is None:
            return "user name and password incorrect"
        else:
            session['uid'] = data[0]
            return render_template("student1.html",data=data)
@app.route("/studentlogin1",methods=['GET','POST'])
def studentlogin1():
    if request.method == 'POST':
        sid=session['sid']
        var=''





        def examvales():
            global ExamName1
            global SubjectName1
            global Date1
            global Degree1
            global Department1
            global Year1

        # ExamName1 = ExamName
        # SubjectName1 = SubjectName
        # Date1 = Date
        # Degree1 = Degree
        # Department1 = Department
        # Year1 = Year11

        # print(ExamName1)
        # print(SubjectName1)
        # print(Date1)
        # print(Degree1)
        # print(Department1)
        # print(Year1)

        license_key = "fVrFCzYC5wOtEVspKM/zfLWVcSIZA4RNqx74s+QngdvRiCC7z7MHlSf2w3+OUyAZkTFeD4kSpfVPcRVIqAKWUZzJG975b/P4HNNzpl11edXGIyGrTO/DImoZksDSRs6wktvgr8lnNCB5IukIPV5j/jBKlgL5aqiwSfyCR8UdC9s="

        if not fsdk.windows:
            print('The program is for Microsoft Windows.');
            exit(1)
        import win

        trackerMemoryFile = "tracker70.dat"

        FONT_SIZE = 30

        print("Initializing FSDK... ", end='')
        FSDK.ActivateLibrary(license_key);
        FSDK.Initialize()
        print("OK\nLicense info:", FSDK.GetLicenseInfo())

        FSDK.InitializeCapturing()
        print('Looking for video cameras... ', end='')
        camList = FSDK.ListCameraNames()

        if not camList: print("Please attach a camera.");
        print(camList[0])  # camList[0].devicePath

        camera = camList[0]  # choose the first camera (0)
        print("using '%s'" % camera)
        formatList = FSDK.ListVideoFormats(camera)
        # print(*zip(range(len(formatList)), formatList), sep='\n')
        print(*formatList[0:5], sep='\n')
        if len(formatList) > 5: print('...', len(formatList) - 5, 'more formats (skipped)...')

        vfmt = formatList[0]  # choose the first format: vfmt.Width, vfmt.Height, vfmt.BPP
        print('Selected camera format:', vfmt)
        FSDK.SetVideoFormat(camera, vfmt)

        print("Trying to open '%s'... " % camera, end='')
        camera = FSDK.OpenVideoCamera(camera)
        print("OK", camera.handle)

        try:
            fsdkTracker = FSDK.Tracker.FromFile(trackerMemoryFile)
        except:
            fsdkTracker = FSDK.Tracker()  # creating a FSDK Tracker

        fsdkTracker.SetParameters(  # set realtime face detection parameters
            RecognizeFaces=True, DetectFacialFeatures=True,
            HandleArbitraryRotations=True, DetermineFaceRotationAngle=False,
            InternalResizeWidth=256, FaceDetectionThreshold=5
        )

        need_to_exit = False

        def WndProc(hWnd, message, wParam, lParam):
            global capturedFace
            if message == win.WM_CTLCOLOREDIT:
                fsdkTracker.SetName(capturedFace, win.GetWindowText(inpBox))
            if message == win.WM_DESTROY:
                global need_to_exit
                need_to_exit = True
            else:
                if message == win.WM_MOUSEMOVE:
                    updateActiveFace()
                    return 1
                if message == win.WM_LBUTTONDOWN:
                    if activeFace and capturedFace != activeFace:
                        capturedFace = activeFace
                        win.SetWindowText(inpBox, fsdkTracker.GetName(capturedFace))
                        win.ShowWindow(inpBox, win.SW_SHOW)
                        win.SetFocus(inpBox)
                    else:
                        capturedFace = None
                        win.ShowWindow(inpBox, win.SW_HIDE)
                    return 1
            return win.DefWindowProc(hWnd, message, win.WPARAM(wParam), win.LPARAM(lParam))

        wcex = win.WNDCLASSEX(cbSize=ctypes.sizeof(win.WNDCLASSEX), style=0, lpfnWndProc=win.WNDPROC(WndProc),
                              cbClsExtra=0, cbWndExtra=0, hInstance=0, hIcon=0,
                              hCursor=win.LoadCursor(0, win.IDC_ARROW), hbrBackground=0,
                              lpszMenuName=0, lpszClassName=win.L("My Window Class"), hIconSm=0)
        win.RegisterClassEx(wcex)

        hwnd = win.CreateWindowEx(win.WS_EX_CLIENTEDGE, win.L("My Window Class"), win.L("Live Recognition"),
                                  win.WS_SYSMENU | win.WS_CAPTION | win.WS_CLIPCHILDREN,
                                  100, 100, vfmt.Width, vfmt.Height, *[0] * 4)
        win.ShowWindow(hwnd, win.SW_SHOW)

        # textBox = win.CreateWindow(win.L("STATIC"), win.L("Click face to name it"), win.SS_CENTER | win.WS_CHILD, 0, 0, 0, 0, hwnd, 0, 0, 0)
        # myFont = win.CreateFont(30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, win.L("Microsoft Sans Serif"))
        # win.SendMessage(textBox, win.WM_SETFONT, myFont, True);
        # win.SetWindowPos(textBox, 0, 0, vfmt.Height, vfmt.Width, 80, win.SWP_NOZORDER)
        # win.ShowWindow(textBox, win.SW_SHOW)

        inpBox = win.CreateWindow(win.L("EDIT"), win.L(""), win.SS_CENTER | win.WS_CHILD, 0, 0, 0, 0, hwnd, 0, 0, 0)
        myFont = win.CreateFont(30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, win.L("Microsoft Sans Serif"))
        win.SendMessage(inpBox, win.WM_SETFONT, myFont, True);
        win.SetWindowPos(inpBox, 0, 0, vfmt.Height - 80, vfmt.Width, 80, win.SWP_NOZORDER)
        win.UpdateWindow(hwnd)

        def dot_center(dots):  # calc geometric center of dots
            return sum(p.x for p in dots) / len(dots), sum(p.y for p in dots) / len(dots)

        class LowPassFilter:  # low pass filter to stabilize frame size
            def __init__(self, a=0.35): self.a, self.y = a, None

            def __call__(self, x): self.y = self.a * x + (1 - self.a) * (self.y or x); return self.y

        class FaceLocator:
            def __init__(self, fid):
                self.lpf = None
                self.center = self.angle = self.frame = None
                self.fid = fid

            def isIntersect(self, state):
                (x1, y1, x2, y2), (xx1, yy1, xx2, yy2) = self.frame, state.frame
                return not (x1 >= xx2 or x2 < xx1 or y1 >= yy2 or y2 < yy1)

            def isActive(self):
                return self.lpf is not None

            def is_inside(self, x, y):
                x -= self.center[0];
                y -= self.center[1]
                a = self.angle * math.pi / 180
                x, y = x * math.cos(a) + y * math.sin(a), x * math.sin(a) - y * math.cos(a)
                return (x / self.frame[0]) ** 2 + (y / self.frame[1]) ** 2 <= 1

            def draw_shape(self, surf):
                container = surf.beginContainer()
                surf.translateTransform(*self.center).rotateTransform(self.angle).ellipse(facePen,
                                                                                          *self.frame)  # draw frame
                if activeFace == self.fid:
                    surf.ellipse(faceActivePen, *self.frame)  # draw active frame
                if capturedFace == self.fid:
                    surf.ellipse(faceCapturedPen, *self.frame)  # draw captured frame
                surf.endContainer(container)

            def draw(self, surf, path, face_id=None):
                if face_id is not None:
                    ff = fsdkTracker.GetFacialFeatures(0, face_id)
                    if self.lpf is None: self.lpf = LowPassFilter()
                    xl, yl = dot_center([ff[k] for k in FSDK.FSDKP_LEFT_EYE_SET])
                    xr, yr = dot_center([ff[k] for k in FSDK.FSDKP_RIGHT_EYE_SET])
                    w = self.lpf((xr - xl) * 2.8)
                    h = w * 1.4
                    self.center = (xr + xl) / 2, (yr + yl) / 2 + w * 0.05
                    self.angle = math.atan2(yr - yl, xr - xl) * 180 / math.pi
                    self.frame = -w / 2, -h / 2, w / 2, h / 2

                    self.draw_shape(surf)

                    name = fsdkTracker.GetName(self.fid)
                    # print(name)
                    surf.drawString(name, font, self.center[0] - w / 2 + 2, self.center[1] - h / 2 + 2, text_shadow)
                    surf.drawString(name, font, self.center[0] - w / 2, self.center[1] - h / 2, text_color)
                else:
                    if self.lpf is not None: self.lpf, self.countdown = None, 35
                    self.countdown -= 1
                    if self.countdown <= 8:
                        self.frame = [v * 0.95 for v in self.frame]
                    else:
                        self.draw_shape(surf)
                    name = 'Unkown User!';
                # print(name)

                path.ellipse(*self.frame)  # frame background
                return self.lpf or self.countdown > 0

        activeFace = capturedFace = None

        def updateActiveFace():
            global activeFace
            p = win.ScreenToClient(hwnd, win.GetCursorPos())
            for fid, tr in trackers.items():
                if tr.is_inside(p.x, p.y):
                    activeFace = fid
                    break
            else:
                activeFace = None

        gdiplus = win.GDIPlus()  # initialize GDI+
        graphics = win.Graphics(hwnd=hwnd)
        backsurf = win.Bitmap.FromGraphics(vfmt.Width, vfmt.Height, graphics)
        surfGr = win.Graphics(bmp=backsurf).setSmoothing(True)  # graphics object for back surface with antialiasing
        facePen, featurePen, brush = win.Pen(0x60ffffff, 5), win.Pen(0xa060ff60, 1.8), win.Brush(0x28ffffff)
        faceActivePen, faceCapturedPen = win.Pen(0xFF00ff00, 2), win.Pen(0xFFff0000, 3)
        font = win.Font(win.FontFamily("Tahoma"), FONT_SIZE)
        text_color, text_shadow = win.Brush(0xffffffff), win.Brush(0xff808080)

        trackers = {}
        # def att():
        # pass
        mylist = []
        sampleNum = 0
        while 1:
            sampleNum = sampleNum + 1
            img = camera.GrabFrame()
            surfGr.resetClip().drawImage(win.Bitmap.FromHBITMAP(img.GetHBitmap()))  # fill backsurface with image

            faces = frozenset(fsdkTracker.FeedFrame(0, img))  # recognize all faces in the image
            for face_id in faces.difference(trackers): trackers[face_id] = FaceLocator(face_id)  # create new trackers

            missed, gpath = [], win.GraphicsPath()
            for face_id, tracker in trackers.items():  # iterate over current trackers
                ss = fsdkTracker.GetName(face_id)
                mylist.append(ss)
                print(mylist)
                mylist = list(dict.fromkeys(mylist))
                print("################################################")
                print(mylist)
                for i in range(0, len(mylist)):
                    print(mylist[i])
                if sampleNum > 100:
                    # ExamName1,SubjectName1,Date1,Degree1,Department1,Year1=fs.examvales1()

                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

                    conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
                    cursor = conn.cursor()
                    cursor.execute("select * from register where studentid='" + str(ss) + "'")
                    data = cursor.fetchone()
                    if data is None:
                        '''session['n1'] = "Unkown User!"'''
                        # print("Unkown User!")
                        print(2)
                        var = '2'
                        '''c = var.encode()
                        print(c)
                        arduino.write(c)
                        # ard.write(c)
                        time.sleep(4)'''


                    else:
                        '''session['n1'] = 'Already Face Info Saved'''

                        # print("Already Face Info Saved")

                        var = '1'
                        '''c = var.encode()
                        print(c)
                        arduino.write(c)
                        # ard.write(c)
                        time.sleep(4)'''

                if face_id in faces:
                    tracker.draw(surfGr, gpath,
                                 face_id)  # fsdkTracker.GetFacialFeatures(face_id)) # draw existing tracker
                else:
                    missed.append(face_id)
            for mt in missed:  # find and remove trackers that are not active anymore
                st = trackers[mt]
                if any(st.isIntersect(trackers[tr]) for tr in faces) or not st.draw(surfGr, gpath): del trackers[mt]

            if capturedFace not in trackers:
                capturedFace = None
                win.ShowWindow(inpBox, win.SW_HIDE)
            updateActiveFace()

            # surfGr.clipPath(gpath, win.CombineModeExclude).fillRect(brush, 0, 0, vfmt.Width, vfmt.Height) # clip frames
            graphics.drawImage(backsurf, 0, 0)  # show backsurface
            if sampleNum > 100:
                break

            msg = win.MSG()
            if win.PeekMessage(win.byref(msg), 0, 0, 0, win.PM_REMOVE):
                win.TranslateMessage(win.byref(msg))
                win.DispatchMessage(win.byref(msg))
                if msg.message == win.WM_KEYDOWN and msg.wParam == win.VK_ESCAPE or need_to_exit: break

        print("Please wait while saving Tracker memory... ", end='', flush=True)
        fsdkTracker.SaveToFile(trackerMemoryFile)
        win.ShowWindow(hwnd, win.SW_HIDE)

        img.Free()
        fsdkTracker.Free()
        camera.Close()

        FSDK.FinalizeCapturing()

        FSDK.Finalize()
        if var=='1':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
            cursor1 = conn.cursor()
            cursor1.execute("select * from hall1 where regno='" + str(sid) + "'")
            data2 = cursor1.fetchall()
            print(data2)
            return render_template("studenthome.html", data=data2)
        else:
            return "unkown user"











@app.route("/view1")
def view1():


         #categories=request.form['id']
         id=request.args.get('id')
         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
         cursor = conn.cursor()
         cursor.execute("select * from exam where etype='"+id+"'")
         data = cursor.fetchall()
         print(data)
         return render_template("subject.html", data=data)
@app.route("/studenthome")
def studenthome():


         #categories=request.form['id']

         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
         cursor1 = conn.cursor()
         cursor1.execute("select DISTINCT etype from exam")
         data2 = cursor1.fetchall()
         print(data2)

         return render_template("studenthome.html", data=data2)

@app.route("/view2")
def view2():


         #categories=request.form['id']
         id=request.args.get('id')
         id1 = request.args.get('id1')
         session['sname'] = id
         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
         cursor = conn.cursor()
         cursor.execute("select * from questions where exam='"+id1+"' and subject='"+id+"'")
         data = cursor.fetchall()
         print(data)
         return render_template("ans.html", data=data)

@app.route("/slive",methods=['GET','POST'])
def slive():
    sid=session['sid']
    count = 0
    status = ''
    la=''
    mylist = []

    import time
    import argparse

    import cv2
    import numpy as np
    import mediapipe as mp

    from Utils import get_face_area
    from Eye_Dector_Module import EyeDetector as EyeDet
    from Pose_Estimation_Module import HeadPoseEstimator as HeadPoseEst
    from Attention_Scorer_Module import AttentionScorer as AttScorer

    # camera matrix obtained from the camera calibration script, using a 9x6 chessboard
    camera_matrix = np.array(
        [[899.12150372, 0., 644.26261492],
         [0., 899.45280671, 372.28009436],
         [0, 0, 1]], dtype="double")

    # distortion coefficients obtained from the camera calibration script, using a 9x6 chessboard
    dist_coeffs = np.array(
        [[-0.03792548, 0.09233237, 0.00419088, 0.00317323, -0.15804257]], dtype="double")

    def _get_landmarks(lms):
        surface = 0
        for lms0 in lms:
            landmarks = [np.array([point.x, point.y, point.z]) \
                         for point in lms0.landmark]

            landmarks = np.array(landmarks)

            landmarks[landmarks[:, 0] < 0., 0] = 0.
            landmarks[landmarks[:, 0] > 1., 0] = 1.
            landmarks[landmarks[:, 1] < 0., 1] = 0.
            landmarks[landmarks[:, 1] > 1., 1] = 1.

            dx = landmarks[:, 0].max() - landmarks[:, 0].min()
            dy = landmarks[:, 1].max() - landmarks[:, 1].min()
            new_surface = dx * dy
            if new_surface > surface:
                biggest_face = landmarks

        return biggest_face

    def main():

        parser = argparse.ArgumentParser(description='Driver State Detection')

        # selection the camera number, default is 0 (webcam)
        parser.add_argument('-c', '--camera', type=int,
                            default=0, metavar='', help='Camera number, default is 0 (webcam)')

        # TODO: add option for choose if use camera matrix and dist coeffs

        # visualisation parameters
        parser.add_argument('--show_fps', type=bool, default=True,
                            metavar='', help='Show the actual FPS of the capture stream, default is true')
        parser.add_argument('--show_proc_time', type=bool, default=True,
                            metavar='', help='Show the processing time for a single frame, default is true')
        parser.add_argument('--show_eye_proc', type=bool, default=False,
                            metavar='', help='Show the eyes processing, deafult is false')
        parser.add_argument('--show_axis', type=bool, default=True,
                            metavar='', help='Show the head pose axis, default is true')
        parser.add_argument('--verbose', type=bool, default=False,
                            metavar='', help='Prints additional info, default is false')

        # Attention Scorer parameters (EAR, Gaze Score, Pose)
        parser.add_argument('--smooth_factor', type=float, default=0.5,
                            metavar='',
                            help='Sets the smooth factor for the head pose estimation keypoint smoothing, default is 0.5')
        parser.add_argument('--ear_thresh', type=float, default=0.15,
                            metavar='', help='Sets the EAR threshold for the Attention Scorer, default is 0.15')
        parser.add_argument('--ear_time_thresh', type=float, default=2,
                            metavar='',
                            help='Sets the EAR time (seconds) threshold for the Attention Scorer, default is 2 seconds')
        parser.add_argument('--gaze_thresh', type=float, default=0.015,
                            metavar='', help='Sets the Gaze Score threshold for the Attention Scorer, default is 0.2')
        parser.add_argument('--gaze_time_thresh', type=float, default=2, metavar='',
                            help='Sets the Gaze Score time (seconds) threshold for the Attention Scorer, default is 2. seconds')
        parser.add_argument('--pitch_thresh', type=float, default=20,
                            metavar='',
                            help='Sets the PITCH threshold (degrees) for the Attention Scorer, default is 30 degrees')
        parser.add_argument('--yaw_thresh', type=float, default=20,
                            metavar='',
                            help='Sets the YAW threshold (degrees) for the Attention Scorer, default is 20 degrees')
        parser.add_argument('--roll_thresh', type=float, default=20,
                            metavar='',
                            help='Sets the ROLL threshold (degrees) for the Attention Scorer, default is 30 degrees')
        parser.add_argument('--pose_time_thresh', type=float, default=2.5,
                            metavar='',
                            help='Sets the Pose time threshold (seconds) for the Attention Scorer, default is 2.5 seconds')

        # parse the arguments and store them in the args variable dictionary
        args = parser.parse_args()

        if args.verbose:
            print(f"Arguments and Parameters used:\n{args}\n")

        if not cv2.useOptimized():
            try:
                cv2.setUseOptimized(True)  # set OpenCV optimization to True
            except:
                print(
                    "OpenCV optimization could not be set to True, the script may be slower than expected")

        """instantiation of mediapipe face mesh model. This model give back 478 landmarks
        if the rifine_landmarks parameter is set to True. 468 landmarks for the face and
        the last 10 landmarks for the irises
        """
        detector = mp.solutions.face_mesh.FaceMesh(static_image_mode=False,
                                                   min_detection_confidence=0.5,
                                                   min_tracking_confidence=0.5,
                                                   refine_landmarks=True)

        # instantiation of the eye detector and pose estimator objects
        Eye_det = EyeDet(show_processing=args.show_eye_proc)

        Head_pose = HeadPoseEst(show_axis=args.show_axis)

        # instantiation of the attention scorer object, with the various thresholds
        # NOTE: set verbose to True for additional printed information about the scores
        t0 = time.perf_counter()
        Scorer = AttScorer(t_now=t0, ear_thresh=args.ear_thresh, gaze_time_thresh=args.gaze_time_thresh,
                           roll_thresh=args.roll_thresh, pitch_thresh=args.pitch_thresh,
                           yaw_thresh=args.yaw_thresh, ear_time_thresh=args.ear_time_thresh,
                           gaze_thresh=args.gaze_thresh, pose_time_thresh=args.pose_time_thresh,
                           verbose=args.verbose)

        # capture the input from the default system camera (camera number 0)
        cap = cv2.VideoCapture(args.camera)
        if not cap.isOpened():  # if the camera can't be opened exit the program
            print("Cannot open camera")
            exit()

        i = 0
        time.sleep(0.01)  # To prevent zero division error when calculating the FPS
        count = 0
        while True:  # infinite loop for webcam video capture
            t_now = time.perf_counter()
            fps = i / (t_now - t0)
            if fps == 0:
                fps = 10

            ret, frame = cap.read()  # read a frame from the webcam

            if not ret:  # if a frame can't be read, exit the program
                print("Can't receive frame from camera/stream end")
                break

            # if the frame comes from webcam, flip it so it looks like a mirror.
            if args.camera == 0:
                frame = cv2.flip(frame, 2)

            # start the tick counter for computing the processing time for each frame
            e1 = cv2.getTickCount()

            # transform the BGR frame in grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # get the frame size
            frame_size = frame.shape[1], frame.shape[0]

            # apply a bilateral filter to lower noise but keep frame details. create a 3D matrix from gray image to give it to the model
            gray = np.expand_dims(cv2.bilateralFilter(gray, 5, 10, 10), axis=2)
            gray = np.concatenate([gray, gray, gray], axis=2)

            # find the faces using the face mesh model
            lms = detector.process(gray).multi_face_landmarks
            print(lms)

            if lms is None:
                count = count + 1
                print(count)
                if count > 4000:
                    status = 'Absent'
                    break

            if lms:  # process the frame only if at least a face is found
                # getting face landmarks and then take only the bounding box of the biggest face
                landmarks = _get_landmarks(lms)
                la = 'normal'
                mylist.append(la)

                # shows the eye keypoints (can be commented)
                Eye_det.show_eye_keypoints(
                    color_frame=frame, landmarks=landmarks, frame_size=frame_size)

                # compute the EAR score of the eyes
                ear = Eye_det.get_EAR(frame=gray, landmarks=landmarks)

                # compute the PERCLOS score and state of tiredness
                tired, perclos_score = Scorer.get_PERCLOS(t_now, fps, ear)

                # compute the Gaze Score
                gaze = Eye_det.get_Gaze_Score(
                    frame=gray, landmarks=landmarks, frame_size=frame_size)

                # compute the head pose
                frame_det, roll, pitch, yaw = Head_pose.get_pose(
                    frame=frame, landmarks=landmarks, frame_size=frame_size)

                # evaluate the scores for EAR, GAZE and HEAD POSE
                asleep, looking_away, distracted = Scorer.eval_scores(t_now=t_now,
                                                                      ear_score=ear,
                                                                      gaze_score=gaze,
                                                                      head_roll=roll,
                                                                      head_pitch=pitch,
                                                                      head_yaw=yaw)

                # if the head pose estimation is successful, show the results
                if frame_det is not None:
                    frame = frame_det

                # show the real-time EAR score
                if ear is not None:
                    cv2.putText(frame, "EAR:" + str(round(ear, 3)), (10, 50),
                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1, cv2.LINE_AA)

                # show the real-time Gaze Score
                if gaze is not None:
                    cv2.putText(frame, "Gaze Score:" + str(round(gaze, 3)), (10, 80),
                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1, cv2.LINE_AA)

                # show the real-time PERCLOS score
                cv2.putText(frame, "PERCLOS:" + str(round(perclos_score, 3)), (10, 110),
                            cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1, cv2.LINE_AA)

                if roll is not None:
                    cv2.putText(frame, "roll:" + str(roll.round(1)[0]), (450, 40),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), 1, cv2.LINE_AA)
                if pitch is not None:
                    cv2.putText(frame, "pitch:" + str(pitch.round(1)[0]), (450, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), 1, cv2.LINE_AA)
                if yaw is not None:
                    cv2.putText(frame, "yaw:" + str(yaw.round(1)[0]), (450, 100),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), 1, cv2.LINE_AA)

                # if the driver is tired, show and alert on screen
                if tired:
                    cv2.putText(frame, "TIRED!", (10, 280),
                                cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1, cv2.LINE_AA)
                    la = 'TIRED'
                    mylist.append(la)

                # if the state of attention of the driver is not normal, show an alert on screen
                if asleep:
                    cv2.putText(frame, "ASLEEP!", (10, 300),
                                cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1, cv2.LINE_AA)
                    la = 'ASLEEP'

                    mylist.append(la)

                if looking_away:
                    cv2.putText(frame, "LOOKING AWAY!", (10, 320),
                                cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1, cv2.LINE_AA)
                    la = 'Cheating'
                    mylist.append(la)

                if distracted:
                    cv2.putText(frame, "DISTRACTED!", (10, 340),
                                cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1, cv2.LINE_AA)
                    la = 'Cheating'
                    mylist.append(la)


            # stop the tick counter for computing the processing time for each frame
            e2 = cv2.getTickCount()
            # processign time in milliseconds
            proc_time_frame_ms = ((e2 - e1) / cv2.getTickFrequency()) * 1000
            # print fps and processing time per frame on screen

            # show the frame on screen
            cv2.imshow("Press 'q' to terminate", frame)

            # if the key "q" is pressed on the keyboard, the program is terminated
            if cv2.waitKey(20) & 0xFF == ord('q'):
                status = 'present'
                break

            i += 1

        cap.release()
        cv2.destroyAllWindows()

        return

    main()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO updatestatus VALUES ('','" + str(sid) + "','"+str(la)+"')")
    conn.commit()
    conn.close()




    return render_template("studenthome.html")
@app.route("/sview")
def sview():


         uid=session['uid']
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
         cursor1 = conn.cursor()
         cursor1.execute("select * from result where uid='"+str(uid)+"' and status='1'")
         data2 = cursor1.fetchall()
         print(data2)

         return render_template("result.html", data=data2)
@app.route("/stafflogin",methods=['GET','POST'])
def stafflogin():
    if request.method == 'POST':
        uname=request.form['uname']
        password=request.form['password']
        print(uname)
        print(password)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
        cursor = conn.cursor()
        cursor.execute("select * from staffregister where name='"+uname+"' and staffid='"+password+"'")
        data=cursor.fetchone()
        print(data)
        if data is None:
            return "user name and password incorrect"
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
            cursor = conn.cursor()
            cursor = conn.cursor()
            cursor.execute("select * from register")
            data = cursor.fetchall()
           # session['uid'] = data[0]
            return render_template("staffhome.html",data=data)
@app.route("/staffhome")
def staffhome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')

    cursor = conn.cursor()
    cursor.execute("select * from register")
    data = cursor.fetchall()
    # session['uid'] = data[0]
    return render_template("staffhome.html", data=data)
@app.route("/rview")
def rview():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')

    cursor = conn.cursor()
    cursor.execute("select * from result where status='0'")
    data = cursor.fetchall()
    # session['uid'] = data[0]
    return render_template("rview.html", data=data)
@app.route("/rview1",methods=['GET','POST'])
def rview1():
    if request.method == 'POST':
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')

        cursor = conn.cursor()
        cursor.execute("update result set status='1'")
        conn.commit()
        conn.close()
        conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')

        cursor1 = conn1.cursor()
        cursor1.execute("select * from result where status='0'")
        data=cursor1.fetchall()


        return render_template("rview.html", data=data)
@app.route("/search",methods=['GET','POST'])
def search():
    if request.method == 'POST':

        name=request.form['name']
        conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')

        cursor1 = conn1.cursor()
        cursor1.execute("select * from exam where etype='"+name+"'")
        data = cursor1.fetchall()

        return render_template("view.html", data=data)

@app.route("/reports")
def reports():



         conn = mysql.connector.connect(user='root', password='', host='localhost', database='onlineexam')
         cursor1 = conn.cursor()
         cursor1.execute("select * from updatestatus")
         data2 = cursor1.fetchall()
         print(data2)

         return render_template("reports.html", data=data2)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)