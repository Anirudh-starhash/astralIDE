<template>
    <div>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <div>
<<<<<<< HEAD
            <nav class="navbar navbar-default" style="background-color: #cbd5e1; height:60%;">
                <div class="container-fluid">
                    <div class="navbar-header">
                        <a @click="backtoHome" style="color: blue;">
=======
            <nav class="navbar navbar-default" style="background-color: aliceblue; height:60%;">
                <div class="container-fluid">
                    <div class="navbar-header">
                        <a class="navbar-brand"  style="color: darkblue;" href="#">Code Editor</a>
                    </div>
                    <div class="content">
                        <a href="#" style="color: blue;">
>>>>>>> 1f3b79616d5c59c5ea3203507e0ca135777e9f16
                            <svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-house-add-fill x blue" viewBox="0 0 16 16">
                                <path d="M12.5 16a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7m.5-5v1h1a.5.5 0 0 1 0 1h-1v1a.5.5 0 1 1-1 0v-1h-1a.5.5 0 1 1 0-1h1v-1a.5.5 0 0 1 1 0"/>
                                <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293z"/>
                                <path d="m8 3.293 4.712 4.712A4.5 4.5 0 0 0 8.758 15H3.5A1.5 1.5 0 0 1 2 13.5V9.293z"/>
                            </svg>
                            <p class="black">Home</p>
                        </a>
                        
<<<<<<< HEAD
                        <a @click="Fileoptions" class="dropdown">
=======
                        <a href="#">
>>>>>>> 1f3b79616d5c59c5ea3203507e0ca135777e9f16
                            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-archive-fill x blue" viewBox="0 0 16 16">
                                <path d="M12.643 15C13.979 15 15 13.845 15 12.5V5H1v7.5C1 13.845 2.021 15 3.357 15zM5.5 7h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1 0-1M.8 1a.8.8 0 0 0-.8.8V3a.8.8 0 0 0 .8.8h14.4A.8.8 0 0 0 16 3V1.8a.8.8 0 0 0-.8-.8z"/>
                            </svg>
                            <p class="black">File</p>
                        </a>
<<<<<<< HEAD
                        <div v-if="isFilePopupVisible" class="dropdown-menu">
                            <a class="dropdown-item" @click="optionSelected('New Text File')">
                                <div class="mcontent">
                                    <div>New Text File</div>
                                    <div>Ctrl+N</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('New File')">
                                <div class="mcontent">
                                    <div>New File</div>
                                    <div>Ctrl+Alt+Windows+N</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('New Window')">
                                <div class="mcontent">
                                    <div>New Window</div>
                                    <div>Ctrl+Shift+N</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Open File...')">
                                <div class="mcontent">
                                    <div>Open File</div>
                                    <div>Ctrl+O</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Open Folder...')">
                                <div class="mcontent">
                                    <div>Open Folder</div>
                                    <div>Ctrl+K Ctrl+O</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Open Workspace from File..')">Open Workspace from File..</a>
                            <a class="dropdown-item" @click="optionSelected('Open Recent')">
                                <div class="mcontent">
                                    <div>Open Recent</div>
                                    <div>></div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Add Folder to Workspace')">Add Folder to Workspace</a>
                            <a class="dropdown-item" @click="optionSelected('Save Workspace as..')">Save Workspace as</a>
                            <a class="dropdown-item" @click="optionSelected('Duplicate Workspace')">Duplicate Workspace</a>
                            <a class="dropdown-item" @click="optionSelected('Save')">
                                <div class="mcontent">
                                    <div>Save</div>
                                    <div>Ctrl+S</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Save as')">
                                <div class="mcontent">
                                    <div>Save as</div>
                                    <div>Ctrl+Shift+S</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Save All')">
                                <div class="mcontent">
                                    <div>Save All</div>
                                    <div>Ctrl+K S</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Share')">
                                <div class="mcontent">
                                    <div>Share</div>
                                    <div>></div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Auto Save')">Auto Save</a>
                            <a class="dropdown-item" @click="optionSelected('Prefrences')">
                                <div class="mcontent">
                                    <div>Preferences</div>
                                    <div>></div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Revert File')">Revert File</a>
                            <a class="dropdown-item" @click="optionSelected('Close Editor')">
                                <div class="mcontent">
                                    <div>Close Editor</div>
                                    <div>Ctrl+F4</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Close Folder')">
                                <div class="mcontent">
                                    <div>Close Folder</div>
                                    <div>Ctrl+K F</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Close Window')">
                                <div class="mcontent">
                                    <div>Close Window</div>
                                    <div>Alt+F4</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Exit')">Exit</a>
                        </div>
                        
                        <a @click="Editoptions" class="dropdown">
