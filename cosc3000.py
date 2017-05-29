#COSC3000 Computer Graphics Project

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import *
from time import *
from math import *
from mouseInteractor import MouseInteractor
from objloader import *

hWindow = 0


CamPhi = 0
CamTheta = 0
CamRange = 10

def DrawCar():
    glBindTexture(GL_TEXTURE_2D, 0)
    glPushMatrix()
    glTranslatef(0,0.6,0)
    glRotatef(90.0, 0.0, 1.0, 0.0)
    glCallList(car.gl_list)
    glPopMatrix()

def DrawBus():
    glEnable(GL_TEXTURE_2D)
    
    glPushMatrix()

    glColor3f(1.0,1.0,1.0)
    glBindTexture(GL_TEXTURE_2D, busFrontID)
    
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex(-1.0, 1.0, 0.0)
    glTexCoord2f(0, 0)
    glVertex(-1.0, 0.2, 0.0)
    glTexCoord2f(1, 0)
    glVertex(1.0, 0.2, 0.0)
    glTexCoord2f(1, 1)
    glVertex(1.0, 1.0, 0.0)
    glEnd()
    
    glBindTexture(GL_TEXTURE_2D, busBonnetID)
    
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex(-1.0, 1.0, 0.0)
    glTexCoord2f(0, 0)
    glVertex(-1.0, 1.0, 1.0)
    glTexCoord2f(1, 0)
    glVertex(1.0, 1.0, 1.0)
    glTexCoord2f(1, 1)
    glVertex(1.0, 1.0, 0.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, busWindshieldID)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex(-1.0, 1.0, 1.0)
    glTexCoord2f(1, 0)
    glVertex(1.0, 1.0, 1.0)
    glTexCoord2f(1, 1)
    glVertex(1.0, 2.0, 1.0)
    glTexCoord2f(0, 1)
    glVertex(-1.0, 2.0, 1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, busTopID)
    
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex(-1.0, 2.0, 1.0)
    glTexCoord2f(1, 0)
    glVertex(1.0, 2.0, 1.0)
    glTexCoord2f(1, 1)
    glVertex(1.0, 2.0, 4.0)
    glTexCoord2f(0, 1)
    glVertex(-1.0, 2.0, 4.0)
    glEnd()


    glBindTexture(GL_TEXTURE_2D, busFWheelID)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex(1.0, 0.2, 0.0)
    glTexCoord2f(1, 0)
    glVertex(1.0, 0.2, 1.0)
    glTexCoord2f(1, 1)
    glVertex(1.0, 1.0, 1.0)
    glTexCoord2f(0, 1)
    glVertex(1.0, 1.0, 0.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, busSideID)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex(1.0, 0.2, 1.0)
    glTexCoord2f(1, 0)
    glVertex(1.0, 0.2, 4.0)
    glTexCoord2f(1, 1)
    glVertex(1.0, 2.0, 4.0)
    glTexCoord2f(0, 1)
    glVertex(1.0, 2.0, 1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, busFWheelID)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex(-1.0, 0.2, 0.0)
    glTexCoord2f(1, 0)
    glVertex(-1.0, 0.2, 1.0)
    glTexCoord2f(1, 1)
    glVertex(-1.0, 1.0, 1.0)
    glTexCoord2f(0, 1)
    glVertex(-1.0, 1.0, 0.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, busSideID)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex(-1.0, 0.2, 1.0)
    glTexCoord2f(1, 0)
    glVertex(-1.0, 0.2, 4.0)
    glTexCoord2f(1, 1)
    glVertex(-1.0, 2.0, 4.0)
    glTexCoord2f(0, 1)
    glVertex(-1.0, 2.0, 1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, busRearID)

    glBegin(GL_QUADS)
    glTexCoord2f(1, 0)
    glVertex(1.0, 0.2, 4.0)
    glTexCoord2f(0, 0)
    glVertex(-1.0, 0.2, 4.0)
    glTexCoord2f(0, 1)
    glVertex(-1.0, 2.0, 4.0)
    glTexCoord2f(1, 1)
    glVertex(1.0, 2.0, 4.0)
    glEnd()

    #Wheels

    glPushMatrix()
    glColor3f(0,0,0)
    quadratic = gluNewQuadric();
    glTranslatef(.9,0.25,0.65)
    glRotatef(90.0, 0.0, 1.0, 0.0)
    gluCylinder(quadratic, 0.25, 0.25, 0.2, 10, 10)
    glTranslatef(0,0,0.2)
    gluDisk(quadratic, 0.2, 0.25, 10, 10)
    glColor3f(0.85,0.85,0.85)
    gluDisk(quadratic, 0, 0.2, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0,0,0)
    quadratic = gluNewQuadric();
    glTranslatef(-.9,0.25,0.65)
    glRotatef(-90.0, 0.0, 1.0, 0.0)
    gluCylinder(quadratic, 0.25, 0.25, 0.2, 10, 10)
    glTranslatef(0,0,0.2)
    gluDisk(quadratic, 0.2, 0.25, 10, 10)
    glColor3f(0.85,0.85,0.85)
    gluDisk(quadratic, 0, 0.2, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0,0,0)
    quadratic = gluNewQuadric();
    glTranslatef(.9,0.25,3.0)
    glRotatef(90.0, 0.0, 1.0, 0.0)
    gluCylinder(quadratic, 0.25, 0.25, 0.2, 10, 10)
    glTranslatef(0,0,0.2)
    gluDisk(quadratic, 0.2, 0.25, 10, 10)
    glColor3f(0.85,0.85,0.85)
    gluDisk(quadratic, 0, 0.2, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0,0,0)
    quadratic = gluNewQuadric();
    glTranslatef(-.9,0.25,3.0)
    glRotatef(-90.0, 0.0, 1.0, 0.0)
    gluCylinder(quadratic, 0.25, 0.25, 0.2, 10, 10)
    glTranslatef(0,0,0.2)
    gluDisk(quadratic, 0.2, 0.25, 10, 10)
    glColor3f(0.85,0.85,0.85)
    gluDisk(quadratic, 0, 0.2, 10, 10)
    glPopMatrix()
    
    glPopMatrix()

