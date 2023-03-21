import maya.cmds as cmds

#Global Variables
rowsVar=1
materials=["BaseColor"]
files=[]
colorSpace=["sRGB"]

#Window function
def makeUI():
    #Delete window if it exists
    if cmds.window("Window", exists=True):
        cmds.deleteUI("Window")
    #Create window
    cmds.window("Window",t="Link Textures",s=True)
    form=cmds.formLayout(nd=100)
    #Column Layout
    columns=cmds.rowColumnLayout(nc=2,cat=([1,'both',5],[2,'both',5]),cw=[1,250])
    #Material selection
    makeUI.matSel=cmds.optionMenu(label="Material",cc="matSelected()")
    cmds.menuItem(label='aiStandardSurface')
    #More material options
    #cmds.menuItem(label='Lambert')
    #First row
    makeUI.firstRow=cmds.rowColumnLayout(nr=1)
    #Texture Map selection
    makeUI.mapSel1=cmds.optionMenu(label="File",cc="matSelected()")
    cmds.menuItem(label='BaseColor')
    cmds.menuItem(label='Height')
    cmds.menuItem(label='Metallic')
    cmds.menuItem(label='Roughness')
    cmds.menuItem(label='Normal')
    cmds.menuItem(label='Opacity')
    cmds.menuItem(label='Transmission')
    #Color Space selection
    makeUI.colorSel1=cmds.optionMenu(label="ColorSpace",cc="CSSelected()")
    cmds.menuItem(label='sRGB')
    cmds.menuItem(label='Raw')
    #Checkbox UDIMs
    makeUI.checkUDIM1=cmds.checkBox(label='UDIM')
    #Checkbox Alpha is luminance
    makeUI.checkAlpha1=cmds.checkBox(label='Alpha is Luminance')
    #File selection
    makeUI.textureFileSL1=cmds.textFieldButtonGrp(l="File: ",tx="Select File",bl="select",ed=False,cw=([1,30],[2,200],[3,50]),cl3=['right','both','both'],bc='textureFile1()')
    #End of first row
    cmds.setParent("..")
    #spaces
    cmds.separator(style="none",h=5)
    cmds.separator(style="none",h=5)
    #Second row
    makeUI.matName=cmds.textFieldGrp( l='Material name: ', tx='aiStandardSurface', cal=([1,'left'],[2,'center']),cw=([1,80]),ad2=2,ed=True)
    #cmds.separator(style="none")
    makeUI.secondRow=cmds.rowColumnLayout(nr=1,en=False)
    #Texture Map selection
    makeUI.mapSel2=cmds.optionMenu(label="File",cc="mapSelected2()")
    cmds.menuItem(label='BaseColor')
    cmds.menuItem(label='Height')
    cmds.menuItem(label='Metallic')
    cmds.menuItem(label='Roughness')
    cmds.menuItem(label='Normal')
    cmds.menuItem(label='Opacity')
    cmds.menuItem(label='Transmission')
    #Color Space selection
    makeUI.colorSel2=cmds.optionMenu(label="ColorSpace",cc="CSSelected()")
    cmds.menuItem(label='sRGB')
    cmds.menuItem(label='Raw')
    #Checkbox UDIMs
    makeUI.checkUDIM2=cmds.checkBox(label='UDIM')
    #Checkbox Alpha is luminance
    makeUI.checkAlpha2=cmds.checkBox(label='Alpha is Luminance')
    #File selection
    makeUI.textureFileSL2=cmds.textFieldButtonGrp(l="File: ",tx="Select File",bl="select",ed=False,cw=([1,30],[2,200],[3,50]),cl3=['right','both','both'],bc='textureFile2()')
    #End of second row
    cmds.setParent("..")
    #spaces
    cmds.separator(style="none",h=5)
    cmds.separator(style="none",h=5)    
    #Third row
    cmds.separator(style="none")
    makeUI.thirdRow=cmds.rowColumnLayout(nr=1,en=False)
    #Texture Map selection
    makeUI.mapSel3=cmds.optionMenu(label="File",cc="mapSelected3()")
    cmds.menuItem(label='BaseColor')
    cmds.menuItem(label='Height')
    cmds.menuItem(label='Metallic')
    cmds.menuItem(label='Roughness')
    cmds.menuItem(label='Normal')
    cmds.menuItem(label='Opacity')
    cmds.menuItem(label='Transmission')
    #Color Space selection
    makeUI.colorSel3=cmds.optionMenu(label="ColorSpace",cc="CSSelected()")
    cmds.menuItem(label='sRGB')
    cmds.menuItem(label='Raw')
    #Checkbox UDIMs
    makeUI.checkUDIM3=cmds.checkBox(label='UDIM')
    #Checkbox Alpha is luminance
    makeUI.checkAlpha3=cmds.checkBox(label='Alpha is Luminance')
    #File selection
    makeUI.textureFileSL3=cmds.textFieldButtonGrp(l="File: ",tx="Select File",bl="select",ed=False,cw=([1,30],[2,200],[3,50]),cl3=['right','both','both'],bc='textureFile3()')
    #End of third row
    cmds.setParent("..")
    #spaces
    cmds.separator(style="none",h=5)
    cmds.separator(style="none",h=5) 
    #Fourth row
    cmds.separator(style="none")
    makeUI.fourthRow=cmds.rowColumnLayout(nr=1,en=False)
    #Texture Map selection
    makeUI.mapSel4=cmds.optionMenu(label="File",cc="mapSelected4()")
    cmds.menuItem(label='BaseColor')
    cmds.menuItem(label='Height')
    cmds.menuItem(label='Metallic')
    cmds.menuItem(label='Roughness')
    cmds.menuItem(label='Normal')
    cmds.menuItem(label='Opacity')
    cmds.menuItem(label='Transmission')
    #Color Space selection
    makeUI.colorSel4=cmds.optionMenu(label="ColorSpace",cc="CSSelected()")
    cmds.menuItem(label='sRGB')
    cmds.menuItem(label='Raw')
    #Checkbox UDIMs
    makeUI.checkUDIM4=cmds.checkBox(label='UDIM')
    #Checkbox Alpha is luminance
    makeUI.checkAlpha4=cmds.checkBox(label='Alpha is Luminance')
    #File selection
    makeUI.textureFileSL4=cmds.textFieldButtonGrp(l="File: ",tx="Select File",bl="select",ed=False,cw=([1,30],[2,200],[3,50]),cl3=['right','both','both'],bc='textureFile4()')
    #End of fourth row
    cmds.setParent("..")
    #spaces
    cmds.separator(style="none",h=5)
    cmds.separator(style="none",h=5) 
    #Fifth row
    cmds.separator(style="none")
    makeUI.fifthRow=cmds.rowColumnLayout(nr=1,en=False)
    #Texture Map selection
    makeUI.mapSel5=cmds.optionMenu(label="File",cc="mapSelected5()")
    cmds.menuItem(label='BaseColor')
    cmds.menuItem(label='Height')
    cmds.menuItem(label='Metallic')
    cmds.menuItem(label='Roughness')
    cmds.menuItem(label='Normal')
    cmds.menuItem(label='Opacity')
    cmds.menuItem(label='Transmission')
    #Color Space selection
    makeUI.colorSel5=cmds.optionMenu(label="ColorSpace",cc="CSSelected()")
    cmds.menuItem(label='sRGB')
    cmds.menuItem(label='Raw')
    #Checkbox UDIMs
    makeUI.checkUDIM5=cmds.checkBox(label='UDIM')
    #Checkbox Alpha is luminance
    makeUI.checkAlpha5=cmds.checkBox(label='Alpha is Luminance')
    #File selection
    makeUI.textureFileSL5=cmds.textFieldButtonGrp(l="File: ",tx="Select File",bl="select",ed=False,cw=([1,30],[2,200],[3,50]),cl3=['right','both','both'],bc='textureFile5()')
    #End of fifth row
    cmds.setParent("..")
    #spaces
    cmds.separator(style="none",h=5)
    cmds.separator(style="none",h=5)   
    #Sixth row
    cmds.separator(style="none")
    makeUI.sixthRow=cmds.rowColumnLayout(nr=1,en=False)
    #Texture Map selection
    makeUI.mapSel6=cmds.optionMenu(label="File",cc="mapSelected6()")
    cmds.menuItem(label='BaseColor')
    cmds.menuItem(label='Height')
    cmds.menuItem(label='Metallic')
    cmds.menuItem(label='Roughness')
    cmds.menuItem(label='Normal')
    cmds.menuItem(label='Opacity')
    cmds.menuItem(label='Transmission')
    #Color Space selection
    makeUI.colorSel6=cmds.optionMenu(label="ColorSpace",cc="CSSelected()")
    cmds.menuItem(label='sRGB')
    cmds.menuItem(label='Raw')
    #Checkbox UDIMs
    makeUI.checkUDIM6=cmds.checkBox(label='UDIM')
    #Checkbox Alpha is luminance
    makeUI.checkAlpha6=cmds.checkBox(label='Alpha is Luminance')
    #File selection
    makeUI.textureFileSL6=cmds.textFieldButtonGrp(l="File: ",tx="Select File",bl="select",ed=False,cw=([1,30],[2,200],[3,50]),cl3=['right','both','both'],bc='textureFile6()')
    #End of sixth row
    cmds.setParent("..")
    #spaces
    cmds.separator(style="none",h=5)
    cmds.separator(style="none",h=5)
    #Seventh row
    cmds.separator(style="none")
    makeUI.seventhRow=cmds.rowColumnLayout(nr=1,en=False)
    #Texture Map selection
    makeUI.mapSel7=cmds.optionMenu(label="File",cc="mapSelected7()")
    cmds.menuItem(label='BaseColor')
    cmds.menuItem(label='Height')
    cmds.menuItem(label='Metallic')
    cmds.menuItem(label='Roughness')
    cmds.menuItem(label='Normal')
    cmds.menuItem(label='Opacity')
    cmds.menuItem(label='Transmission')
    #Color Space selection
    makeUI.colorSel7=cmds.optionMenu(label="ColorSpace",cc="CSSelected()")
    cmds.menuItem(label='sRGB')
    cmds.menuItem(label='Raw')
    #Checkbox UDIMs
    makeUI.checkUDIM7=cmds.checkBox(label='UDIM')
    #Checkbox Alpha is luminance
    makeUI.checkAlpha6=cmds.checkBox(label='Alpha is Luminance')
    #File selection
    makeUI.textureFileSL7=cmds.textFieldButtonGrp(l="File: ",tx="Select File",bl="select",ed=False,cw=([1,30],[2,200],[3,50]),cl3=['right','both','both'],bc='textureFile7()')
    #End of seventh row
    cmds.setParent("..")
    #spaces
    cmds.separator(style="none",h=5)
    cmds.separator(style="none",h=5)
    #Button row
    cmds.separator(style="none")
    btnRow=cmds.rowColumnLayout(nr=1,rat=[1,'top',10])
    cmds.rowColumnLayout(nc=2,cat=([1,'both',5],[2,'both',5]),cw=[(1, 100), (2, 100)])
    cmds.button(l="Add",c="addBtn()")
    cmds.button(l="Remove",c="removeBtn()")
    cmds.setParent("..")
    #End of button row
    cmds.setParent("..")
    cmds.separator(style='none')
    #spaces
    cmds.separator(style="none",h=5)
    cmds.separator(style="none",h=5)
    #Create button
    cmds.rowColumnLayout(nc=3,cat=([1,'right',15],[2,'both',5],[3,'both',5]),cw=[(1, 200), (2, 300), (3, 100)])    
    makeUI.assignMat=cmds.checkBox(label='Assign material to selection')
    cmds.button(l="Create material",c="createConnection()",bgc=(0.4,0.4,0.4))  
    cmds.separator(style="none",h=5)
    cmds.setParent("..")
    cmds.setParent("..")
    cmds.formLayout(form,e=True,af=[(columns,'left',10),(columns,'top',10)])
    cmds.showWindow()
    
