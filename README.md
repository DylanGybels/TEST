# Readme

## Project start checklist

1. Clone the project from github using "git clone [github_git_link]"
2. Rename the "Template-rename.PrjPcb" file in the "Altium_Design" folder to the name of the PCB.
3. Open the project in Altium
4. Open the project options by right clicking the project and then clicking on "Project Options..."
5. Go to the "Parameters" tab and fill in the following parameters
- "Designer": The designer(s) of the schematics and PCB. 
- "PcbTitle": The name of the PCB.
- "ProjectTitle": The name of the project the PCB is for.
- "Reviewer": The name(s) of the full reviewer(s) of the project. This can be left blank if the reviewer(s) are not known yet.
- "SchematicReviewer": The name(s) of the schematic reviewer(s) of the project. This can be left blank if the reviewer(s) are not known yet.
- "Version": The current version of the PCB. For a new PCB this is V1.  

Names can be typed in full or with initials. It is advised to use three or four letter initials (ex: Bob the Builder -> BTB, Jan Geuns -> JaGe).  
Multible names can be used by adding a ", " in between them (ex: BTB, JaGe).

6. Click "OK" and save the project.
7. Commit and push to github using "git add *", "git commit -m "Initial commit"" and "git push".
8. Wait for the system to compile the first version of the project. In the meantime you can start designing the schematic of the project. Under the Actions tab in github you can see when the project is running and if it is finished.
9. Pull the generated files from github using "git pull"
10. The system should have generated a checklist, bin folder and an output folder inside the "Altium_Design" folder.
11. Overwrite this readme with a nice overview of your PCB.

## Project design process

During the design of the project a git commit and push can be done at any time. The system will automatically generate all files after every push. Be sure to pull the data from the git once in a while. Only the last push will be uploaded if a second push was done before the first one was handled.  
It is advised to push to the git every evening and pull it back in every morning. This way the documentation inside the git stays up to date and not much data will be lost if your computer breaks.