def DrawGround():

    glEnable(GL_TEXTURE_2D)
    glPushMatrix()

    glBindTexture(GL_TEXTURE_2D, groundTextureID)
    
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex(-4000, 0, -4000)
    glTexCoord2f(0, 1000)
    glVertex(4000, 0, -4000)
    glTexCoord2f(1000, 1000)
    glVertex(4000, 0, 4000)
    glTexCoord2f(1000, 0)
    glVertex(-4000, 0, 4000)
    glEnd()

    glPopMatrix()

def DrawSkyBox():
    scaling = 70.0

    glEnable(GL_TEXTURE_2D)
    
    glPushMatrix()
    glDisable(GL_DEPTH_TEST)
    
    glColor3f(1,1,1) #front
    glBindTexture(GL_TEXTURE_2D, skyFrontID)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex(-scaling, -scaling, -scaling)
    glTexCoord2f(1, 0)
    glVertex(scaling, -scaling, -scaling)
    glTexCoord2f(1, 1)
    glVertex(scaling, scaling, -scaling)
    glTexCoord2f(0, 1)

    glVertex(-scaling, scaling, -scaling)

    glEnd()

    glBindTexture(GL_TEXTURE_2D, skyLeftID)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-scaling, -scaling, scaling)
    glTexCoord2f(1, 0)
    glVertex3f(-scaling, -scaling, -scaling)
    glTexCoord2f(1, 1)
    glVertex3f(-scaling, scaling, -scaling)
    glTexCoord2f(0, 1)

    glVertex3f(-scaling, scaling, scaling)

    glEnd()

    glBindTexture(GL_TEXTURE_2D, skyRightID)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(scaling, -scaling, -scaling)
    glTexCoord2f(1, 0)
    glVertex3f(scaling, -scaling, scaling)
    glTexCoord2f(1, 1)
    glVertex3f(scaling, scaling, scaling)
    glTexCoord2f(0, 1)

    glVertex3f(scaling, scaling, -scaling)

    glEnd()

    glBindTexture(GL_TEXTURE_2D, skyBackID)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex(-scaling, -scaling, scaling)
    glTexCoord2f(1, 0)
    glVertex(scaling, -scaling, scaling)
    glTexCoord2f(1, 1)
    glVertex(scaling, scaling, scaling)
    glTexCoord2f(0, 1)

    glVertex(-scaling, scaling, scaling)

    glEnd()

    glBindTexture(GL_TEXTURE_2D, skyTopID)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-scaling, scaling, -scaling)
    glTexCoord2f(1, 0)
    glVertex3f(scaling, scaling, -scaling)
    glTexCoord2f(0, 1)
    glVertex3f(scaling, scaling, scaling)
    glTexCoord2f(1, 1)

    glVertex3f(-scaling, scaling, scaling)

    glEnd()
    
    glBindTexture(GL_TEXTURE_2D, 0)
    glEnable(GL_DEPTH_TEST)

    glPopMatrix()
    