#Create window    
makeUI()

#Add row button function
def addBtn():    
    #Number of active rows variable
    global rowsVar
    print(rowsVar)
    #Enable rows and fill materials and colorSpace list with default value
    if rowsVar==1:
        cmds.rowColumnLayout(makeUI.secondRow,en=True,e=True)  
        materials.insert(1,"BaseColor")    
        colorSpace.insert(1,"sRGB") 
    if rowsVar==2:
        cmds.rowColumnLayout(makeUI.thirdRow,en=True,e=True)  
        materials.insert(2,"BaseColor")     
        colorSpace.insert(2,"sRGB")           
    if rowsVar==3:
        cmds.rowColumnLayout(makeUI.fourthRow,en=True,e=True)
        materials.insert(3,"BaseColor") 
        colorSpace.insert(3,"sRGB") 
    if rowsVar==4:
        cmds.rowColumnLayout(makeUI.fifthRow,en=True,e=True)  
        materials.insert(4,"BaseColor") 
        colorSpace.insert(4,"sRGB") 
    if rowsVar==5:
        cmds.rowColumnLayout(makeUI.sixthRow,en=True,e=True)
        materials.insert(5,"BaseColor") 
        colorSpace.insert(5,"sRGB")     
    if rowsVar==6:
        cmds.rowColumnLayout(makeUI.seventhRow,en=True,e=True)
        materials.insert(6,"BaseColor") 
        colorSpace.insert(6,"sRGB") 
    if rowsVar<7:
        rowsVar+=1
        
