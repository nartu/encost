Sub upload_linux

    Dim strProgramPath As String
    Dim strProgramName As String
    Dim strArgument As String


    strProgramPath = "./dist/"
    strProgramName = "upload"
    strArgument = ThisComponent.getURL()

    rem Msgbox ThisComponent.getURL()

    Shell strProgramPath & strProgramName & " " &  strArgument

End Sub