def DrawGLScene():
    global numCars, busEnabled
    
    #Clear screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    r_xz = CamRange * cos(CamPhi)
    x = r_xz * sin(CamTheta)
    y = CamRange * sin(CamPhi)
    z = r_xz * cos(CamTheta)

    gluLookAt(25,10,-60,
              0,0,0,
              0,1,0, 
    )

    mouseInteractor.applyTransformation()

    DrawSkyBox()

    counter = 0
    counterx = 0
    counterz = -3

    DrawGround()

    glColor3f(0,0,0)
    glRasterPos3f(37, 20, 0)
    text = "Number of passengers: " + str(numCars)
    for c in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int( ord(c) ))

    if busEnabled:
        carCounter = math.ceil(numCars / 20)
    else:
        carCounter = numCars

    glPushMatrix()
    while (counter < carCounter):
        glPushMatrix()
        glTranslatef(0, 0, counterz*8.0)
        glTranslatef((counterx-3)*8.0, 0, 0)
        counter += 1
        if busEnabled:
            DrawBus()
        else:
            DrawCar()
        glPopMatrix()
        counterx += 1
        if counterx > 6:
            counterx = 0
            counterz += 1
    glPopMatrix()

    glutSwapBuffers()

    sleep(0.01) #non-NVIDIA support
    return

def ResizeGLScene(nWidth, nHeight):
    #Divide by 0 protection
    if nHeight == 0:
        nHeight = 1

    #Reset viewport
    glViewport(0, 0, nWidth, nHeight)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float( nWidth )/float( nHeight ), 0.1, 1000.0)

    #Return to the modelview matrix mode
    glMatrixMode(GL_MODELVIEW)
    return