#Remove row button function
def removeBtn():
    #Number of active rows variable
    global rowsVar
    print(rowsVar)
    #Disable rows and remove elements from materials, files and colorSpace lists
    if rowsVar==2:
        cmds.rowColumnLayout(makeUI.secondRow,en=False,e=True)
        if len(materials)>=2:
            materials.pop(1)
            colorSpace.pop(1)
            print(materials)
            if len(files)>=2:
                files.pop(1)
                #Change the text of textField back to default
                cmds.textFieldButtonGrp(makeUI.textureFileSL2,e=True,tx="Select File")
    if rowsVar==3:
        cmds.rowColumnLayout(makeUI.thirdRow,en=False,e=True)  
        if len(materials)>=3:
            materials.pop(2)
            colorSpace.pop(2)
            print(materials)   
            if len(files)>=3:
                files.pop(2)  
                cmds.textFieldButtonGrp(makeUI.textureFileSL3,e=True,tx="Select File")         
    if rowsVar==4:
        cmds.rowColumnLayout(makeUI.fourthRow,en=False,e=True)
        if len(materials)>=4:
            materials.pop(3)
            colorSpace.pop(3)
            print(materials)
            if len(files)>=4:
                files.pop(3)
                cmds.textFieldButtonGrp(makeUI.textureFileSL4,e=True,tx="Select File")
    if rowsVar==5:
        cmds.rowColumnLayout(makeUI.fifthRow,en=False,e=True)  
        if len(materials)>=5:
            materials.pop(4)
            colorSpace.pop(4)
            print(materials)
            if len(files)>=5:
                files.pop(4)
                cmds.textFieldButtonGrp(makeUI.textureFileSL5,e=True,tx="Select File")
    if rowsVar==6:
        cmds.rowColumnLayout(makeUI.sixthRow,en=False,e=True)  
        if len(materials)>=6:
            materials.pop(5)
            colorSpace.pop(5)
            print(materials) 
            if len(files)>=6:
                files.pop(5) 
                cmds.textFieldButtonGrp(makeUI.textureFileSL6,e=True,tx="Select File")
    if rowsVar==7:
        cmds.rowColumnLayout(makeUI.seventhRow,en=False,e=True)   
        if len(materials)>=7:
            materials.pop(6)
            colorSpace.pop(6)
            print(materials)
            if len(files)>=7:
                files.pop(6)
                cmds.textFieldButtonGrp(makeUI.textureFileSL7,e=True,tx="Select File")
    if rowsVar>1:
        #Adjust variable to current state
        rowsVar-=1

