@echo off
set manic="C:\Program Files (x86)\ManicTime"
cd %manic%
mtc backup "C:\Users\estudiante.2016\Desktop" /f:"bck.sdf" /o
set sqlcsv="C:\Users\estudiante.2016\Desktop\Scripts"
set datasource="Data Source=C:\Users\estudiante.2016\Desktop\bck.sdf"
set query="select a.ActivityId, a.DisplayName as Event, a.StartLocalTime, a.EndLocalTime, g.DisplayName as Application, t.TypeName as Type from Activity a, [Group] g, Timeline t where a.GroupId = g.GroupId and a.TimelineId = t.TimelineId order by a.ActivityId;"
set output="output.csv"
cd %sqlcsv%
::-hn coloca el header cada n filas, con -h0, el header es eliminado
SqlCeCmd40.exe -d %datasource% -q %query% -h 0 -s "|" -W -o %output%
cd ..
del bck.sdf
