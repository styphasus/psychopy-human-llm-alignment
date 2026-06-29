#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on November 20, 2025, at 15:51
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2025.1.1')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from elConnect_2
# DESCRIPTION:
# This is a basic example, which shows how connect to and disconnect from
# the tracker, how to open and close data file, how to start/stop recording,
# and the standard messages for integration with Data Viewer.
# Each trial presents a fixation cross for 0.5 seconds followed by an image
# for 4 seconds.  A keyboard press terminates the trial.

# The code components in the eyelinkSetup, eyelinkStartRecording, trial, and 
# eyelinkStopRecording routines handle communication with the Host PC/EyeLink
# system.  All the code components are set to Code Type Py, and each code 
# component may have code in the various tabs (e.g., Before Experiment, Begin
# Experiment, etc.)

# Last updated: June 26, 2024

# This Before Experiment tab of the elConnect component imports some
# modules we need, manages data filenames, allows for dummy mode configuration
# (for testing), connects to the Host PC, and defines some helper function 
# definitions (which are called later)

import pylink
import time
import platform
from PIL import Image  # for preparing the Host backdrop image
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from string import ascii_letters, digits
from psychopy import gui

# Switch to the script folder
script_path = os.path.dirname(sys.argv[0])
if len(script_path) != 0:
    os.chdir(script_path)

# Set this variable to True if you use the built-in retina screen as your
# primary display device on macOS. If have an external monitor, set this
# variable True if you choose to "Optimize for Built-in Retina Display"
# in the Displays preference settings.
use_retina = False

# Set this variable to True to run the script in "Dummy Mode"
dummy_mode = False

# Set up EDF data file name and local data folder
#
# The EDF data filename should not exceed 8 alphanumeric characters
# use ONLY number 0-9, letters, & _ (underscore) in the filename
edf_fname = 'TEST'

# Prompt user to specify an EDF data filename
# before we open a fullscreen window
dlg_title = "Enter EDF Filename"
dlg_prompt = "Please enter a file name with 8 or fewer characters [letters, numbers, and underscore]."
# loop until we get a valid filename
while True:
    dlg = gui.Dlg(dlg_title)
    dlg.addText(dlg_prompt)
    dlg.addField("Filename", "EDF Filename:","Test")
    # show dialog and wait for OK or Cancel
    ok_data = dlg.show()
    if dlg.OK:  # if ok_data is not None
        print("EDF data filename: {}".format(ok_data["Filename"]))
    else:
        print("user cancelled")
        core.quit()
        sys.exit()

    # get the string entered by the experimenter
    tmp_str = ok_data["Filename"]
    # strip trailing characters, ignore the ".edf" extension
    edf_fname = tmp_str.rstrip().split(".")[0]

    # check if the filename is valid (length <= 8 & no special char)
    allowed_char = ascii_letters + digits + "_"
    if not all([c in allowed_char for c in edf_fname]):
        print("ERROR: Invalid EDF filename")
    elif len(edf_fname) > 8:
        print("ERROR: EDF filename should not exceed 8 characters")
    else:
        break
        
# Set up a folder to store the EDF data files and the associated resources
# e.g., files defining the interest areas used in each trial
results_folder = 'results'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

# We download EDF data file from the EyeLink Host PC to the local hard
# drive at the end of each testing session, here we rename the EDF to
# include session start date/time
time_str = time.strftime("_%Y_%m_%d_%H_%M", time.localtime())
session_identifier = edf_fname + time_str

# create a folder for the current testing session in the "results" folder
session_folder = os.path.join(results_folder, session_identifier)
if not os.path.exists(session_folder):
    os.makedirs(session_folder)

# For macOS users check if they have a retina screen
if 'Darwin' in platform.system():
    dlg = gui.Dlg("Retina Screen?")
    dlg.addText("What type of screen will the experiment run on?")
    dlg.addField("Screen Type", choices=["High Resolution (Retina, 2k, 4k, 5k)", "Standard Resolution (HD or lower)"])
    # show dialog and wait for OK or Cancel
    ok_data = dlg.show()
    if dlg.OK:
        if dlg.data["Screen Type"] == "High Resolution (Retina, 2k, 4k, 5k)":  
            use_retina = True
        else:
            use_retina = False
    else:
        print('user cancelled')
        core.quit()
        sys.exit()

# Step 1: Connect to the EyeLink Host PC
#
# The Host IP address, by default, is "100.1.1.1".
# the "el_tracker" objected created here can be accessed through the Pylink
# Set the Host PC address to "None" (without quotes) to run the script
# in "Dummy Mode"
if dummy_mode:
    el_tracker = pylink.EyeLink(None)
else:
    try:
        el_tracker = pylink.EyeLink("100.1.1.1")
    except RuntimeError as error:
        dlg = gui.Dlg("Dummy Mode?")
        dlg.addText("Couldn't connect to tracker at 100.1.1.1 -- continue in Dummy Mode?")
        # show dialog and wait for OK or Cancel
        ok_data = dlg.show()
        if dlg.OK:  # if ok_data is not None
            dummy_mode = True
            el_tracker = pylink.EyeLink(None)
        else:
            print('user cancelled')
            core.quit()
            sys.exit()

# Define some helper functions for screen drawing 
# and exiting trials/sessions early
def clear_screen(win,genv):
    """ clear up the PsychoPy window"""
    win.fillColor = genv.getBackgroundColor()
    win.flip()

def show_msg(win, genv, text, wait_for_keypress=True):
    """ Show task instructions on screen"""
    scn_width, scn_height = win.size
    msg = visual.TextStim(win, text,
                          color=genv.getForegroundColor(),
                          wrapWidth=scn_width/2)
    clear_screen(win,genv)
    msg.draw()
    win.flip()

    # wait indefinitely, terminates upon any key press
    if wait_for_keypress:
        kb = keyboard.Keyboard()
        #keys = kb.getKeys(['Enter'], waitRelease=False)
        waitKeys = kb.waitKeys(keyList=None, waitRelease=True, clear=True)
        clear_screen(win,genv)

def terminate_task(genv,edf_file,session_folder,session_identifier):
    """ Terminate the task gracefully and retrieve the EDF data file
    """
    el_tracker = pylink.getEYELINK()

    if el_tracker.isConnected():
        # Terminate the current trial first if the task terminated prematurely
        error = el_tracker.isRecording()
        if error == pylink.TRIAL_OK:
            abort_trial()

        # Put tracker in Offline mode
        el_tracker.setOfflineMode()

        # Clear the Host PC screen and wait for 500 ms
        el_tracker.sendCommand('clear_screen 0')
        pylink.msecDelay(500)

        # Close the edf data file on the Host
        el_tracker.closeDataFile()

        # Show a file transfer message on the screen
        msg = 'EDF data is transferring from EyeLink Host PC...'
        show_msg(win, genv, msg, wait_for_keypress=False)

        # Download the EDF data file from the Host PC to a local data folder
        # parameters: source_file_on_the_host, destination_file_on_local_drive
        local_edf = os.path.join(session_folder, session_identifier + '.EDF')
        try:
            el_tracker.receiveDataFile(edf_file, local_edf)
        except RuntimeError as error:
            print('ERROR:', error)

        # Close the link to the tracker.
        el_tracker.close()

    # close the PsychoPy window
    win.close()

    # quit PsychoPy
    core.quit()
    sys.exit()