def LoadTextures():
    #sky
    LoadSkybox()
    
    #ground
    global groundTexture
    groundTexture = Image()
    bmp = open("textures/grass.bmp")
    groundTexture.sizeX = bmp.size[0]
    groundTexture.sizeY = bmp.size[1]
    groundTexture.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()
    
    #bus
    global busTextureFront, busTextureBonnet, busTextureWindshield, busTextureTop, busTextureFWheel, busTextureSide, busTextureRear

    busTextureFront = Image()
    bmp = open("textures/bus_front.bmp")
    busTextureFront.sizeX = bmp.size[0]
    busTextureFront.sizeY = bmp.size[1]
    busTextureFront.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

    busTextureBonnet = Image()
    bmp = open("textures/bus_bonnet.bmp")
    busTextureBonnet.sizeX = bmp.size[0]
    busTextureBonnet.sizeY = bmp.size[1]
    busTextureBonnet.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

    busTextureWindshield = Image()
    bmp = open("textures/bus_windshield.bmp")
    busTextureWindshield.sizeX = bmp.size[0]
    busTextureWindshield.sizeY = bmp.size[1]
    busTextureWindshield.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

    busTextureTop = Image()
    bmp = open("textures/bus_top.bmp")
    busTextureTop.sizeX = bmp.size[0]
    busTextureTop.sizeY = bmp.size[1]
    busTextureTop.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

    busTextureFWheel = Image()
    bmp = open("textures/bus_frontwheel.bmp")
    busTextureFWheel.sizeX = bmp.size[0]
    busTextureFWheel.sizeY = bmp.size[1]
    busTextureFWheel.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

    busTextureSide = Image()
    bmp = open("textures/bus_side.bmp")
    busTextureSide.sizeX = bmp.size[0]
    busTextureSide.sizeY = bmp.size[1]
    busTextureSide.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

    busTextureRear = Image()
    bmp = open("textures/bus_rear.bmp")
    busTextureRear.sizeX = bmp.size[0]
    busTextureRear.sizeY = bmp.size[1]
    busTextureRear.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

def LoadSkybox():
    global skyFront, skyLeft, skyRight, skyBack, skyTop
    global skyFrontID, skyLeftID, skyRightID, skyBackID, skyTopID
    
    skyFront = Image()
    bmp = open("textures/skybox/front.bmp")
    skyFront.sizeX = bmp.size[0]
    skyFront.sizeY = bmp.size[1]
    skyFront.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

    skyLeft = Image()
    bmp = open("textures/skybox/left.bmp")
    bmp.rotate(180)
    bmp.resize((512,512))
    skyLeft.sizeX = bmp.size[0]
    skyLeft.sizeY = bmp.size[1]
    skyLeft.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

    skyRight = Image()
    bmp = open("textures/skybox/right.bmp")
    bmp.rotate(180)
    bmp.resize((512,512))
    skyRight.sizeX = bmp.size[0]
    skyRight.sizeY = bmp.size[1]
    skyRight.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

    skyBack = Image()
    bmp = open("textures/skybox/back.bmp")
    bmp.rotate(180)
    bmp.resize((512,512))
    skyBack.sizeX = bmp.size[0]
    skyBack.sizeY = bmp.size[1]
    skyBack.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()

    skyTop = Image()
    bmp = open("textures/skybox/top.bmp")
    bmp.rotate(180)
    bmp.resize((512,512))
    skyTop.sizeX = bmp.size[0]
    skyTop.sizeY = bmp.size[1]
    skyTop.data = bmp.tobytes("raw","RGBX", 0, -1)
    bmp.close()
    
    #Skybox
    skyFrontID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, skyFrontID)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, skyFront.sizeX, skyFront.sizeY, 0, GL_RGBA, GL_UNSIGNED_BYTE, skyFront.data)

    skyLeftID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, skyLeftID)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, skyLeft.sizeX, skyLeft.sizeY, 0, GL_RGBA, GL_UNSIGNED_BYTE, skyLeft.data)

    skyRightID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, skyRightID)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, skyRight.sizeX, skyRight.sizeY, 0, GL_RGBA, GL_UNSIGNED_BYTE, skyRight.data)

    skyBackID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, skyBackID)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, skyBack.sizeX, skyBack.sizeY, 0, GL_RGBA, GL_UNSIGNED_BYTE, skyBack.data)

    skyTopID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, skyTopID)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, skyTop.sizeX, skyTop.sizeY, 0, GL_RGBA, GL_UNSIGNED_BYTE, skyTop.data)
    

        

