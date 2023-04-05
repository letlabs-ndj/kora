import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.2
import QtQuick.Controls.Material 2.15

ApplicationWindow {
    title: qsTr("Test")
    width: Screen.width
    height: Screen.height
    visible: true
    property var temp:"0"
    property var hum:"0"
    property var lum:"0"
    property string air_qual:"00"
    property bool sprinkler:true
    property bool ven:true
    property QtObject gui    
    Material.theme: Material.light
    Material.accent: "#367E18"
    property var datafontSize: 30
    property var controlsfontSize: 15
    property bool pass:false
    property alias actualPage: stack.currentItem
    FontLoader { id: fontello; source: "assets/font/fontello.ttf" }
    

 StackView {
        id: stack
        initialItem: mainView
        anchors.fill: parent
    }
    
    Component{
        id:mainView

        Column{
            Image{
            anchors.fill: parent
            source: "../assets/images/background.png"
            fillMode: Image.PreserveAspectCrop
        }
            
            Row {
                topPadding : 30
                width: parent.width

                    Text{
                        id:time_txt_two
                        text: "TIME"
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        verticalAlignment: Text.AlignVCenter
                        anchors.bottomMargin: 0
                        anchors.rightMargin: parent.width / 2
                        anchors.topMargin: 50
                        anchors.leftMargin: (parent.width / 2) - 80
                        font.pointSize:30
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
                                id:notif
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
                                id:reseau
                                width:15
                                height:15                            
                                color:"transparent"
                                Image{
                                    anchors.fill: parent
                                    source: "../assets/images/reseau.png"
                                    fillMode: Image.PreserveAspectCrop
                                }
                            }

                    }
                }
                
                
                
            }
            
            
            
                    Column{
                        spacing:10
                        topPadding:parent.height/5
                        leftPadding:(parent.width/2) - 50
                        rightPadding:parent.width/2
                        
                        Rectangle{
                            width:100
                            height:100                              
                            color:"transparent"
                            Image{
                                anchors.fill: parent
                                source: "../assets/images/user.png"
                                fillMode: Image.PreserveAspectCrop
                            }
                        }
                        
                        Text{
                            text:"Ma serre"
                            color: "white"
                            font.pointSize:15
                            leftPadding:10
                        }
                        Column{
                            leftPadding:-50
                              TextField {
                                id:user_pass
                                placeholderText: qsTr("     Entrer password")
                                placeholderTextColor: "white"
                                color:"white"
                                font.pointSize:13
                                echoMode: TextInput.Password  
                                onAccepted:{
                                    pass =  gui.login(user_pass.text)  

                                    if (pass){
                                        stack.push(Qt.resolvedUrl("home.qml"));
                                    }else{
                                        console.log("no");
                                        pass_validator.visible = true
                                    }

                                    
                                }                     
                                background: Rectangle {
                                    radius: 8
                                    width:200
                                    height:40
                                    color:"#0A0A0A"
                                    border.color: "Transparent"
                                    opacity:0.5
                                }
                            
                            } 
                            Text{
                                id: pass_validator
                                text:"Mot de passe incorrecte"
                                color: "#EC5757"
                                font.pointSize:10
                                leftPadding:25
                                topPadding:5
                                visible:false
                        }  
                        }
                       
                     }
           Connections{
                target: backend
                function onPrintTime(time){
                    time_txt_two.text = time
                }
            }
    }
}

}