=======
                        
                        <a href="#" style="color: blue;">
>>>>>>> 1f3b79616d5c59c5ea3203507e0ca135777e9f16
                            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-credit-card x blue" viewBox="0 0 16 16">
                                <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v1h14V4a1 1 0 0 0-1-1zm13 4H1v5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1z"/>
                                <path d="M2 10a1 1 0 0 1 1-1h1a1 1 0 0 1 1 1v1a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1z"/>
                              </svg>
                            <p class="black">Edit</p>
                        </a>
<<<<<<< HEAD

                        <div v-if="isEditPopupVisible" class="dropdown-menu">
                            <a class="dropdown-item" @click="optionSelected('Undo')">
                                <div class="mcontent">
                                    <div>Undo</div>
                                    <div>Ctrl+Z</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Redo')">
                                <div class="mcontent">
                                    <div>Redo</div>
                                    <div>Ctrl+Y</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Cut')">
                                <div class="mcontent">
                                    <div>Cut</div>
                                    <div>Ctrl+X</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Copy')">
                                <div class="mcontent">
                                    <div>Copy</div>
                                    <div>Ctrl+C</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Paste')">
                                <div class="mcontent">
                                    <div>Paste</div>
                                    <div>Ctrl+V</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Find')">
                                <div class="mcontent">
                                    <div>Find</div>
                                    <div>Ctrl+F</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Replace')">
                                <div class="mcontent">
                                    <div>Replace</div>
                                    <div>Ctrl+H</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Find in Files')">
                                <div class="mcontent">
                                    <div>Find in Files</div>
                                    <div>Ctrl+Shift+F</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Replace in Files')">
                                <div class="mcontent">
                                    <div>Replace in Files</div>
                                    <div>Ctrl+Shift+H</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Toggle Line Comment')">
                                <div class="mcontent">
                                    <div>Toggle Line Comment</div>
                                    <div>Ctrl+/</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Toggle Block Comment')">
                                <div class="mcontent">
                                    <div>Toggle Block Comment</div>
                                    <div>Shift+Alt+A</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Emmet Expand Abbreviation')">
                                <div class="mcontent">
                                    <div>Emmet Expand Abbreviation</div>
                                    <div>Tab</div>
                                </div>
                            </a>
                        </div>
                        
                        <a @click="Selectionoptions" class="dropdown">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-check2-circle x blue" viewBox="0 0 16 16">
                                <path d="M2.5 8a5.5 5.5 0 0 1 8.25-4.764.5.5 0 0 0 .5-.866A6.5 6.5 0 1 0 14.5 8a.5.5 0 0 0-1 0 5.5 5.5 0 1 1-11 0"/>
                                <path d="M15.354 3.354a.5.5 0 0 0-.708-.708L8 9.293 5.354 6.646a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0z"/>
                            </svg>
                            <p class="black">Selection</p>
                        </a>
                        <div v-if="isSelectionPopupVisible" class="dropdown-menu">
                            <a class="dropdown-item" @click="optionSelected('Select All')">
                                <div class="mcontent">
                                    <div>Select All</div>
                                    <div>Ctrl+A</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Expand Selection')">
                                <div class="mcontent">
                                    <div>Expand Selection</div>
                                    <div>Shift+Alt+RightArrow</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Shrink Selection')">
                                <div class="mcontent">
                                    <div>Shrink Selection</div>
                                    <div>Shift+Alt+LeftArrow</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Copy Line Up')">
                                <div class="mcontent">
                                    <div>Copy Line Up</div>
                                    <div>Shift+Alt+UpArrow</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Copy Line Down')">
                                <div class="mcontent">
                                    <div>Copy Line Down</div>
                                    <div>Shift+Alt+DownArrow</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Move Line Up')">
                                <div class="mcontent">
                                    <div>Move Line Up</div>
                                    <div>Alt+UpArrow</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Move Line Down')">
                                <div class="mcontent">
                                    <div>Move Line Down</div>
                                    <div>Alt+DownArrow</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Duplicate Selection')">Duplicate Selection</a>
                            <a class="dropdown-item" @click="optionSelected('Add Cursor Above')">
                                <div class="mcontent">
                                    <div>Add Cursor Above</div>
                                    <div>Ctrl+Alt+UpArrow</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Add Cursor Below')">
                                <div class="mcontent">
                                    <div>Add Cursor Below</div>
                                    <div>Ctrl+Alt+DownArrow</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Add Cursor to Line Ends')">
                                <div class="mcontent">
                                    <div>Add Cursor to Line Ends</div>
                                    <div>Shift+Alt+I</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Add Next Occurrence')">
                                <div class="mcontent">
                                    <div>Add Next Occurence</div>
                                    <div>Ctrl+D</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Add Previous Occurrence')">Add Previous Occurrence</a>
                            <a class="dropdown-item" @click="optionSelected('Select All Occurrence')">
                                <div class="mcontent">
                                    <div>Select All Occurrence</div>
                                    <div>Ctrl+Shift+L</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Switch to Ctrl+Click for Multi Cursor')">Switch to Ctrl+Click for Multi Cursor</a>
                            <a class="dropdown-item" @click="optionSelected('Column Selection Mode')">Column Selection Mode</a>
                            
                        </div>

                        <a @click="Viewoptions" class="dropdown">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-view-list x blueb" viewBox="0 0 16 16">
                                <path d="M3 4.5h10a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2m0 1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1zM1 2a.5.5 0 0 1 .5-.5h13a.5.5 0 0 1 0 1h-13A.5.5 0 0 1 1 2m0 12a.5.5 0 0 1 .5-.5h13a.5.5 0 0 1 0 1h-13A.5.5 0 0 1 1 14"/>
                            </svg>
                            <p class="black">View</p>
                        </a>
                        <div v-if="isViewPopupVisible" class="dropdown-menu">
                            <a class="dropdown-item" @click="optionSelected('Command Palette...')">
                                <div class="mcontent">
                                    <div>Command Palette..</div>
                                    <div>Ctrl+Shift+P</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Open View')">Open View</a>
                            <a class="dropdown-item" @click="optionSelected('Apperance')">
                                <div class="mcontent">
                                    <div>Apperance</div>
                                    <div>></div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Editor Layout')">
                                <div class="mcontent">
                                    <div>Editor Layout</div>
                                    <div>></div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Explorer')">
                                <div class="mcontent">
                                    <div>Explorer</div>
                                    <div>Ctrl+Shift+E</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Search')">
                                <div class="mcontent">
                                    <div>Search</div>
                                    <div>Ctrl+Shift+F</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Source Control')">
                                <div class="mcontent">
                                    <div>Source Control</div>
                                    <div>Ctrl+Shift+G G</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Run')">
                                <div class="mcontent">
                                    <div>Run</div>
                                    <div>Ctrl+Shift+D</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Extensions')">
                                <div class="mcontent">
                                    <div>Extensions</div>
                                    <div>Ctrl+Shift+X</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Problems')">
                                <div class="mcontent">
                                    <div>Problems</div>
                                    <div>Ctrl+Shift+M</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Output')">
                                <div class="mcontent">
                                    <div>Output</div>
                                    <div>Ctrl+Shift+U</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Debug Console')">
                                <div class="mcontent">
                                    <div>Debug Console</div>
                                    <div>Ctrl+Shift+Y</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Terminal')">
                                <div class="mcontent">
                                    <div>Terminal</div>
                                    <div>Ctrl+~</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Word Wrap')">
                                <div class="mcontent">
                                    <div>Word Wrap</div>
                                    <div>Alt+Z</div>
                                </div>
                            </a>
                            
                        </div>
                        <a @click="Gooptions" class="dropdown">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-tags-fill x blue" viewBox="0 0 16 16">
                                <path d="M2 2a1 1 0 0 1 1-1h4.586a1 1 0 0 1 .707.293l7 7a1 1 0 0 1 0 1.414l-4.586 4.586a1 1 0 0 1-1.414 0l-7-7A1 1 0 0 1 2 6.586zm3.5 4a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3"/>
                                <path d="M1.293 7.793A1 1 0 0 1 1 7.086V2a1 1 0 0 0-1 1v4.586a1 1 0 0 0 .293.707l7 7a1 1 0 0 0 1.414 0l.043-.043z"/>
                            </svg>
                            <p class="black">Go</p>
                        </a>
                        <div v-if="isGoPopupVisible" class="dropdown-menu">
                            <a class="dropdown-item" @click="optionSelected('Back')">
                                <div class="mcontent">
                                    <div>Back</div>
                                    <div>Alt+LeftArrow</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Forward')">
                                <div class="mcontent">
                                    <div>Forward</div>
                                    <div>Alt+RightArrow</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Last Edit Location')">
                                <div class="mcontent">
                                    <div>Last Edit Location</div>
                                    <div>Ctrl+K Ctrl+Q</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Switch Editor')">
                                <div class="mcontent">
                                    <div>Switch Editor</div>
                                    <div>></div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Switch Group')">
                                <div class="mcontent">
                                    <div>Switch Group</div>
                                    <div>></div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Go to File')">
                                <div class="mcontent">
                                    <div>Go to File</div>
                                    <div>Ctrl+E Ctrl+E</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Go to Symbol in Workspace')">
                                <div class="mcontent">
                                    <div>Go to Symbol in Workspace</div>
                                    <div>Ctrl+T</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Go to Symbol in Editor')">
                                <div class="mcontent">
                                    <div>Go to Symbol in Editor</div>
                                    <div>Ctrl+Shift+O</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Go to Definition')">
                                <div class="mcontent">
                                    <div>Go to Definition</div>
                                    <div>F12</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Go to Declaration')">Go to Declaration</a>
                            <a class="dropdown-item" @click="optionSelected('Go to Type Definition')">Go to Type Definition</a>
                            <a class="dropdown-item" @click="optionSelected('Go to Implementations')">
                                <div class="mcontent">
                                    <div>Go to Implementations</div>
                                    <div>Ctrl+F12</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Go to Reference')">
                                <div class="mcontent">
                                    <div>Go to Reference</div>
                                    <div>Shift+F12</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Go to Line/Column')">
                                <div class="mcontent">
                                    <div>Go to Line/Column</div>
                                    <div>Ctrl+G</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Go to Bracket')">
                                <div class="mcontent">
                                    <div>Go to Bracket</div>
                                    <div>Ctrl+Shift+\</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Next Problem')">
                                <div class="mcontent">
                                    <div>Next Problem</div>
                                    <div>F8</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Previous Problem')">
                                <div class="mcontent">
                                    <div>Previous Problem</div>
                                    <div>Shift+F8</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Next Change')">
                                <div class="mcontent">
                                    <div>Next Change</div>
                                    <div>Alt+F3</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Previous Change')">
                                <div class="mcontent">
                                    <div>Previous Change</div>
                                    <div>Shift+Alt+F3</div>
                                </div>
                            </a>
                            
                        </div>

                        <a @click="Runoptions" class="dropdown">
                            <svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-caret-right-fill x blue" viewBox="0 0 16 16">
                                <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                            </svg>
                            <p class="black">Run</p>
                        </a>
                        <div v-if="isRunPopupVisible" class="dropdown-menu">
                            <a class="dropdown-item" @click="optionSelected('Start Debugging')">
                                <div class="mcontent">
                                    <div>Start Debugging</div>
                                    <div>F5</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Run Without Debugging')">
                                <div class="mcontent">
                                    <div>Run Without Debugging</div>
                                    <div>Ctrl+F5</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Stop Debugging')">
                                <div class="mcontent">
                                    <div>Stop Debugging</div>
                                    <div>Shift+F5</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Restart Debugging')">
                                <div class="mcontent">
                                    <div>Restart Debugging</div>
                                    <div>Ctrl+Shift+F5</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Open Configurations')">Open Configurations</a>
                            <a class="dropdown-item" @click="optionSelected('Add Configuration')">Add Configuration</a>
                            <a class="dropdown-item" @click="optionSelected('Step Over')">
                                <div class="mcontent">
                                    <div>Step Over</div>
                                    <div>F10</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Step Into')">
                                <div class="mcontent">
                                    <div>Step Into</div>
                                    <div>F11</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Step Out')">
                                <div class="mcontent">
                                    <div>Step Out</div>
                                    <div>Shift+F11</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Continue')">
                                <div class="mcontent">
                                    <div>Continue</div>
                                    <div>F5</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Toggle Breakpoint')">
                                <div class="mcontent">
                                    <div>Toggle Breakpoint</div>
                                    <div>F9</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('New Breakpoint')">
                                <div class="mcontent">
                                    <div>New Breakpoint</div>
                                    <div>></div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Enable All Breakpoint')">Enable All Breakpoint</a>
                            <a class="dropdown-item" @click="optionSelected('Disable All Breakpoint')">Disable All Breakpoint</a>
                            <a class="dropdown-item" @click="optionSelected('Remove All Breakpoint')">Remove All Breakpoint</a>
                            <a class="dropdown-item" @click="optionSelected('Install Additional Debuggers')">Install Additional Debuggers</a>
                            
                        </div>

                        <a @click="Terminaloptions" class="dropdown">