def InitTexturing():
    global busFrontID, busBonnetID, busWindshieldID, busTopID, busFWheelID, busSideID, busRearID
    global groundTextureID
    global busTextureFront, busTextureBonnet, busTextureWindshield, busTextureTop, busTextureFWheel, busTextureSide, busTextureRear
    global groundTexture
    global bRepeatTexture

    glEnable(GL_TEXTURE_2D)

    #Ground Texture
    groundTextureID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, groundTextureID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glTexImage2D(GL_TEXTURE_2D, 0, 4, groundTexture.sizeX, groundTexture.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, groundTexture.data)

    #Bus Textures
    busFrontID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, busFrontID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

    glTexImage2D(GL_TEXTURE_2D, 0, 4, busTextureFront.sizeX, busTextureFront.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, busTextureFront.data)

    busBonnetID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, busBonnetID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

    glTexImage2D(GL_TEXTURE_2D, 0, 4, busTextureBonnet.sizeX, busTextureBonnet.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, busTextureBonnet.data)

    busWindshieldID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, busWindshieldID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

    glTexImage2D(GL_TEXTURE_2D, 0, 4, busTextureWindshield.sizeX, busTextureWindshield.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, busTextureWindshield.data)

    busTopID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, busTopID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

    glTexImage2D(GL_TEXTURE_2D, 0, 4, busTextureTop.sizeX, busTextureTop.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, busTextureTop.data)

    busFWheelID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, busFWheelID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

    glTexImage2D(GL_TEXTURE_2D, 0, 4, busTextureFWheel.sizeX, busTextureFWheel.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, busTextureFWheel.data)

    busSideID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, busSideID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

    glTexImage2D(GL_TEXTURE_2D, 0, 4, busTextureSide.sizeX, busTextureSide.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, busTextureSide.data)

    busRearID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, busRearID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

    glTexImage2D(GL_TEXTURE_2D, 0, 4, busTextureRear.sizeX, busTextureRear.sizeY,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, busTextureRear.data)
        

def InitLighting():
    glColor3f(1.0, 1.0, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, -0.5, -1.0, -1.0);
    glLightfv( GL_LIGHT0, GL_AMBIENT, (0.8, 0.8, 0.8, 1) )
    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)


def InitGL(nWidth, nHeight):
    LoadTextures()
    InitTexturing()
    InitLighting()
    
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    ResizeGLScene(nWidth, nHeight)
    return

def KeyPressed( key, x, y ):
    global numCars, busEnabled
    
    key = ord(key)
    
    if key == 27 or key == ord( 'Q' ) or key == ord( 'q' ): #quit
        glutDestroyWindow( hWindow )
        sys.exit( )
    elif key == ord( 'W' ) or key == ord( 'w' ):
        numCars += 1
    elif key == ord( 'S' ) or key == ord( 's' ):
        numCars -= 1
        if numCars < 0:
            numCars = 0
    elif key == ord( 'A' ) or key == ord( 'a' ):
        busEnabled = not(busEnabled)
    else:
        return

def main():
    global hWindow, numCars, busEnabled

    nWidth = 1280
    nHeight = 720

    #Init GLUT
    glutInit("")
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    
    glutInitWindowSize(nWidth, nHeight)
    glutInitWindowPosition(0, 0)

    #Create window
    hWindow = glutCreateWindow(b"Bus Passenger Simulator")

    global mouseInteractor
    mouseInteractor = MouseInteractor( .01, 1 )
    mouseInteractor.registerCallbacks( )

    #load blender file with car model
    global car
    car = OBJ("car.obj")

    #init variables for actual demonstration
    numCars = 1
    busEnabled = False

    #Display callbacks
    glutIdleFunc(DrawGLScene)
    glutDisplayFunc(DrawGLScene)
    glutReshapeFunc(ResizeGLScene)

    #Keyboard input callback
    glutKeyboardFunc(KeyPressed)

    #Init function
    InitGL(nWidth, nHeight)

    #Window main loop
    glutMainLoop()

#Start program
print("COSC3000 Assignment - Callum Bryson - Bus Capacity Simulator")
print("Hit Q or ESC to quit")
print("W/S = Increase/Decrease number of passengers")
print("A = Toggle bus/car view")
main( )