def abort_trial():
    """Ends recording """
    el_tracker = pylink.getEYELINK()

    # Stop recording
    if el_tracker.isRecording():
        # add 100 ms to catch final trial events
        pylink.pumpDelay(100)
        el_tracker.stopRecording()
        
    # Send a message to clear the Data Viewer screen
    bgcolor_RGB = (128, 128, 128)
    el_tracker.sendMessage('!V CLEAR %d %d %d' % bgcolor_RGB)

    # send a message to mark trial end
    el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_ERROR)

    return pylink.TRIAL_ERROR

# Run 'Before Experiment' code from prompt_code
import sys
import os
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'human-llm-alignment'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '01',
    'session': '01',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Display\\Desktop\\Kim-MT\\human-llm-alignment.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=1,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('ready_2') is None:
        # initialise ready_2
        ready_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ready_2',
        )
    if deviceManager.getDevice('ready_3') is None:
        # initialise ready_3
        ready_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ready_3',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "eyelinkSetup_2" ---
    elInstructions_2 = visual.TextStim(win=win, name='elInstructions_2',
        text='Press any key to start Camera Setup',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=50.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    # Run 'Begin Experiment' code from elConnect_2
    # This Begin Experiment tab of the elConnect component opens the EDF, gets graphic 
    # information from Psychopy, configures some eye tracker settings, logs the screen 
    # resolution for Data Viewer via a DISPLAY_COORDS message, and configures a 
    # graphics environment for eye tracker setup/calibration
    
    el_tracker = pylink.getEYELINK()
    # Step 2: Open an EDF data file on the Host PC
    global edf_fname
    edf_file = edf_fname + ".EDF"
    try:
        el_tracker.openDataFile(edf_file)
    except RuntimeError as err:
        print('ERROR:', err)
        # close the link if we have one open
        if el_tracker.isConnected():
            el_tracker.close()
        core.quit()
        sys.exit()
    
    # Add a header text to the EDF file to identify the current experiment name
    # This is OPTIONAL. If your text starts with "RECORDED BY " it will be
    # available in DataViewer's Inspector window by clicking
    # the EDF session node in the top panel and looking for the "Recorded By:"
    # field in the bottom panel of the Inspector.
    preamble_text = 'RECORDED BY %s' % os.path.basename(__file__)
    el_tracker.sendCommand("add_file_preamble_text '%s'" % preamble_text)
    
    # Step 3: Configure the tracker
    #
    # Put the tracker in offline mode before we change tracking parameters
    el_tracker.setOfflineMode()
    
    # Get the software version:  1-EyeLink I, 2-EyeLink II, 3/4-EyeLink 1000,
    # 5-EyeLink 1000 Plus, 6-Portable DUO
    eyelink_ver = 0  # set version to 0, in case running in Dummy mode
    if not dummy_mode:
        vstr = el_tracker.getTrackerVersionString()
        eyelink_ver = int(vstr.split()[-1].split('.')[0])
        # print out some version info in the shell
        print('Running experiment on %s, version %d' % (vstr, eyelink_ver))
    
    # File and Link data control
    # what eye events to save in the EDF file, include everything by default
    file_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
    # what eye events to make available over the link, include everything by default
    link_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON,FIXUPDATE,INPUT'
    # what sample data to save in the EDF data file and to make available
    # over the link, include the 'HTARGET' flag to save head target sticker
    # data for supported eye trackers
    if eyelink_ver > 3:
        file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,HTARGET,GAZERES,BUTTON,STATUS,INPUT'
        link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,HTARGET,STATUS,INPUT'
    else:
        file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,PUPIL,AREA,GAZERES,BUTTON,STATUS,INPUT'
        link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT'
    el_tracker.sendCommand("file_event_filter = %s" % file_event_flags)
    el_tracker.sendCommand("file_sample_data = %s" % file_sample_flags)
    el_tracker.sendCommand("link_event_filter = %s" % link_event_flags)
    el_tracker.sendCommand("link_sample_data = %s" % link_sample_flags)
    
    # Optional tracking parameters
    # Sample rate, 250, 500, 1000, or 2000, check your tracker specification
    # if eyelink_ver > 2:
    #     el_tracker.sendCommand("sample_rate 1000")
    # Choose a calibration type, H3, HV3, HV5, HV13 (HV = horizontal/vertical),
    el_tracker.sendCommand("calibration_type = HV9")
    # Set a gamepad button to accept calibration/drift check target
    # You need a supported gamepad/button box that is connected to the Host PC
    el_tracker.sendCommand("button_function 5 'accept_target_fixation'")
    
    # get the native screen resolution used by PsychoPy
    scn_width, scn_height = win.size
    # resolution fix for Mac retina displays
    if 'Darwin' in platform.system():
        if use_retina:
            scn_width = int(scn_width/2.0)
            scn_height = int(scn_height/2.0)
    
    # Pass the display pixel coordinates (left, top, right, bottom) to the tracker
    # see the EyeLink Installation Guide, "Customizing Screen Settings"
    el_coords = "screen_pixel_coords = 0 0 %d %d" % (scn_width - 1, scn_height - 1)
    el_tracker.sendCommand(el_coords)
    
    # Write a DISPLAY_COORDS message to the EDF file
    # Data Viewer needs this piece of info for proper visualization, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    dv_coords = "DISPLAY_COORDS  0 0 %d %d" % (scn_width - 1, scn_height - 1)
    el_tracker.sendMessage(dv_coords)  
        
    # Configure a graphics environment (genv) for tracker calibration
    genv = EyeLinkCoreGraphicsPsychoPy(el_tracker, win)
    print(genv)  # print out the version number of the CoreGraphics library
    
    
    # --- Initialize components for Routine "instruction" ---
    taskInstructions_2 = visual.TextStim(win=win, name='taskInstructions_2',
        text='Ready for the experiment?\n\nPress SPACE key to continue',
        font='Courier New',
        pos=(0, 0), draggable=False, height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ready_2 = keyboard.Keyboard(deviceName='ready_2')
    
    # --- Initialize components for Routine "eyelinkStartRecording_2" ---
    
    # --- Initialize components for Routine "TaskRoutine" ---
    Task = visual.TextStim(win=win, name='Task',
        text='Read the following situation and then write what you would say in that situation. \n\nPress SPACE to continue\n',
        font='Courier New',
        pos=(0,0), draggable=False, height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ready_3 = keyboard.Keyboard(deviceName='ready_3')
    
    # --- Initialize components for Routine "PromptRoutine" ---
    ParticipantResponse = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Courier New',
         ori=0.0, pos=(0, -250), draggable=False, units='pix',     letterHeight=30.0,
         size=(500, 200), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='ParticipantResponse',
         depth=0, autoLog=True,
    )
    PromptText = visual.TextStim(win=win, name='PromptText',
        text='',
        font='Courier New',
        pos=(0, 0), draggable=False, height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from prompt_code
    participant_resp = ""
    
    # --- Initialize components for Routine "AIRoutine" ---
    AI_Response = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Courier New',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=30.0,
         size=(500,200), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='AI_Response',
         depth=0, autoLog=True,
    )
    # Run 'Begin Experiment' code from ai_response_code
    from psychopy import core, event, data
    import random, json, time
    import subprocess
    import re
    from datetime import datetime
    text = visual.TextStim(win=win, name='text',
        text='Press SPACE to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "RatingRoutine" ---
    slider = visual.Slider(win=win, name='slider',
        startValue=50, size=(1000,80), pos=(0, -150), units='pix',
        labels=("Strongly disagree","Strongly agree"), ticks=(0,100), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=20.0,
        flip=False, ori=0.0, depth=0, readOnly=False)
    # Run 'Begin Experiment' code from slider_code
    from psychopy import event
    
    rating_text = visual.TextStim(win=win, name='rating_text',
        text='The LLM answer was aligned with my own answer for this scenario.',
        font='Courier New',
        units='pix', pos=(0,0), draggable=False, height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "PauseRoutine" ---
    Pause = visual.TextStim(win=win, name='Pause',
        text='Do you need a break?\n\nIf yes, do not press anything.\n\nIf not, press SPACE to continue',
        font='Courier New',
        pos=(0, 0), draggable=False, height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from savePauseTime
    from psychopy import event
    
    # --- Initialize components for Routine "eyelinkStopRecording_2" ---
    
    # --- Initialize components for Routine "thanks" ---
    endScreen = visual.TextStim(win=win, name='endScreen',
        text='This is the end of the experiment.\n\nThanks!',
        font='Arial',
        pos=(0, 0), draggable=False, height=50.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "eyelinkSetup_2" ---
    # create an object to store info about Routine eyelinkSetup_2
    eyelinkSetup_2 = data.Routine(
        name='eyelinkSetup_2',
        components=[elInstructions_2, key_resp_2],
    )
    eyelinkSetup_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # Run 'Begin Routine' code from saveBeginSetupTime_2
    import time
    thisExp.addData("el_setup.started_Unix", time.time())
    # store start times for eyelinkSetup_2
    eyelinkSetup_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    eyelinkSetup_2.tStart = globalClock.getTime(format='float')
    eyelinkSetup_2.status = STARTED
    thisExp.addData('eyelinkSetup_2.started', eyelinkSetup_2.tStart)
    eyelinkSetup_2.maxDuration = None
    # keep track of which components have finished
    eyelinkSetup_2Components = eyelinkSetup_2.components
    for thisComponent in eyelinkSetup_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "eyelinkSetup_2" ---
    eyelinkSetup_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *elInstructions_2* updates
        
        # if elInstructions_2 is starting this frame...
        if elInstructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            elInstructions_2.frameNStart = frameN  # exact frame index
            elInstructions_2.tStart = t  # local t and not account for scr refresh
            elInstructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(elInstructions_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'elInstructions_2.started')
            # update status
            elInstructions_2.status = STARTED
            elInstructions_2.setAutoDraw(True)
        
        # if elInstructions_2 is active this frame...
        if elInstructions_2.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=["space"], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=eyelinkSetup_2,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            eyelinkSetup_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eyelinkSetup_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eyelinkSetup_2" ---
    for thisComponent in eyelinkSetup_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for eyelinkSetup_2
    eyelinkSetup_2.tStop = globalClock.getTime(format='float')
    eyelinkSetup_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('eyelinkSetup_2.stopped', eyelinkSetup_2.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    # Run 'End Routine' code from elConnect_2
    # This End Routine tab of the elConnect component configures some
    # graphics options for calibration, and then performs a camera setup
    # so that you can set up the eye tracker and calibrate/validate the participant
    
    # Set background and foreground colors for the calibration target
    # in PsychoPy, (-1, -1, -1)=black, (1, 1, 1)=white, (0, 0, 0)=mid-gray
    foreground_color = (-1, -1, -1)
    background_color = tuple(win.color)
    genv.setCalibrationColors(foreground_color, background_color)
    
    # Set up the calibration target
    #
    # The target could be a "circle" (default), a "picture", a "movie" clip,
    # or a rotating "spiral". To configure the type of calibration target, set
    # genv.setTargetType to "circle", "picture", "movie", or "spiral", e.g.,
    # genv.setTargetType('picture')
    #
    # Use genv.setMovieTarget() to set a "movie" target
    # genv.setMovieTarget(os.path.join('videos', 'calibVid.mov'))
    
    # Use a picture as the calibration target
    genv.setTargetType('picture')
    genv.setPictureTarget(os.path.join('images', 'fixTarget.bmp'))
    
    # Configure the size of the calibration target (in pixels)
    # this option applies only to "circle" and "spiral" targets
    # genv.setTargetSize(24)
    
    # Beeps to play during calibration, validation and drift correction
    # parameters: target, good, error
    #     target -- sound to play when target moves
    #     good -- sound to play on successful operation
    #     error -- sound to play on failure or interruption
    # Each parameter could be ''--default sound, 'off'--no sound, or a wav file
    genv.setCalibrationSounds('', '', '')
    
    # resolution fix for macOS retina display issues
    if use_retina:
        genv.fixMacRetinaDisplay()
    
    #clear the screen before we begin Camera Setup mode
    clear_screen(win,genv)
    
    # Request Pylink to use the PsychoPy window we opened above for calibration
    pylink.openGraphicsEx(genv)
    
    # Peform a Camera Setup (eye tracker calibration)
    # skip this step if running the script in Dummy Mode
    if not dummy_mode:
        try:
            el_tracker.doTrackerSetup()
        except RuntimeError as err:
            print('ERROR:', err)
            el_tracker.exitCalibration()
    clear_screen(win,genv)
    
    # Run 'End Routine' code from saveBeginSetupTime_2
    import time
    thisExp.addData("el_recording.stopped_Unix", time.time())
    thisExp.nextEntry()
    # the Routine "eyelinkSetup_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction" ---
    # create an object to store info about Routine instruction
    instruction = data.Routine(
        name='instruction',
        components=[taskInstructions_2, ready_2],
    )
    instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for ready_2
    ready_2.keys = []
    ready_2.rt = []
    _ready_2_allKeys = []
    # Run 'Begin Routine' code from saveInstructTime_2
    import time
    import psychopy.visual
    thisExp.addData("instructions.started_Unix", time.time())
    #window = psychopy.visual.Window()
    win.getMovieFrame();
    # store start times for instruction
    instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction.tStart = globalClock.getTime(format='float')
    instruction.status = STARTED
    thisExp.addData('instruction.started', instruction.tStart)
    instruction.maxDuration = None
    win.color = [-1.0000, -1.0000, -1.0000]
    win.colorSpace = 'rgb'
    win.backgroundImage = ''
    win.backgroundFit = 'none'
    # keep track of which components have finished
    instructionComponents = instruction.components
    for thisComponent in instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction" ---
    instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *taskInstructions_2* updates
        
        # if taskInstructions_2 is starting this frame...
        if taskInstructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskInstructions_2.frameNStart = frameN  # exact frame index
            taskInstructions_2.tStart = t  # local t and not account for scr refresh
            taskInstructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskInstructions_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'taskInstructions_2.started')
            # update status
            taskInstructions_2.status = STARTED
            taskInstructions_2.setAutoDraw(True)
        
        # if taskInstructions_2 is active this frame...
        if taskInstructions_2.status == STARTED:
            # update params
            pass
        
        # *ready_2* updates
        waitOnFlip = False
        
        # if ready_2 is starting this frame...
        if ready_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ready_2.frameNStart = frameN  # exact frame index
            ready_2.tStart = t  # local t and not account for scr refresh
            ready_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ready_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ready_2.started')
            # update status
            ready_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ready_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ready_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ready_2.status == STARTED and not waitOnFlip:
            theseKeys = ready_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _ready_2_allKeys.extend(theseKeys)
            if len(_ready_2_allKeys):
                ready_2.keys = _ready_2_allKeys[-1].name  # just the last key pressed
                ready_2.rt = _ready_2_allKeys[-1].rt
                ready_2.duration = _ready_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instruction,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction" ---
    for thisComponent in instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction
    instruction.tStop = globalClock.getTime(format='float')
    instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction.stopped', instruction.tStop)
    setupWindow(expInfo=expInfo, win=win)
    # Run 'End Routine' code from saveInstructTime_2
    import time
    thisExp.addData("instructions.stopped_Unix", time.time())
    thisExp.nextEntry()
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "eyelinkStartRecording_2" ---
    # create an object to store info about Routine eyelinkStartRecording_2
    eyelinkStartRecording_2 = data.Routine(
        name='eyelinkStartRecording_2',
        components=[],
    )
    eyelinkStartRecording_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from elStartRecord_2
    # This Begin Routine tab of the elStartRecord component draws some feedback 
    # graphics (image and a simple shape) on the Host PC, sends a trial start 
    # message to the EDF, performs drift check/drift correct, and starts eye tracker 
    # recording
    
    # get a reference to the currently active EyeLink connection
    el_tracker = pylink.getEYELINK()
    
    # put the tracker in the offline mode first
    el_tracker.setOfflineMode()
    
    # clear the host screen before we draw the backdrop
    el_tracker.sendCommand('clear_screen 0')
    # imagesAndComponentsStringList value = ['trialImage,image']
    # imagesAndComponentsList value = [['trialImage', 'image']]
    # imagesAndComponentsListString value = [[trialImage, image]]
    # Send image components to the Host PC backdrop to serve as landmarks during recording
    # The method bitmapBackdrop() requires a step of converting the
    # image pixels into a recognizable format by the Host PC.
    # pixels = [line1, ...lineH], line = [pix1,...pixW], pix=(R,G,B)
    # the bitmapBackdrop() command takes time to return, not recommended
    # for tasks where the ITI matters, e.g., in an event-related fMRI task
    # parameters: width, height, pixel, crop_x, crop_y,
    #             crop_width, crop_height, x, y on the Host, drawing options
    # get the array of blank pixels where each pixel corresponds to win.color
    # pixels = blankHostPixels[::]
    
    # Make a list of image components to be transferred
    # Each item in the list should itself be a list, where the first item is
    # the name of the image file to be transferred and the second
    # is the name of the component handling the presentation of the image
    # imagesAndComponentsListForHostBackdrop = [[targetImage_file+"target.png", image]]
    # go through each image and replace the pixels in the blank array with the image pixels
    # for thisImageFileComponentPair in imagesAndComponentsListForHostBackdrop:
    #    thisImageFile = thisImageFileComponentPair[0]
    #    thisImageComponent = thisImageFileComponentPair[1]
    #    thisImageComponent.setImage(thisImageFile)
    #    if "Image" in str(thisImageComponent.__class__):
    #        # Use the code commented below to convert the image and send the backdrop
    #        im = Image.open(script_path + "/" + thisImageFile)
    #        thisImageComponent.elPos = eyelink_pos(thisImageComponent.pos,[scn_width,scn_height])
    #        thisImageComponent.elSize = eyelink_size(thisImageComponent.size,[scn_width,scn_height])
    #        imWidth = int(round(thisImageComponent.elSize[0]))
    #        imHeight = int(round(thisImageComponent.elSize[1]))
    #        imLeft = int(round(thisImageComponent.elPos[0]-thisImageComponent.elSize[0]/2))
    #        imTop = int(round(thisImageComponent.elPos[1]-thisImageComponent.elSize[1]/2))
    #        im = im.resize((imWidth,imHeight))
            # Access the pixel data of the image
    #        img_pixels = list(im.getdata())
            # Check to see if the image goes off the screen
            # If so, adjust the coordinates appropriately
    #        if imLeft < 0:
    #            imTransferLeft = 0
    #        else:
    #            imTransferLeft = imLeft
    #        if imTop < 0:
    #            imTransferTop = 0
    #        else:
    #            imTransferTop = imTop
    #        if imLeft + imWidth > scn_width:
    #            imTransferRight = scn_width
    #        else:
    #            imTransferRight = imLeft+imWidth
    #        if imTop + imHeight > scn_height:
    #            imTransferBottom = scn_height
    #        else:
    #            imTransferBottom = imTop+imHeight    
    #        imTransferImageLineStartX = imTransferLeft-imLeft
    #        imTransferImageLineEndX = imTransferRight-imTransferLeft+imTransferImageLineStartX
    #        imTransferImageLineStartY = imTransferTop-imTop
    #        for y in range(imTransferBottom-imTransferTop):
    #            pixels[imTransferTop+y][imTransferLeft:imTransferRight] = \
    #                img_pixels[(imTransferImageLineStartY + y)*imWidth+imTransferImageLineStartX:\
    #                (imTransferImageLineStartY + y)*imWidth + imTransferImageLineEndX]
    #    else:
    #        print("WARNING: Image Transfer Not Supported For non-Image Component %s)" % str(thisComponent.__class__))
    # transfer the full-screen pixel array to the Host PC
    #el_tracker.bitmapBackdrop(scn_width,scn_height, pixels,\
    #    0, 0, scn_width, scn_height, 0, 0, pylink.BX_MAXCONTRAST)
    
    # OPTIONAL: draw landmarks and texts on the Host screen
    # In addition to backdrop image, You may draw simples on the Host PC to use
    # as landmarks. For illustration purposes, here we draw a box
    # For a list of supported draw commands, see the "COMMANDS.INI" file on the
    # Host PC (under /elcl/exe)
    left = int(scn_width/2.0) - 60
    top = int(scn_height/2.0) - 60
    right = int(scn_width/2.0) + 60
    bottom = int(scn_height/2.0) + 60
    draw_cmd = 'draw_filled_box %d %d %d %d 1' % (left, top, right, bottom)
    el_tracker.sendCommand(draw_cmd)
    
    # send a "TRIALID" message to mark the start of a trial, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    trial_index = 0
    el_tracker.sendMessage('TRIALID %d' % trial_index)
    
    # record_status_message : show some info on the Host PC
    # here we show how many trial has been tested
    status_msg = 'TRIAL number %d' % trial_index
    el_tracker.sendCommand("record_status_message '%s'" % status_msg)
    
    # drift check
    # we recommend drift-check at the beginning of each trial
    # the doDriftCorrect() function requires target position in integers
    # the last two arguments:
    # draw_target (1-default, 0-draw the target then call doDriftCorrect)
    # allow_setup (1-press ESCAPE to recalibrate, 0-not allowed)
    # Skip drift-check if running the script in Dummy Mode
    # --- Drift correction ---
    if not dummy_mode:
        if not el_tracker.isConnected() or el_tracker.breakPressed():
            terminate_task(genv, edf_file, session_folder, session_identifier)
    
        el_tracker.setOfflineMode()
        pylink.pumpDelay(50)
    
        try:
            error = el_tracker.doDriftCorrect(
                int(scn_width/2.0),
                int(scn_height/2.0),
                1,  # draw_target
                1   # allow_setup
            )
            # Check result
            if error in [pylink.ESC_KEY, pylink.TERMINATE_KEY]:
                print("Drift correction cancelled — restarting calibration.")
                el_tracker.doTrackerSetup()
            else:
                print("Drift correction successful.")
        except Exception as e:
            print("Drift correction failed:", e)
    else:
        print("Dummy mode: skipping drift correction.")
    
    
    # put tracker in idle/offline mode before recording
    el_tracker.setOfflineMode()
    
    # Start recording
    try:
        el_tracker.startRecording(1, 1, 1, 1)
        pylink.pumpDelay(100)
        print("Recording started.")
        continueRoutine = False
        print("continueRoutine set to False")
        routineTimer.reset()
    except Exception as e:
        print("Start recording failed:", e)
        abort_trial()
    
    # Allow PsychoPy to move on
    # continueRoutine = False
    # Run 'Begin Routine' code from saveRecordStartTime_2
    import time
    thisExp.addData("el_recording.started_Unix", time.time())
    # store start times for eyelinkStartRecording_2
    eyelinkStartRecording_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    eyelinkStartRecording_2.tStart = globalClock.getTime(format='float')
    eyelinkStartRecording_2.status = STARTED
    thisExp.addData('eyelinkStartRecording_2.started', eyelinkStartRecording_2.tStart)
    eyelinkStartRecording_2.maxDuration = None
    # keep track of which components have finished
    eyelinkStartRecording_2Components = eyelinkStartRecording_2.components
    for thisComponent in eyelinkStartRecording_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "eyelinkStartRecording_2" ---
    eyelinkStartRecording_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=eyelinkStartRecording_2,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            eyelinkStartRecording_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eyelinkStartRecording_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eyelinkStartRecording_2" ---
    for thisComponent in eyelinkStartRecording_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for eyelinkStartRecording_2
    eyelinkStartRecording_2.tStop = globalClock.getTime(format='float')
    eyelinkStartRecording_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('eyelinkStartRecording_2.stopped', eyelinkStartRecording_2.tStop)
    # Run 'End Routine' code from saveRecordStartTime_2
    import time
    thisExp.addData("el_recording.stopped_Unix", time.time())
    thisExp.nextEntry()
    # the Routine "eyelinkStartRecording_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ScenarioLoop = data.TrialHandler2(
        name='ScenarioLoop',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('scenarios.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(ScenarioLoop)  # add the loop to the experiment
    thisScenarioLoop = ScenarioLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisScenarioLoop.rgb)
    if thisScenarioLoop != None:
        for paramName in thisScenarioLoop:
            globals()[paramName] = thisScenarioLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisScenarioLoop in ScenarioLoop:
        ScenarioLoop.status = STARTED
        if hasattr(thisScenarioLoop, 'status'):
            thisScenarioLoop.status = STARTED
        currentLoop = ScenarioLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisScenarioLoop.rgb)
        if thisScenarioLoop != None:
            for paramName in thisScenarioLoop:
                globals()[paramName] = thisScenarioLoop[paramName]
        
        # --- Prepare to start Routine "TaskRoutine" ---
        # create an object to store info about Routine TaskRoutine
        TaskRoutine = data.Routine(
            name='TaskRoutine',
            components=[Task, ready_3],
        )
        TaskRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for ready_3
        ready_3.keys = []
        ready_3.rt = []
        _ready_3_allKeys = []
        # Run 'Begin Routine' code from saveTaskTime
        import time
        import psychopy.visual
        thisExp.addData("task.started_Unix", time.time())
        #window = psychopy.visual.Window()
        win.getMovieFrame();
        # store start times for TaskRoutine
        TaskRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        TaskRoutine.tStart = globalClock.getTime(format='float')
        TaskRoutine.status = STARTED
        thisExp.addData('TaskRoutine.started', TaskRoutine.tStart)
        TaskRoutine.maxDuration = None
        # keep track of which components have finished
        TaskRoutineComponents = TaskRoutine.components
        for thisComponent in TaskRoutine.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TaskRoutine" ---
        TaskRoutine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisScenarioLoop, 'status') and thisScenarioLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Task* updates
            
            # if Task is starting this frame...
            if Task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Task.frameNStart = frameN  # exact frame index
                Task.tStart = t  # local t and not account for scr refresh
                Task.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Task, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Task.started')
                # update status
                Task.status = STARTED
                Task.setAutoDraw(True)
            
            # if Task is active this frame...
            if Task.status == STARTED:
                # update params
                pass
            
            # *ready_3* updates
            waitOnFlip = False
            
            # if ready_3 is starting this frame...
            if ready_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                ready_3.frameNStart = frameN  # exact frame index
                ready_3.tStart = t  # local t and not account for scr refresh
                ready_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ready_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ready_3.started')
                # update status
                ready_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ready_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ready_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ready_3.status == STARTED and not waitOnFlip:
                theseKeys = ready_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _ready_3_allKeys.extend(theseKeys)
                if len(_ready_3_allKeys):
                    ready_3.keys = _ready_3_allKeys[-1].name  # just the last key pressed
                    ready_3.rt = _ready_3_allKeys[-1].rt
                    ready_3.duration = _ready_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=TaskRoutine,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                TaskRoutine.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TaskRoutine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TaskRoutine" ---
        for thisComponent in TaskRoutine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for TaskRoutine
        TaskRoutine.tStop = globalClock.getTime(format='float')
        TaskRoutine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('TaskRoutine.stopped', TaskRoutine.tStop)
        # Run 'End Routine' code from saveTaskTime
        import time
        thisExp.addData("task.stopped_Unix", time.time())
        # the Routine "TaskRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "PromptRoutine" ---
        # create an object to store info about Routine PromptRoutine
        PromptRoutine = data.Routine(
            name='PromptRoutine',
            components=[ParticipantResponse, PromptText],
        )
        PromptRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        ParticipantResponse.reset()
        PromptText.setText(scenario)
        # Run 'Begin Routine' code from savePromptTime
        import time
        thisExp.addData("prompt.started_Unix", time.time())
        # store start times for PromptRoutine
        PromptRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PromptRoutine.tStart = globalClock.getTime(format='float')
        PromptRoutine.status = STARTED
        thisExp.addData('PromptRoutine.started', PromptRoutine.tStart)
        PromptRoutine.maxDuration = None
        # keep track of which components have finished
        PromptRoutineComponents = PromptRoutine.components
        for thisComponent in PromptRoutine.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PromptRoutine" ---
        PromptRoutine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisScenarioLoop, 'status') and thisScenarioLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ParticipantResponse* updates
            
            # if ParticipantResponse is starting this frame...
            if ParticipantResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ParticipantResponse.frameNStart = frameN  # exact frame index
                ParticipantResponse.tStart = t  # local t and not account for scr refresh
                ParticipantResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ParticipantResponse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ParticipantResponse.started')
                # update status
                ParticipantResponse.status = STARTED
                ParticipantResponse.setAutoDraw(True)
            
            # if ParticipantResponse is active this frame...
            if ParticipantResponse.status == STARTED:
                # update params
                pass
            
            # *PromptText* updates
            
            # if PromptText is starting this frame...
            if PromptText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PromptText.frameNStart = frameN  # exact frame index
                PromptText.tStart = t  # local t and not account for scr refresh
                PromptText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PromptText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PromptText.started')
                # update status
                PromptText.status = STARTED
                PromptText.setAutoDraw(True)
            
            # if PromptText is active this frame...
            if PromptText.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from prompt_code
            from psychopy import event
            
            # Check if participant has typed something AND pressed return
            keys = event.getKeys()
            if ParticipantResponse.text and 'return' in keys:
                # mark that the response is complete
                continueRoutine = False  # ends the current routine
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PromptRoutine,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PromptRoutine.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PromptRoutine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PromptRoutine" ---
        for thisComponent in PromptRoutine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PromptRoutine
        PromptRoutine.tStop = globalClock.getTime(format='float')
        PromptRoutine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PromptRoutine.stopped', PromptRoutine.tStop)
        ScenarioLoop.addData('ParticipantResponse.text',ParticipantResponse.text.strip())
        # Run 'End Routine' code from prompt_code
        import requests
        import re
        from sentence_transformers import SentenceTransformer, util
        import torch
        import random
        import time
        from dotenv import load_dotenv

        load_dotenv()
        OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        # MODEL = "openai/gpt-3.5-turbo-instruct"
        MODEL = "openai/gpt-5.4-mini"
        print(MODEL)

        DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
        # model = SentenceTransformer(r"C:\Users\Display\Desktop\all-MiniLM-L6-v2", device=DEVICE)
        print("Sentence Transformer found!")
        
        def generate_llm_responses_openrouter(scenario, participant_answer, n=100):
            url = "https://openrouter.ai/api/v1/chat/completions"
        
            prompt = (
                f"Scenario: {scenario}\n"
                f"Participant answer: {participant_answer}\n\n"
                f"Generate {n} short, natural, polite responses (max 20 words).\n"
                f"Return each response on a separate line.\n"
            )
        
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }
        
            payload = {
                "model": MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 800,
                "temperature": 0.7,
                "top_p": 0.9,
                "n": 1
            }
        
            max_retries = 5
            for attempt in range(max_retries):
                r = requests.post(url, headers=headers, json=payload)
                if r.status_code == 200:
                    resp_json = r.json()
                    text = resp_json["choices"][0]["message"]["content"]
        
                    # Zeilen filtern + führende Zahlen entfernen
                    responses = [
                        re.sub(r"^\d+\.\s*", "", l.strip())
                        for l in text.split("\n")
                        if len(l.split()) > 2
                    ]
                    print(len(responses), "responses generated")
                    return responses[:n]  # exakt n Antworten
                elif r.status_code == 429:
                    wait_time = 5 * (attempt + 1)
                    print(f"Rate-limited! Warte {wait_time}s und retry {attempt+1}/{max_retries}...")
                    time.sleep(wait_time)
                else:
                    raise ValueError(f"Request failed: {r.status_code} {r.text}")
        
            raise ValueError("Max retries reached due to rate limiting.")
            return responses[:n]  # exakt n Antworten
        
        
        # -----------------------------------------------------------
        # 2) Alignment + Similarity berechnen
        # -----------------------------------------------------------
        def compute_alignment_responses(scenario, participant_answer):
            high = participant_answer.strip()
            # 100 Modellantworten generieren
            responses = generate_llm_responses_openrouter(scenario, participant_answer, 100)
        
            # Embeddings
            emb_llm = model.encode(responses, convert_to_tensor=True)
            emb_part = model.encode(participant_answer, convert_to_tensor=True)
        
            sims = util.cos_sim(emb_part, emb_llm)[0].cpu().tolist()
        
            # Sortieren nach Ähnlichkeit
            scored = sorted(zip(responses, sims), key=lambda x: x[1], reverse=True)
        
            # high = participant_answer.strip()
            medium = scored[len(scored)//2][0]
            low = random.choice(scored[-5:])[0]
        
            return {
                "high": {"text": high, "sim": 1.0},
                "medium": {"text": medium, "sim": scored[len(scored)//2][1]},
                "low": {"text": low, "sim": scored[-1][1]},
                "all_sims": sims
            }
        
        participant_answer = ParticipantResponse.text.strip()
        scenario_text = scenario
        
        print("Scenario: ", scenario)
        print("Answer: ", participant_answer)
        
        thisExp.addData('scenario', scenario)
        thisExp.addData('participant_answer', participant_answer)
        
        alignments = compute_alignment_responses(scenario_text, participant_answer)
        
        print("Medium answer: ", alignments['medium']['text'])
        print("Medium sim: ", alignments['medium']['sim'])
        print("Low answer: ", alignments['low']['text'])
        print("Low sim: ", alignments['low']['sim'])
        
        thisExp.addData('ai_high', alignments['high']['text'])
        thisExp.addData('ai_medium', alignments['medium']['text'])
        thisExp.addData('ai_low', alignments['low']['text'])
        thisExp.addData('sim_medium', alignments['medium']['sim'])
        thisExp.addData('sim_low', alignments['low']['sim'])
        
        expInfo['alignments'] = alignments
        
        # Run 'End Routine' code from savePromptTime
        import time
        thisExp.addData("prompt.stopped_Unix", time.time())
        
        # the Routine "PromptRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "AIRoutine" ---
        # create an object to store info about Routine AIRoutine
        AIRoutine = data.Routine(
            name='AIRoutine',
            components=[AI_Response, text],
        )
        AIRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        AI_Response.reset()
        AI_Response.setText('')
        # Run 'Begin Routine' code from ai_response_code
        from psychopy import parallel
        from psychopy import core, event
        import time, random
        
        #ai_delay = 3.0  # Sekunden
        #ai_shown = False
        #trial_clock = core.Clock()
        #trial_clock.reset()
        
        # Alignment aus Excel-Tabelle verwenden
        alignment = Alignment.lower().strip()  # z. B. "high"
        
        # Zugriff auf gespeicherte Texte
        alignments = expInfo['alignments']
        ai_text = alignments[alignment]['text']
        
        # anzeigen
        AI_Response.setText(ai_text)
        
        # speichern
        print("LLM Alignment:", alignment)
        print("LLM Response:", ai_text)
        thisExp.addData('AI_shown_alignment', alignment)
        thisExp.addData('AI_shown_text', ai_text)
        # Run 'Begin Routine' code from saveBeginAIResponseTime
        import time
        thisExp.addData("ai_response.started_Unix", time.time())
        # store start times for AIRoutine
        AIRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        AIRoutine.tStart = globalClock.getTime(format='float')
        AIRoutine.status = STARTED
        thisExp.addData('AIRoutine.started', AIRoutine.tStart)
        AIRoutine.maxDuration = None
        # keep track of which components have finished
        AIRoutineComponents = AIRoutine.components
        for thisComponent in AIRoutine.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "AIRoutine" ---
        AIRoutine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisScenarioLoop, 'status') and thisScenarioLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AI_Response* updates
            
            # if AI_Response is starting this frame...
            if AI_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AI_Response.frameNStart = frameN  # exact frame index
                AI_Response.tStart = t  # local t and not account for scr refresh
                AI_Response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AI_Response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'AI_Response.started')
                # update status
                AI_Response.status = STARTED
                AI_Response.setAutoDraw(True)
            
            # if AI_Response is active this frame...
            if AI_Response.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from ai_response_code
            keys = event.getKeys()
            if 'space' in keys:
                continueRoutine = False
                event.clearEvents()
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=AIRoutine,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                AIRoutine.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AIRoutine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "AIRoutine" ---
        for thisComponent in AIRoutine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for AIRoutine
        AIRoutine.tStop = globalClock.getTime(format='float')
        AIRoutine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('AIRoutine.stopped', AIRoutine.tStop)
        # Run 'End Routine' code from saveBeginAIResponseTime
        import time
        thisExp.addData("ai_response.stopped_Unix", time.time())
        # the Routine "AIRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "RatingRoutine" ---
        # create an object to store info about Routine RatingRoutine
        RatingRoutine = data.Routine(
            name='RatingRoutine',
            components=[slider, rating_text, mouse],
        )
        RatingRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        slider.reset()
        # Run 'Begin Routine' code from slider_code
        from psychopy import event
        win.mouseVisible = True
        slider.reset()
        
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from saveRatingData
        import time
        thisExp.addData("rating.started_Unix", time.time())
        # store start times for RatingRoutine
        RatingRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        RatingRoutine.tStart = globalClock.getTime(format='float')
        RatingRoutine.status = STARTED
        thisExp.addData('RatingRoutine.started', RatingRoutine.tStart)
        RatingRoutine.maxDuration = None
        # keep track of which components have finished
        RatingRoutineComponents = RatingRoutine.components
        for thisComponent in RatingRoutine.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "RatingRoutine" ---
        RatingRoutine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisScenarioLoop, 'status') and thisScenarioLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *slider* updates
            
            # if slider is starting this frame...
            if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider.frameNStart = frameN  # exact frame index
                slider.tStart = t  # local t and not account for scr refresh
                slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider.started')
                # update status
                slider.status = STARTED
                slider.setAutoDraw(True)
            
            # if slider is active this frame...
            if slider.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from slider_code
            if slider.getRating() is not None:
                continueRoutine = False  # end the routine as soon as user made a selection
            
            
            # *rating_text* updates
            
            # if rating_text is starting this frame...
            if rating_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_text.frameNStart = frameN  # exact frame index
                rating_text.tStart = t  # local t and not account for scr refresh
                rating_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rating_text.started')
                # update status
                rating_text.status = STARTED
                rating_text.setAutoDraw(True)
            
            # if rating_text is active this frame...
            if rating_text.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=RatingRoutine,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                RatingRoutine.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RatingRoutine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "RatingRoutine" ---
        for thisComponent in RatingRoutine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for RatingRoutine
        RatingRoutine.tStop = globalClock.getTime(format='float')
        RatingRoutine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('RatingRoutine.stopped', RatingRoutine.tStop)
        ScenarioLoop.addData('slider.response', slider.getRating())
        ScenarioLoop.addData('slider.rt', slider.getRT())
        # Run 'End Routine' code from slider_code
        win.mouseVisible = False
        rating = slider.getRating()
        # store data for ScenarioLoop (TrialHandler)
        # Run 'End Routine' code from saveRatingData
        import time
        thisExp.addData("rating.stopped_Unix", time.time())
        
        rating = slider.getRating()
        rt = slider.getRT()
        
        thisExp.addData('slider.rating', rating)
        thisExp.addData('slider.rt', rt)
        
        
        # the Routine "RatingRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "PauseRoutine" ---
        # create an object to store info about Routine PauseRoutine
        PauseRoutine = data.Routine(
            name='PauseRoutine',
            components=[Pause],
        )
        PauseRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from savePauseTime
        import time
        thisExp.addData("task.started_Unix", time.time())
        print("Pause?")
        
        if (ScenarioLoop.thisN + 1) % 5 != 0:
            continueRoutine = False
        # store start times for PauseRoutine
        PauseRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PauseRoutine.tStart = globalClock.getTime(format='float')
        PauseRoutine.status = STARTED
        thisExp.addData('PauseRoutine.started', PauseRoutine.tStart)
        PauseRoutine.maxDuration = None
        # keep track of which components have finished
        PauseRoutineComponents = PauseRoutine.components
        for thisComponent in PauseRoutine.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PauseRoutine" ---
        PauseRoutine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisScenarioLoop, 'status') and thisScenarioLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Pause* updates
            
            # if Pause is starting this frame...
            if Pause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pause.frameNStart = frameN  # exact frame index
                Pause.tStart = t  # local t and not account for scr refresh
                Pause.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pause, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Pause.started')
                # update status
                Pause.status = STARTED
                Pause.setAutoDraw(True)
            
            # if Pause is active this frame...
            if Pause.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from savePauseTime
            keys = event.getKeys()
            if 'space' in keys:
                continueRoutine = False
                event.clearEvents()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PauseRoutine,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PauseRoutine.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PauseRoutine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PauseRoutine" ---
        for thisComponent in PauseRoutine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PauseRoutine
        PauseRoutine.tStop = globalClock.getTime(format='float')
        PauseRoutine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PauseRoutine.stopped', PauseRoutine.tStop)
        # Run 'End Routine' code from savePauseTime
        import time
        thisExp.addData("task.stopped_Unix", time.time())
        # the Routine "PauseRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisScenarioLoop as finished
        if hasattr(thisScenarioLoop, 'status'):
            thisScenarioLoop.status = FINISHED
        # if awaiting a pause, pause now
        if ScenarioLoop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            ScenarioLoop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'ScenarioLoop'
    ScenarioLoop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "eyelinkStopRecording_2" ---
    # create an object to store info about Routine eyelinkStopRecording_2
    eyelinkStopRecording_2 = data.Routine(
        name='eyelinkStopRecording_2',
        components=[],
    )
    eyelinkStopRecording_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from saveStopRecordTime_2
    import time
    thisExp.addData("el_recordingStop.started_Unix", time.time())
    # store start times for eyelinkStopRecording_2
    eyelinkStopRecording_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    eyelinkStopRecording_2.tStart = globalClock.getTime(format='float')
    eyelinkStopRecording_2.status = STARTED
    thisExp.addData('eyelinkStopRecording_2.started', eyelinkStopRecording_2.tStart)
    eyelinkStopRecording_2.maxDuration = None
    # keep track of which components have finished
    eyelinkStopRecording_2Components = eyelinkStopRecording_2.components
    for thisComponent in eyelinkStopRecording_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "eyelinkStopRecording_2" ---
    eyelinkStopRecording_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=eyelinkStopRecording_2,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            eyelinkStopRecording_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eyelinkStopRecording_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eyelinkStopRecording_2" ---
    for thisComponent in eyelinkStopRecording_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for eyelinkStopRecording_2
    eyelinkStopRecording_2.tStop = globalClock.getTime(format='float')
    eyelinkStopRecording_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('eyelinkStopRecording_2.stopped', eyelinkStopRecording_2.tStop)
    # Run 'End Routine' code from elStopRecord_2
    # This End Routine tab of the elStopRecord component clears the 
    # screen (and sends a message to mark the clearing), stops recording, sends
    # a trial end message, and increments a trial counter variable
    
    # clear the screen
    clear_screen(win,genv)
    el_tracker.sendMessage('blank_screen')
    # send a message to clear the Data Viewer screen as well
    el_tracker.sendMessage('!V CLEAR 128 128 128')
    
    # stop recording; add 100 msec to catch final events before stopping
    pylink.pumpDelay(100)
    el_tracker.stopRecording()
        
    # send a 'TRIAL_RESULT' message to mark the end of trial, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    el_tracker.sendMessage('TRIAL_RESULT %d' % 0)
    
    # update the trial counter for the next trial
    trial_index = trial_index + 1
    
    # Run 'End Routine' code from saveStopRecordTime_2
    import time
    thisExp.addData("el_recordingStop.stopped_Unix", time.time())
    thisExp.nextEntry()
    # the Routine "eyelinkStopRecording_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "thanks" ---
    # create an object to store info about Routine thanks
    thanks = data.Routine(
        name='thanks',
        components=[endScreen],
    )
    thanks.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from end_code
    import time
    thisExp.addData("experimentStop.started_Unix", time.time())
    # store start times for thanks
    thanks.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    thanks.tStart = globalClock.getTime(format='float')
    thanks.status = STARTED
    thisExp.addData('thanks.started', thanks.tStart)
    thanks.maxDuration = None
    # keep track of which components have finished
    thanksComponents = thanks.components
    for thisComponent in thanks.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thanks" ---
    thanks.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endScreen* updates
        
        # if endScreen is starting this frame...
        if endScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endScreen.frameNStart = frameN  # exact frame index
            endScreen.tStart = t  # local t and not account for scr refresh
            endScreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endScreen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endScreen.started')
            # update status
            endScreen.status = STARTED
            endScreen.setAutoDraw(True)
        
        # if endScreen is active this frame...
        if endScreen.status == STARTED:
            # update params
            pass
        
        # if endScreen is stopping this frame...
        if endScreen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > endScreen.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                endScreen.tStop = t  # not accounting for scr refresh
                endScreen.tStopRefresh = tThisFlipGlobal  # on global time
                endScreen.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'endScreen.stopped')
                # update status
                endScreen.status = FINISHED
                endScreen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=thanks,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            thanks.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thanks.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thanks" ---
    for thisComponent in thanks.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for thanks
    thanks.tStop = globalClock.getTime(format='float')
    thanks.tStopRefresh = tThisFlipGlobal
    thisExp.addData('thanks.stopped', thanks.tStop)
    # Run 'End Routine' code from end_code
    import time
    thisExp.addData("experimentStop.stopped_Unix", time.time())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if thanks.maxDurationReached:
        routineTimer.addTime(-thanks.maxDuration)
    elif thanks.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    # Run 'End Experiment' code from elConnect_2
    # This End Experiment tab of the elConnect component calls the 
    # terminate_task helper function to get the EDF file and close the connection
    # to the Host PC
    
    # Disconnect, download the EDF file, then terminate the task
    terminate_task(genv,edf_file,session_folder,session_identifier)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim=',', quoting=csv.QUOTE.NONNUMERIC)
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