#Material textures selection functions
#First row selection
def matSelected():  
    #Material selection
    matSelected.shader=cmds.optionMenu(makeUI.matSel,q=True,v=True)
    #delete element in the list if it already exists
    if len(materials)>=1:
        materials.pop(0)
    #Get selection from user
    matSelected.map1=cmds.optionMenu(makeUI.mapSel1,q=True,v=True) 
    #Insert in materials list
    materials.insert(0,matSelected.map1)
#Seccond row selection
def mapSelected2():
    if len(materials)>=2:
        materials.pop(1)
    mapSelected2.map2=cmds.optionMenu(makeUI.mapSel2,q=True,v=True)
    materials.insert(1,mapSelected2.map2)
#Third row selection
def mapSelected3():
    if len(materials)>=3:
        materials.pop(2)
    mapSelected3.map3=cmds.optionMenu(makeUI.mapSel3,q=True,v=True)
    materials.insert(2,mapSelected3.map3)
#Fourth row selection    
def mapSelected4():
    if len(materials)>=4:
        materials.pop(3)
    mapSelected4.map4=cmds.optionMenu(makeUI.mapSel4,q=True,v=True)
    materials.insert(3,mapSelected4.map4)
#Fifth row selection
def mapSelected5():
    if len(materials)>=5:
        materials.pop(4)
    mapSelected5.map5=cmds.optionMenu(makeUI.mapSel5,q=True,v=True)
    materials.insert(4,mapSelected5.map5)    
