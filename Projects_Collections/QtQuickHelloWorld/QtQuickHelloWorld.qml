import QtQuick 2.8
import QtQuick.Window 2.3

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    MouseArea{
    ancohors.fill:parent
    onClicked: {
    console.log(qsTr('Clicked on background. Text:"' + TextEdit.text + '"'))}
    }

    TextEdit {
        id:textEdit
        text:qsTr("Enter some text...")
        verticalAlignment: Text.AlignVCenter
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 20
        Rectangle {
            anchors.fill: parent
            anchors.margins: -10
            color:"transparent"
            border.
        }
    }
}
