
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.1
import QtQuick.Controls.Material 2.15
import QtWebSockets 1.0


Item {

    property string currTime:"0"
    Material.theme: Material.light
    Material.accent: "#367E18"
    property string email:""
    property string userTok:""
    
 
    StackView {
        id: home
        initialItem: mainView
        anchors.fill: parent
    }
    
    
    Component{
        id:mainView

        Column{
            Image{
            anchors.fill: parent
            source: "../assets/images/background2.png"
            fillMode: Image.PreserveAspectCrop
        }
            
            Rectangle{
                    anchors.left:parent.left
                    anchors.right:parent.right
                    color:"#0A0A0A"
                    height:40
                    border.color:"transparent"
                    opacity:0.5
            Row {
                spacing: 180
                width: parent.width

                    Text{
                        id:time_txt
                        text: "time"
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        verticalAlignment: Text.AlignVCenter
                        anchors.bottomMargin: 0
                        anchors.rightMargin: parent.width / 2
                        anchors.topMargin: 50
                        anchors.leftMargin: (parent.width / 2) - 50
                        font.pointSize:20
                        color: "white"
                }

                Rectangle{
                     width: 50
                    anchors.right :parent.right
                        Row{
                            spacing: 15
                            leftPadding : -50
                            topPadding : 15 


                        Rectangle{
                                id:notif_two
                                width:20
                                height:20                              
                                color:"transparent"
                                Image{
                                    anchors.fill: parent
                                    source: "../assets/images/notif.png"
                                    fillMode: Image.PreserveAspectCrop
                                }
                            }

                        Rectangle{
                                id:reseau_two
                                width:15
                                height:15                            
                                color:"transparent"
                                Image{
                                    anchors.fill: parent
                                    source: "../assets/images/reseau.png"
                                    fillMode: Image.PreserveAspectCrop
                                }
                            }

                        Component.onCompleted: {
                            socket.active = !socket.active
                        }
                        WebSocket {
                            id: socket
                            url: "ws://koraapi.alwaysdata.net/ws/serre/"+token+"/"
                            onTextMessageReceived: {
                                console.log(message) 
                                 
                                if(message.includes("Serre Connection")){
                                    console.log("SR")
                                    messageDialog.open()
                                }
                                else if(message.includes("Change Propertie")){
                                    console.log("CP")
                                }
                                else{
                                    console.log("none")
                                }  

                                
                            }
                            onStatusChanged: if (socket.status == WebSocket.Error) {
                                                console.log("Error: " + socket.errorString+ "token"+tok)
                                            } else if (socket.status == WebSocket.Open) {
                                                console.log("socket opened")                                                
                                            } else if (socket.status == WebSocket.Closed) {
                                                console.log("Socket closed")
                                            }
                            active: false
                        }
                        

                        Button{
                            id:qr                        
                            font.family: fontello.font.family
                    
                            Rectangle{
                                width:15
                                height:15                              
                                color:"transparent"
                                Image{
                                    anchors.fill: parent
                                    source: "../assets/images/qr.jpg"
                                    fillMode: Image.PreserveAspectCrop
                                }
                            }
                            background: Rectangle {
                                implicitWidth: 20
                                implicitHeight: 20                            
                                border.color: "transparent"
                                color:"transparent"
                                
                            }
                            onClicked: {
                                qrDialog.open()                                
                                }


                            Dialog {
                                id: messageDialog
                                width:400
                                x: -Screen.width/2 - 200
                                y:  Screen.height/6 


                                background:Rectangle {
                                    color: "#100F0F"
                                    height:200
                                    opacity:0.8
                                    radius:10
                                    
                                    
                                
                                Column{
                                    spacing: 15
                                    anchors.fill: parent
                                    topPadding:10
                                    leftPadding:10
                                    
                                    Row{
                                        spacing:10
                                        Text{
                                            text:"\uF0F3"
                                            font.family: fontello.font.family
                                            color:"white"
                                            font.pointSize:15
                                        }
                                        Text{
                                            text:"Authentification"  
                                            color:"white"  
                                            font.pointSize:15                                    
                                        }

                                    }
                                    Label {                              
                                        elide: Label.ElideRight
                                        text: "Une demande de connection vient d’etre faites, entrez 
    votre mots dde passe pour valider la demande"
                                        color:"white"
                                    }
                                    
                                    TextField {
                                        id:distAuth
                                        placeholderText: "Password"
                                        echoMode: TextInput.Password
                                        color:"white"
                                        placeholderTextColor: "white"
                                        width:350
                                        background: Item {
                                            implicitHeight: 40
                                            Rectangle {
                                                color: "white"
                                                height: 3
                                                width: parent.width
                                                anchors.bottom: parent.bottom
                                            }
                                        }
                                        
                                    }

                                    Row{
                                        spacing:10
                                        leftPadding:170
                                        RoundButton {
                                            radius:10 
                                            width:100                                       
                                            highlighted: true
                                            Material.accent: "white"

                                            Text{
                                                leftPadding:25
                                                topPadding:15
                                                text:"Valider"                                    
                                        }
                                            onClicked:{
                                                pass =  gui.login(distAuth.text)
                                                email = gui.getUserEmail()
                                                userTok=gui.getUserTok()  
                                                if (pass){                                                    
                                                    var object = {"type":"Accept Request","user":userTok,"serre":token}
                                                    var json = JSON.stringify(object)
                                                    socket.sendTextMessage(json)
                                                    console.log("Sent JSON:", json)
                                                    
                                                }else{
                                                    var object = {"type":"Refuse Request","user":userTok,"serre":token}
                                                    var json = JSON.stringify(object)
                                                    socket.sendTextMessage(json)
                                                    console.log("Sent JSON:", json)                                                    
                                                    
                                                }
                                                messageDialog.close()
                                                }
                                        }
                                        RoundButton {
                                            id:annuler
                                            radius:10  
                                            width:100                                      
                                            highlighted: true
                                            Material.accent: "#BA1313"
                                            Text{
                                                leftPadding:25
                                                topPadding:15
                                                text:"Annuler"  
                                                color:"white"                                  
                                        }
                                        onClicked: {                                            
                                            messageDialog.close()
                                            }
                                        }

                                    }
                                }
                                }

                            }

                            
                            
                        }
            
                        
                    
                    
                    }
                }
            }

             Connections{
                target: backend
                function onPrintTime(time){
                    time_txt.text = time
                }
                function onDistantUser(email){
                    console.log(email)
                }
            }
        }


    Rectangle{
        anchors.fill: parent
        anchors.topMargin:100
        anchors.leftMargin:20
        anchors.bottomMargin:100
        anchors.rightMargin:20
        color:"#0A0A0A"
        height:200
        width:parent.width
        radius: 50
        border.color:"transparent"
        opacity:0.7

    Dialog{
        id: qrDialog
        width:300
        height:250
        x: Screen.width/3
        y:  Screen.height/6                           
        
        Image{
            anchors.fill: parent
            source: "../assets/images/qr-img.jpg"
            fillMode: Image.PreserveAspectCrop
        }
    }
    Row{
        leftPadding: (parent.width/2) - 320
        topPadding: (parent.height/2)-130
        spacing:parent.width/9
    
    Column{  
        spacing:parent.height/8    
        Row{
            Row{
                spacing:60

                Column{
                    spacing:15
                    Row{
                        spacing:10
                        Text{
                            text: "\uF2C7"
                            font.family: fontawesome.font.family
                            font.pointSize: datafontSize
                            color:"#850000"
                        }

                        Text{
                        id: tem
                        text: temp+" °C"
                        font.pointSize: datafontSize
                        color:"white"
                        }
                        
                    }
                    
                Text{
                    text: "Temperature"
                    font.pointSize:15
                    color:"white"
                }
                }
                Column{
                    spacing:15

                    Row{
                        spacing:10
                        Text{
                            text: "\uE800"
                            font.family: fontellone.font.family
                            font.pointSize: datafontSize
                            color:"#2B3467"
                        }
                        Text{
                            id: humidity
                            text: hum+" %"
                            font.pointSize: datafontSize
                            color:"white"
                        }
                    }
                    
                Text{
                    text: "Humidity"
                    font.pointSize:15
                    color:"white"
                }
                }
                
            }
        }   

        Row{
            spacing:40

            Column{
                spacing:15

                Row{
                    spacing:5
                    Text{
                        text: "\uE801"
                        font.family: fontellone.font.family
                        font.pointSize: datafontSize
                        color:"#F2CD5C"
                    }
                    Text{
                        id: light
                        text: lum+" %"
                        font.pointSize: datafontSize
                        color:"white"
                    }
                }
                
            Text{
                text: "Luminosity"
                font.pointSize:15
                color:"white"
            }
            }
            Column{
                spacing:15

                Row{
                    spacing:10
                    Text{
                        text: "\uE802"
                        font.family: fontello.font.family
                        font.pointSize: datafontSize
                        color:"#90A17D"
                    }
                    Text{
                        id: air
                        text: air_qual+" PPM"
                        font.pointSize: datafontSize
                        color:"white"
                    }
                }
                
            Text{
                text: "Taux CO2"
                font.pointSize:15
                color:"white"
            }
            }
            
        }
     }  

     Column{
        topPadding:15
        spacing:parent.height/8
        Row{
            spacing:18
            Text{
                text: "Ventilateur"
                topPadding : 15
                font.pointSize: controlsfontSize
                color:"white"
            }
            Switch {
                id:vent
                checked:!ven
                onClicked:gui.ventilage(!vent.checked)
            }
        }

        Row{
            spacing:25
            Text{
                text: "Arroseur"
                topPadding : 15
                font.pointSize:controlsfontSize
                color:"white"
            }
            Switch {
                id:arro
                checked:!sprinkler
                onClicked:gui.arrosage(!arro.checked)
            }
        }
        
        Row{
            spacing:25
            Text{
                text: "Eclairage"
                topPadding : 10
                font.pointSize: controlsfontSize
                color:"white"
            }
	
	 Switch {
		id:am
                checked:!ampoule
                onClicked:gui.eclairage(!am.checked)
            }

                       
        }
     }
    }
    }
}
    
}
}