#Sixth row selection
def mapSelected6():
    if len(materials)>=6:
        materials.pop(5)
    mapSelected6.map6=cmds.optionMenu(makeUI.mapSel6,q=True,v=True)
    materials.insert(5,mapSelected6.map6) 
#Seventh row selection
def mapSelected7():
    if len(materials)>=7:
        materials.pop(6)
    mapSelected7.map7=cmds.optionMenu(makeUI.mapSel7,q=True,v=True)
    materials.insert(6,mapSelected7.map7)

#Files selection function
def browseTextureFiles():
    #Get current project 
    proj = cmds.workspace(q=True, rd=True)   
    #Save file path of user selected file in a variable
    browseTextureFiles.textureFile=cmds.fileDialog(m=0)

#First row file selection
def textureFile1():
    #Call file selection function
    browseTextureFiles()
    #Delete file path from files list if it already exists
    if len(files)>=1:
        files.pop(0)
    #insert file path in list
    files.insert(0,browseTextureFiles.textureFile)
    #Show file path in text field
    cmds.textFieldButtonGrp(makeUI.textureFileSL1,e=True,tx=files[0])    
#Second row file selection
def textureFile2():
    browseTextureFiles()
    if len(files)>=2:
        files.pop(1)
    files.insert(1,browseTextureFiles.textureFile)
    cmds.textFieldButtonGrp(makeUI.textureFileSL2,e=True,tx=files[1]) 
#Third row file selection        
def textureFile3():
    browseTextureFiles()
    if len(files)>=3:
        files.pop(2)
    files.insert(2,browseTextureFiles.textureFile)
    cmds.textFieldButtonGrp(makeUI.textureFileSL3,e=True,tx=files[2]) 
#Fourth row file selection                
def textureFile4():
    browseTextureFiles()
    if len(files)>=4:
        files.pop(3)
    files.insert(3,browseTextureFiles.textureFile)
    cmds.textFieldButtonGrp(makeUI.textureFileSL4,e=True,tx=files[3]) 