=======
                        <a href="#" style="color: blue;">
>>>>>>> 1f3b79616d5c59c5ea3203507e0ca135777e9f16
                            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-terminal-fill x blueb" viewBox="0 0 16 16">
                                <path d="M0 3a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm9.5 5.5h-3a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1m-6.354-.354a.5.5 0 1 0 .708.708l2-2a.5.5 0 0 0 0-.708l-2-2a.5.5 0 1 0-.708.708L4.793 6.5z"/>
                            </svg>
                            <p class="black">Terminal</p>
                        </a>
<<<<<<< HEAD
                        <div v-if="isTerminalPopupVisible" class="dropdown-menu">
                            <a class="dropdown-item" @click="optionSelected('New Terminal')">
                                <div class="mcontent">
                                    <div>New Terminal</div>
                                    <div>Ctr+Shift+`</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Split Terminal')">
                                <div class="mcontent">
                                    <div>Split Terminal</div>
                                    <div>Ctr+Shift+S</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Run Task')">Run Task</a>
                            <a class="dropdown-item" @click="optionSelected('Run Build Task')">
                                <div class="mcontent">
                                    <div>Run Build Task</div>
                                    <div>Ctr+Shift+B</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Run Active File')">Run Active File</a>
                            <a class="dropdown-item" @click="optionSelected('Run Selected Text')">Run Selected Text</a>
                            <a class="dropdown-item" @click="optionSelected('Show Running Tasks')">Show Running Tasks</a>
                            <a class="dropdown-item" @click="optionSelected('Restart Running Tasks')">Restart Running Tasks</a>
                            <a class="dropdown-item" @click="optionSelected('Terminate Tasks')">Terminate Tasks</a>
                            <a class="dropdown-item" @click="optionSelected('Configure Tasks')">Configure Tasks</a>
                            <a class="dropdown-item" @click="optionSelected('Configure Default Build Tasks')">Configure Default Build Tasks</a>
                            
                        </div>

                        <a @click="Helpoptions" class="dropdown">
                            <svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-patch-question x blueb" viewBox="0 0 16 16">
                                <path d="M8.05 9.6c.336 0 .504-.24.554-.627.04-.534.198-.815.847-1.26.673-.475 1.049-1.09 1.049-1.986 0-1.325-.92-2.227-2.262-2.227-1.02 0-1.792.492-2.1 1.29A1.7 1.7 0 0 0 6 5.48c0 .393.203.64.545.64.272 0 .455-.147.564-.51.158-.592.525-.915 1.074-.915.61 0 1.03.446 1.03 1.084 0 .563-.208.885-.822 1.325-.619.433-.926.914-.926 1.64v.111c0 .428.208.745.585.745"/>
                                <path d="m10.273 2.513-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911z"/>
                                <path d="M7.001 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0"/>
                            </svg>
                            <p class="black">Help</p>
                        </a>
                        <div v-if="isHelpPopupVisible" class="dropdown-menu">
                            <a class="dropdown-item" @click="optionSelected('Welcome')">Welcome</a>
                            <a class="dropdown-item" @click="optionSelected('Show All Commands')">
                                <div class="mcontent">
                                    <div>Show All Commands</div>
                                    <div>Ctr+Shift+P</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Documentation')">Documentation</a>
                            <a class="dropdown-item" @click="optionSelected('Editor Playground')">Editor Playground</a>
                            <a class="dropdown-item" @click="optionSelected('Show Release Notes')">Show Release Notes</a>
                            <a class="dropdown-item" @click="optionSelected('Keyboard Shortcut Reference')">
                                <div class="mcontent">
                                    <div>KeyBoard ShortCut Reference</div>
                                    <div>Ctr+K Ctrl+R</div>
                                </div>
                            </a>
                            <a class="dropdown-item" @click="optionSelected('Video Tutorials')">Video Tutorials</a>
                            <a class="dropdown-item" @click="optionSelected('Tips/Tricks')">Tips/Tricks</a>
                            <a class="dropdown-item" @click="optionSelected('Join Us on Youtube')">Join Us on Youtube</a>
                            <a class="dropdown-item" @click="optionSelected('Search Feature Requests ')">Search Feature Requests</a>
                            <a class="dropdown-item" @click="optionSelected('Report Issue')">Report Issue</a>
                            <a class="dropdown-item" @click="optionSelected('View License')">View License</a>
                            <a class="dropdown-item" @click="optionSelected('Privacy Statement')">Privacy Statement</a>
                            <a class="dropdown-item" @click="optionSelected('Toggle Developer Tools')">Toggle Developer Tools</a>
                            <a class="dropdown-item" @click="optionSelected('Open Process Explorer')">Open Process Explorer</a>
                            <a class="dropdown-item" @click="optionSelected('Check for Updates')">Check for Updates</a>
                            <a class="dropdown-item" @click="optionSelected('About')">About</a>
                            
                        </div>

                        <a href="">
                            <svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-arrow-left x blue" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
                            </svg>
                            <p class="black">Left</p>
                        </a>
                        <a href="">
                            <svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-arrow-right x blue" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                            <p class="black">Right</p>
                        </a>
                        <a href="">
                            <input type="text" style="width:300px; background-color:darkgrey; text-align:center; color:black; font-weight:bold" value="Search">
                            <p class="black">Seacrh Bar</p>
                        </a>
                    </div>
                    <div class="navbar-right">
                        <a href="#" style="color: blue;">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 52 52" enable-background="new 0 0 52 52" xml:space="preserve" class="x blueb">
                                <path d="M46,8H6c-1.1,0-2,0.9-2,2v32c0,1.1,0.9,2,2,2h40c1.1,0,2-0.9,2-2V10C48,8.9,47.1,8,46,8z M44,40H8V12h36V40z  "/>
                                <path d="M21,38h-9.9c-0.6,0-1-0.4-1-1V15c0-0.6,0.4-1,1-1H21c0.6,0,1,0.4,1,1v22C22,37.6,21.6,38,21,38z"/>
                            </svg>
                            <p class="black">ToggleSideBar</p>
                        </a>
                        <a href="#" style="color: blue;">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="#000000"  viewBox="0 0 52 52" enable-background="new 0 0 52 52" xml:space="preserve" class="x blueb">
                                <path d="M46,8H6c-1.1,0-2,0.9-2,2v32c0,1.1,0.9,2,2,2h40c1.1,0,2-0.9,2-2V10C48,8.9,47.1,8,46,8z M44,40H8V12h36V40z  "/>
                                <path d="M41,26H11.1c-0.6,0-1-0.4-1-1V15c0-0.6,0.4-1,1-1H41c0.6,0,1,0.4,1,1v10C42,25.6,41.6,26,41,26z"/>
                            </svg>
                            <p class="black">TogglePanel</p>
                        </a>
                        <a href="#" style="color: blue;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-grid-1x2-fill x blue" viewBox="0 0 16 16">
                                <path d="M0 1a1 1 0 0 1 1-1h5a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H1a1 1 0 0 1-1-1zm9 0a1 1 0 0 1 1-1h5a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1h-5a1 1 0 0 1-1-1zm0 9a1 1 0 0 1 1-1h5a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1h-5a1 1 0 0 1-1-1z"/>
                            </svg>
                            <p class="black">CustomLayout</p>
                        </a>
                        <a href="#" style="color: blue;">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-dash x blue" viewBox="0 0 16 16">
                                <path d="M4 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 4 8"/>
                            </svg>
                            <p class="black">Minimize</p>
                        </a>
                        <a href="#" style="color: blue;">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-fullscreen x blueb" viewBox="0 0 16 16">
                                <path d="M1.5 1a.5.5 0 0 0-.5.5v4a.5.5 0 0 1-1 0v-4A1.5 1.5 0 0 1 1.5 0h4a.5.5 0 0 1 0 1zM10 .5a.5.5 0 0 1 .5-.5h4A1.5 1.5 0 0 1 16 1.5v4a.5.5 0 0 1-1 0v-4a.5.5 0 0 0-.5-.5h-4a.5.5 0 0 1-.5-.5M.5 10a.5.5 0 0 1 .5.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 1 0 1h-4A1.5 1.5 0 0 1 0 14.5v-4a.5.5 0 0 1 .5-.5m15 0a.5.5 0 0 1 .5.5v4a1.5 1.5 0 0 1-1.5 1.5h-4a.5.5 0 0 1 0-1h4a.5.5 0 0 0 .5-.5v-4a.5.5 0 0 1 .5-.5"/>
                            </svg>
                            <p class="black">Maximize</p>
                        </a>
                        <a @click="logout">
                            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="red" version="1.1" id="Capa_1" viewBox="0 0 220.496 220.496" xml:space="preserve" class="x red">
                                <g>
                                    <g>
                                        <path d="M0.003,192.658c0,7.434,2.897,14.424,8.154,19.684c5.257,5.261,12.25,8.154,19.684,8.154    c7.44,0,14.429-2.894,19.674-8.154l62.732-62.731l62.717,62.72c5.255,5.26,12.244,8.154,19.684,8.154    c7.44,0,14.436-2.895,19.678-8.154c5.255-5.26,8.155-12.25,8.155-19.684s-2.9-14.424-8.155-19.684l-62.714-62.717l62.727-62.727    c5.254-5.257,8.154-12.247,8.154-19.681c0-7.434-2.9-14.427-8.154-19.684C207.084,2.897,200.095,0,192.655,0    c-7.435,0-14.424,2.897-19.678,8.155l-62.724,62.732L47.522,8.155C42.271,2.897,35.281,0,27.847,0    c-7.44,0-14.433,2.897-19.684,8.155c-5.257,5.257-8.155,12.25-8.155,19.684c0,7.434,2.897,14.423,8.155,19.681l62.732,62.727    L8.157,172.974C2.9,178.234,0.003,185.224,0.003,192.658z M16.858,181.681l67.08-67.086c1.156-1.152,1.801-2.714,1.801-4.344    c0-1.631-0.646-3.198-1.801-4.348l-67.08-67.08c-2.939-2.936-4.552-6.836-4.552-10.985c0-4.152,1.618-8.056,4.552-10.989    c2.939-2.933,6.831-4.552,10.989-4.552c4.149,0,8.055,1.619,10.98,4.552l67.079,67.077c2.306,2.306,6.39,2.306,8.695,0    l67.07-67.077c5.867-5.873,16.104-5.861,21.972,0c2.937,2.939,4.552,6.836,4.552,10.989c0,4.149-1.615,8.056-4.552,10.985    l-67.073,67.074c-2.402,2.404-2.402,6.29,0,8.697l67.062,67.056c2.936,2.937,4.545,6.84,4.545,10.989s-1.609,8.053-4.551,10.988    c-5.85,5.867-16.094,5.873-21.966,0l-67.059-67.056c-2.405-2.407-6.29-2.407-8.695,0l-67.085,67.08    c-5.846,5.866-16.09,5.872-21.962,0c-2.939-2.937-4.552-6.84-4.552-10.989C12.307,188.515,13.919,184.612,16.858,181.681z"/>
                                    </g>
                                </g>
                            </svg>
                            <p class="black">Logout</p>
                        </a>
=======
>>>>>>> 1f3b79616d5c59c5ea3203507e0ca135777e9f16
                    </div>
                </div>
            </nav>
        </div>
    </div>
</template>

<script>
<<<<<<< HEAD
import { useRouter } from 'vue-router';
import axios from 'axios'
export default {
    data(){
        return{
            isFilePopupVisible:false,
            isEditPopupVisible:false,
            isSelectionPopupVisible:false,
            isViewPopupVisible:false,
            isGoPopupVisible:false,
            isRunPopupVisible:false,
            isTerminalPopupVisible:false,
            isHelpPopupVisible:false,
        }
    },
    setup(){
        const router=useRouter();
        return {router};
    },
    methods:{
        Fileoptions(){
            this.isFilePopupVisible=!this.isFilePopupVisible
            this.isEditPopupVisible=false
            this.isSelectionPopupVisible=false
            this.isViewPopupVisible=false
            this.isGoPopupVisible=false
            this.isRunPopupVisible=false
            this.isTerminalPopupVisible=false
            this.isHelpPopupVisible=false
            
        },
        Editoptions(){
            this.isEditPopupVisible=!this.isEditPopupVisible
            this.isFilePopupVisible=false
            this.isSelectionPopupVisible=false
            this.isViewPopupVisible=false
            this.isGoPopupVisible=false
            this.isRunPopupVisible=false
            this.isTerminalPopupVisible=false
            this.isHelpPopupVisible=false
        },
        Selectionoptions(){
            this.isSelectionPopupVisible=!this.isSelectionPopupVisible
            this.isEditPopupVisible=false
            this.isFilePopupVisible=false
            this.isViewPopupVisible=false
            this.isGoPopupVisible=false
            this.isRunPopupVisible=false
            this.isTerminalPopupVisible=false
            this.isHelpPopupVisible=false
        },
        Viewoptions(){
            this.isViewPopupVisible=!this.isViewPopupVisible
            this.isEditPopupVisible=false
            this.isSelectionPopupVisible=false
            this.isFilePopupVisible=false
            this.isGoPopupVisible=false
            this.isRunPopupVisible=false
            this.isTerminalPopupVisible=false
            this.isHelpPopupVisible=false
        },
        Gooptions(){
            this.isGoPopupVisible=!this.isGoPopupVisible
            this.isEditPopupVisible=false
            this.isSelectionPopupVisible=false
            this.isViewPopupVisible=false
            this.isFileVisible=false
            this.isRunPopupVisible=false
            this.isTerminalPopupVisible=false
            this.isHelpPopupVisible=false
        },
        Runoptions(){
            this.isRunPopupVisible=!this.isRunPopupVisible
            this.isEditPopupVisible=false
            this.isSelectionPopupVisible=false
            this.isViewPopupVisible=false
            this.isGoPopupVisible=false
            this.isFilePopupVisible=false
            this.isTerminalPopupVisible=false
            this.isHelpPopupVisible=false
        },
        Terminaloptions(){
            this.isTerminalPopupVisible=!this.isTerminalPopupVisible  
            this.isEditPopupVisible=false
            this.isSelectionPopupVisible=false
            this.isViewPopupVisible=false
            this.isGoPopupVisible=false
            this.isRunPopupVisible=false
            this.isFilePopupVisible=false
            this.isHelpPopupVisible=false
        },
        Helpoptions(){
            this.isHelpPopupVisible=!this.isHelpPopupVisible
            this.isEditPopupVisible=false
            this.isSelectionPopupVisible=false
            this.isViewPopupVisible=false
            this.isGoPopupVisible=false
            this.isRunPopupVisible=false
            this.isTerminalPopupVisible=false
            this.isFilePopupVisible=false
        },
        optionSelected(option) {
            console.log(`${option} selected`);
            this.isFilePopupVisible = false;
        },
        backtoHome(){
            this.$router.push("/");
        },
        async logout(){
            const access_token=localStorage.getItem("access_token")
            try{
                const response=await axios.post("http://127.0.0.1:5000/api/user_logout",null,
                    {
                        headers:{
                            Authorization:`Bearer ${access_token}`
                        }
                    }
                );
                if(response.status===200){
                    localStorage.removeItem("access_token");
                    localStorage.removeItem("info");
                    alert('Logged out Successfully!')
                    this.$router.push("/");
                }
                else{
                    alert('Some Error!')
                }
            }catch(error){
                console.log(error)
            }
        }
    }
=======
export default {
    
>>>>>>> 1f3b79616d5c59c5ea3203507e0ca135777e9f16
}
</script>

<style scoped>
<<<<<<< HEAD
  .navbar-header {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-top: 5px;;
  }

  .navbar-right {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap:10px;
    padding-top: 5px;;
    margin-right: 10px;
  }
  .left{
    justify-content: flex-start;
  }
  .right{
    justify-content: flex-end;
  }
  .black{
    color:black;
    font-weight:bold;
    font-size:13px;
=======
  .content{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap:80px;
    padding-top:10px;
  }
  .black{
    color:black;
>>>>>>> 1f3b79616d5c59c5ea3203507e0ca135777e9f16
  }
  .blue{
    color:blue;
    font-size: 20px;;
  }
<<<<<<< HEAD
  .red{
    color:red;
    font-size: 20px;
  }
=======
>>>>>>> 1f3b79616d5c59c5ea3203507e0ca135777e9f16
  .blueb{
    color:black;
    font-size: 20px;;
  }
  .x{
<<<<<<< HEAD
    height:25px;
    width:40px;
  }
  .x:hover{
    transform: translate(10px);
  }
  .navbar-nav > li {
    position: relative;
}

.dropdown-menu {
    display: flex;
    flex-direction: column;
    background-color: darkgray;
    width:30%;
}

.navbar-nav > li:hover .dropdown-menu {
    display: block;
}

.dropdown-item {
    display: block;
    width: 100%;
    padding: 3px 20px;
    clear: both;
    font-weight: 400;
    color: white;
    text-align: inherit;
    white-space: nowrap;
    background: 0 0;
    border: 0;
    font-weight: bold;
}

.dropdown-item:hover {
    color: #262626;
    text-decoration: none;
    background-color: #f5f5f5;
}
.mcontent{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
=======
    height:30px;
    width:40px;
  }
>>>>>>> 1f3b79616d5c59c5ea3203507e0ca135777e9f16
</style>
