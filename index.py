#!/usr/bin/python
#facebook.com/p0rtclose
#instagram/fv.5v
#https://www.youtube.com/channel/UC2FiUYfYNSP36b8KL6w79rg?view_as=subscriber
mess = """< programed By hayder iQ:~# >
               $+++++++++++++++++++++++++$
               $+The next best,God willing+$
               $+++++++++++++++++++++++++$
"""
print mess
title = raw_input("insert title:")
heading = raw_input("insert heading :")
imagelink = raw_input("insert  URL for image central:")
bgimage = raw_input("Enter the link to the background image (Optional):")
message = raw_input("Enter a message (use <br> to download a line):")
textcolor = raw_input("Enter text color by value hex:")


#Abrir la index
fo = open("index.html","w")

messagescript1 = """<html><head><title>"""

messagescript2 = title

messagescript3 = """</title></head>
<body>

<br>

<body bgcolor="#000000" background ="""

messagescript4 = bgimage

messagescript5 = """>
<center>
<h1><center><font color=\"red\">"""

messagescript6 = heading

messagescript7 = """<h1></font>
<img src=""" 

messagescript8 = imagelink

messagescript9 = """ width=450px height=340px>


<body onload="init()"></body>
<body>

<div id="bulle"></div>"""

messagescript10 = """
<script language=\"JavaScript\">
var i=0
var j=0
var texteNE, affiche
var texte=\"<br><br><br><br><br><font color="""

messagescript11 = textcolor

messagescript12 = """ size=4>"""

messagescript13 = message 

messagescript14 = """<br><br></font><br></b>\"
var ie = (document.all);
var ne = (document.layers); 
function init(){
texteNE='';
machine_a_ecrire();
}
function machine_a_ecrire(){
texteNE=texteNE+texte.charAt(i)
affiche='<font face=verdana size=1 color=#ffffff><strong>'+texteNE+'</strong></font>'
if (texte.charAt(i)=="<") {
j=1
}
if (texte.charAt(i)==">") {
j=0
}
if (j==0) {
if (document.getElementById) { // avec internet explorer
document.getElementById("bulle").innerHTML = affiche;
}
}
if (i<texte.length-1){
i++
setTimeout("machine_a_ecrire()",70)
}
else
return
}
</script><font face="verdana" size="1"><blink><span style="color: rgb(255, 255, 255);"><b><font color=lime size=4></font></b></u></blink><br></font></b>
</body>
<SCRIPT LANGUAGE=\"JavaScript\">
<!-- Disable
function disableselect(e){
return false
}

function reEnable(){
return true
}

//if IE4+
document.onselectstart=new Function (\"return false\")
document.oncontextmenu=new Function (\"return false\")
//if NS6
if (window.sidebar){
document.onmousedown=disableselect
document.onclick=reEnable
}
//-->
</script>

<!-- DEBUT DU SCRIPT --><style>
.spanstyle {
    position:absolute;
    visibility:visible;
    top:-50px;
    font-size:12pt;
    font-family:Arial;
      font-weight:bold;
    color:#0000FF;
}
</style>


<br>
"""
fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)

print "\nIndex successfully created with the name: index.html"

fo.close()