#Fifth row file selection        
def textureFile5():
    browseTextureFiles()
    if len(files)>=5:
        files.pop(4)
    files.insert(4,browseTextureFiles.textureFile)
    cmds.textFieldButtonGrp(makeUI.textureFileSL5,e=True,tx=files[4]) 
#Sixth row file selection
def textureFile6():
    browseTextureFiles()
    if len(files)>=6:
        files.pop(5)
    files.insert(5,browseTextureFiles.textureFile)
    cmds.textFieldButtonGrp(makeUI.textureFileSL6,e=True,tx=files[5]) 
#Seventh row file selection
def textureFile7():
    browseTextureFiles()
    if len(files)>=7:
        files.pop(6)
    files.insert(6,browseTextureFiles.textureFile)
    cmds.textFieldButtonGrp(makeUI.textureFileSL7,e=True,tx=files[6]) 

#Function to create shading nodes
def createConnection():
    #Current file variable
    createConnection.i=0
    #Selected object
    selObj=cmds.ls(sl=True)
    print(selObj)
    #Get shader selected by the user
    if matSelected.shader=="aiStandardSurface":
        mName=cmds.textFieldGrp(makeUI.matName,q=True,tx=True)
        print(mName)
        #Create shader and shader group nodes
        aiShader=cmds.shadingNode("aiStandardSurface",n=mName, asShader=True)
        shadingGrp=cmds.sets(n=mName+"SG",empty=True, renderable=True, noSurfaceShader=True)
        #Connect the nodes
        cmds.connectAttr(aiShader+".outColor",shadingGrp+".surfaceShader")
    #Other nodes options
    #if matSelected.shader=="Lambert":
        #cmds.shadingNode("lambert",asShader=True)
    #Create file nodes for each file in the list
    for i in range(0,len(files)):
        #Name file nodes with texture file names
        fileNodeName=files[i].split('/')[-1].split('.')[0]
        #Create file and place nodes
        fileNode=cmds.shadingNode('file',asTexture=True,isColorManaged=True,n=fileNodeName)
        placeNode=cmds.shadingNode('place2dTexture',asUtility=True)
        #ShadingNode connections
        cmds.connectAttr(placeNode+'.coverage',fileNode+'.coverage',f=True)
        cmds.connectAttr(placeNode+'.translateFrame',fileNode+'.translateFrame',f=True)
        cmds.connectAttr(placeNode+'.rotateFrame',fileNode+'.rotateFrame',f=True)
        cmds.connectAttr(placeNode+'.mirrorU',fileNode+'.mirrorU',f=True)
        cmds.connectAttr(placeNode+'.mirrorV',fileNode+'.mirrorV',f=True)
        cmds.connectAttr(placeNode+'.stagger',fileNode+'.stagger',f=True)
        cmds.connectAttr(placeNode+'.wrapU',fileNode+'.wrapU',f=True)
        cmds.connectAttr(placeNode+'.wrapV',fileNode+'.wrapV',f=True)
        cmds.connectAttr(placeNode+'.repeatUV',fileNode+'.repeatUV',f=True)
        cmds.connectAttr(placeNode+'.offset',fileNode+'.offset',f=True)
        cmds.connectAttr(placeNode+'.rotateUV',fileNode+'.rotateUV',f=True)
        cmds.connectAttr(placeNode+'.noiseUV',fileNode+'.noiseUV',f=True)
        cmds.connectAttr(placeNode+'.vertexUvOne',fileNode+'.vertexUvOne',f=True)
        cmds.connectAttr(placeNode+'.vertexUvTwo',fileNode+'.vertexUvTwo',f=True)
        cmds.connectAttr(placeNode+'.vertexUvThree',fileNode+'.vertexUvThree',f=True)
        cmds.connectAttr(placeNode+'.vertexCameraOne',fileNode+'.vertexCameraOne',f=True)
        cmds.connectAttr(placeNode+'.outUV',fileNode+'.uv')
        cmds.connectAttr(placeNode+'.outUvFilterSize',fileNode+'.uvFilterSize')
        cmds.setAttr(fileNode+'.fileTextureName', files[i], type='string')
        #Select the file node and save in a variable
        cmds.select(fileNode)
        fileNodes=pmc.selected()
        createConnection.node=fileNodes[0]
        #Call check attributes function
        checkAttr()        
        #Call connection nodes function
        arnoldConnection(aiShader,shadingGrp)
    #Assign material to selected object
    assignSel=cmds.checkBox(makeUI.assignMat,q=True,v=True)
    if (assignSel):
        print(shadingGrp)
        cmds.select(selObj)
        cmds.sets(e=True,fe=shadingGrp)
            
#Function to connect shading nodes to Arnold StandardSurface material
def arnoldConnection(shader,shGrp):
    print(createConnection.i)
    #Connect file node based on user selection
    if materials[createConnection.i]=="BaseColor":   
        cmds.connectAttr(createConnection.node+'.outColor',shader+'.baseColor')
    if materials[createConnection.i]=="Height":
        cmds.connectAttr(createConnection.node+'.outAlpha',shGrp+".displacementShader")
    if materials[createConnection.i]=="Metallic":
        cmds.connectAttr(createConnection.node+'.outAlpha',shader+'.metalness')
    if materials[createConnection.i]=="Roughness":
        cmds.connectAttr(createConnection.node+'.outAlpha',shader+'.specularRoughness')
    if materials[createConnection.i]=="Normal":
        #Create and connect bump2d node
        bumpNode=cmds.shadingNode("bump2d",asUtility=True)
        cmds.connectAttr(createConnection.node+'.outAlpha',bumpNode+'.bumpValue')
        cmds.connectAttr(bumpNode+".outNormal",shader+".normalCamera")
        #Set bump2d node to tangent space normals
        cmds.setAttr(bumpNode+".bumpInterp",1)
    if materials[createConnection.i]=="Opacity": 
        cmds.connectAttr(createConnection.node+'.outColor',shader+'.opacity')  
    if materials[createConnection.i]=="Transmission":  
        cmds.connectAttr(createConnection.node+'.outAlpha',shader+'.transmission')                  
    #Set user selected color space
    cmds.setAttr(createConnection.node+".colorSpace",colorSpace[createConnection.i],type="string")
    #Change current file variable
    createConnection.i+=1     

#Function to select UDIM and alpha is luminance
def checkAttr():
    #Check attributes for first file
    if createConnection.i==0:
        #Set attributes if checkbox value is True
        UDIM1=cmds.checkBox(makeUI.checkUDIM1,q=True,v=True)
        if(UDIM1):
            cmds.setAttr(createConnection.node+".uvTilingMode",3)
            
        alpha1=cmds.checkBox(makeUI.checkAlpha1,q=True,v=True)            
        if(alpha1):
            cmds.setAttr(createConnection.node+".alphaIsLuminance",1)
    #Check attributes for second file only if it exists      
    if createConnection.i==1:
        UDIM2=cmds.checkBox(makeUI.checkUDIM2,q=True,v=True)
        if(UDIM2):
            cmds.setAttr(createConnection.node+".uvTilingMode",3)
            
        alpha2=cmds.checkBox(makeUI.checkAlpha2,q=True,v=True)            
        if(alpha2):
            cmds.setAttr(createConnection.node+".alphaIsLuminance",1)
    #Check attributes for third file only if it exists        
    if createConnection.i==2:
        UDIM3=cmds.checkBox(makeUI.checkUDIM3,q=True,v=True)
        if(UDIM3):
            cmds.setAttr(createConnection.node+".uvTilingMode",3)
            
        alpha3=cmds.checkBox(makeUI.checkAlpha3,q=True,v=True)            
        if(alpha3):
            cmds.setAttr(createConnection.node+".alphaIsLuminance",1)
    #Check attributes for fourth file only if it exists
    if createConnection.i==3:
        UDIM4=cmds.checkBox(makeUI.checkUDIM4,q=True,v=True)
        if(UDIM4):
            cmds.setAttr(createConnection.node+".uvTilingMode",3)
            
        alpha4=cmds.checkBox(makeUI.checkAlpha4,q=True,v=True)            
        if(alpha4):
            cmds.setAttr(createConnection.node+".alphaIsLuminance",1)
    #Check attributes for fifth file only if it exists
    if createConnection.i==4:
        UDIM5=cmds.checkBox(makeUI.checkUDIM5,q=True,v=True)
        if(UDIM5):
            cmds.setAttr(createConnection.node+".uvTilingMode",3)
            
        alpha5=cmds.checkBox(makeUI.checkAlpha5,q=True,v=True)            
        if(alpha5):
            cmds.setAttr(createConnection.node+".alphaIsLuminance",1)
    #Check attributes for sixth file only if it exists            
    if createConnection.i==5:
        UDIM6=cmds.checkBox(makeUI.checkUDIM6,q=True,v=True)
        if(UDIM6):
            cmds.setAttr(createConnection.node+".uvTilingMode",3)
                
        alpha6=cmds.checkBox(makeUI.checkAlpha6,q=True,v=True)            
        if(alpha6):
            cmds.setAttr(createConnection.node+".alphaIsLuminance",1)
    #Check attributes for seventh file only if it exists        
    if createConnection.i==6:
        UDIM7=cmds.checkBox(makeUI.checkUDIM7,q=True,v=True)
        if(UDIM7):
            cmds.setAttr(createConnection.node+".uvTilingMode",3)
            
        alpha7=cmds.checkBox(makeUI.checkAlpha7,q=True,v=True)            
        if(alpha7):
            cmds.setAttr(createConnection.node+".alphaIsLuminance",1)            

#Function to change color space                                                
def CSSelected():
    #Check for active rows
    if rowsVar>=1:
        #Delete element in list if it exists
        if len(colorSpace)>=1:
            colorSpace.pop(0)
        #Replace element in list with selected one
        csSel1=cmds.optionMenu(makeUI.colorSel1,v=True,q=True)
        colorSpace.insert(0,csSel1)
    #Check second row
    if rowsVar>=2:
        if len(colorSpace)>=2:
            colorSpace.pop(1)
        csSel2=cmds.optionMenu(makeUI.colorSel2,v=True,q=True)
        colorSpace.insert(1,csSel2)
    #Check third row
    if rowsVar>=3:
        if len(colorSpace)>=3:
            colorSpace.pop(2)
        csSel3=cmds.optionMenu(makeUI.colorSel3,v=True,q=True)
        colorSpace.insert(2,csSel3)
    #Check fourth row    
    if rowsVar>=4:
        if len(colorSpace)>=4:
            colorSpace.pop(3)
        csSel4=cmds.optionMenu(makeUI.colorSel4,v=True,q=True)
        colorSpace.insert(3,csSel4)  
    #Check fifth row    
    if rowsVar>=5:
        if len(colorSpace)>=5:
            colorSpace.pop(4)
        csSel5=cmds.optionMenu(makeUI.colorSel5,v=True,q=True)
        colorSpace.insert(4,csSel5)  
    #Check sixth row    
    if rowsVar>=6:
        if len(colorSpace)>=6:
            colorSpace.pop(5)
        csSel6=cmds.optionMenu(makeUI.colorSel6,v=True,q=True)
        colorSpace.insert(5,csSel6)     
    #Check seventh row    
    if rowsVar>=7:
        if len(colorSpace)==7:
            colorSpace.pop(6)
        csSel7=cmds.optionMenu(makeUI.colorSel7,v=True,q=True)
        colorSpace.insert(6,csSel7)      
         