/**************************** 
 * Human-Llm-Alignment *
 ****************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2025.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'human-llm-alignment';  // from the Builder filename that created this script
let expInfo = {
    'participant': '01',
    'session': '01',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from elConnect_2
/* Syntax Error: Fix Python code */
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'pix',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(eyelinkSetup_2RoutineBegin());
flowScheduler.add(eyelinkSetup_2RoutineEachFrame());
flowScheduler.add(eyelinkSetup_2RoutineEnd());
flowScheduler.add(instructionRoutineBegin());
flowScheduler.add(instructionRoutineEachFrame());
flowScheduler.add(instructionRoutineEnd());
flowScheduler.add(eyelinkStartRecording_2RoutineBegin());
flowScheduler.add(eyelinkStartRecording_2RoutineEachFrame());
flowScheduler.add(eyelinkStartRecording_2RoutineEnd());
const ScenarioLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ScenarioLoopLoopBegin(ScenarioLoopLoopScheduler));
flowScheduler.add(ScenarioLoopLoopScheduler);
flowScheduler.add(ScenarioLoopLoopEnd);






flowScheduler.add(eyelinkStopRecording_2RoutineBegin());
flowScheduler.add(eyelinkStopRecording_2RoutineEachFrame());
flowScheduler.add(eyelinkStopRecording_2RoutineEnd());
flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'scenarios.xlsx', 'path': 'scenarios.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "eyelinkSetup_2"
  eyelinkSetup_2Clock = new util.Clock();
  elInstructions_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'elInstructions_2',
    text: 'Press any key to start Camera Setup',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 50.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  taskInstructions_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'taskInstructions_2',
    text: 'Ready for the experiment?\n\nPress SPACE key to continue',
    font: 'Courier New',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 30.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  ready_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "eyelinkStartRecording_2"
  eyelinkStartRecording_2Clock = new util.Clock();
  // Initialize components for Routine "TaskRoutine"
  TaskRoutineClock = new util.Clock();
  Task = new visual.TextStim({
    win: psychoJS.window,
    name: 'Task',
    text: 'Read the following situation and then write what you would say in that situation. \n\nPress SPACE to continue\n',
    font: 'Courier New',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 30.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  ready_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PromptRoutine"
  PromptRoutineClock = new util.Clock();
  ParticipantResponse = new visual.TextBox({
    win: psychoJS.window,
    name: 'ParticipantResponse',
    text: '',
    placeholder: 'Type here...',
    font: 'Courier New',
    pos: [0, (- 250)], 
    draggable: false,
    letterHeight: 30.0,
    lineSpacing: 1.0,
    size: [500, 200],  units: 'pix', 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  PromptText = new visual.TextStim({
    win: psychoJS.window,
    name: 'PromptText',
    text: '',
    font: 'Courier New',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 30.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Run 'Begin Experiment' code from prompt_code
  participant_resp = "";
  
  // Initialize components for Routine "AIRoutine"
  AIRoutineClock = new util.Clock();
  AI_Response = new visual.TextBox({
    win: psychoJS.window,
    name: 'AI_Response',
    text: '',
    placeholder: 'Type here...',
    font: 'Courier New',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 30.0,
    lineSpacing: 1.0,
    size: [500, 200],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  // Run 'Begin Experiment' code from ai_response_code
  import {core, data, event} from 'psychopy';
  import * as random from 'random';
  import * as json from 'json';
  import * as time from 'time';
  import * as subprocess from 'subprocess';
  import * as re from 're';
  import {datetime} from 'datetime';
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "RatingRoutine"
  RatingRoutineClock = new util.Clock();
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    startValue: 50,
    size: [1000, 80], pos: [0, (- 150)], ori: 0.0, units: 'pix',
    labels: ["Strongly disagree", "Strongly agree"], fontSize: 20.0, ticks: [0, 100],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Noto Sans', bold: true, italic: false, depth: 0, 
    flip: false,
  });
  
  // Run 'Begin Experiment' code from slider_code
  import {event} from 'psychopy';
  
  rating_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rating_text',
    text: 'The LLM answer was aligned with my own answer for this scenario.',
    font: 'Courier New',
    units: 'pix', 
    pos: [0, 0], draggable: false, height: 30.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "PauseRoutine"
  PauseRoutineClock = new util.Clock();
  Pause = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pause',
    text: 'Do you need a break?\n\nIf yes, do not press anything.\n\nIf not, press SPACE to continue',
    font: 'Courier New',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 30.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Run 'Begin Experiment' code from savePauseTime
  import {event} from 'psychopy';
  
  // Initialize components for Routine "eyelinkStopRecording_2"
  eyelinkStopRecording_2Clock = new util.Clock();
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  endScreen = new visual.TextStim({
    win: psychoJS.window,
    name: 'endScreen',
    text: 'This is the end of the experiment.\n\nThanks!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 50.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function eyelinkSetup_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'eyelinkSetup_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    eyelinkSetup_2Clock.reset();
    routineTimer.reset();
    eyelinkSetup_2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // Run 'Begin Routine' code from saveBeginSetupTime_2
    import * as time from 'time';
    psychoJS.experiment.addData("el_setup.started_Unix", time.time());
    
    psychoJS.experiment.addData('eyelinkSetup_2.started', globalClock.getTime());
    eyelinkSetup_2MaxDuration = null
    // keep track of which components have finished
    eyelinkSetup_2Components = [];
    eyelinkSetup_2Components.push(elInstructions_2);
    eyelinkSetup_2Components.push(key_resp_2);
    
    for (const thisComponent of eyelinkSetup_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function eyelinkSetup_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'eyelinkSetup_2' ---
    // get current time
    t = eyelinkSetup_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *elInstructions_2* updates
    if (t >= 0.0 && elInstructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      elInstructions_2.tStart = t;  // (not accounting for frame time here)
      elInstructions_2.frameNStart = frameN;  // exact frame index
      
      elInstructions_2.setAutoDraw(true);
    }
    
    
    // if elInstructions_2 is active this frame...
    if (elInstructions_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    // if key_resp_2 is active this frame...
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: "space", waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of eyelinkSetup_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function eyelinkSetup_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'eyelinkSetup_2' ---
    for (const thisComponent of eyelinkSetup_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('eyelinkSetup_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // Run 'End Routine' code from elConnect_2
    if ((! dummy_mode)) {
        try {
            el_tracker.doTrackerSetup();
        } catch(err) {
            if ((err instanceof RuntimeError)) {
                console.log("ERROR:", err);
                el_tracker.exitCalibration();
            } else {
                throw err;
            }
        }
    }
    
    // Run 'End Routine' code from saveBeginSetupTime_2
    import * as time from 'time';
    psychoJS.experiment.addData("el_recording.stopped_Unix", time.time());
    
    // the Routine "eyelinkSetup_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function instructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instructionClock.reset();
    routineTimer.reset();
    instructionMaxDurationReached = false;
    // update component parameters for each repeat
    ready_2.keys = undefined;
    ready_2.rt = undefined;
    _ready_2_allKeys = [];
    // Run 'Begin Routine' code from saveInstructTime_2
    import * as time from 'time';
    import * as psychopy.visual from 'psychopy/visual';
    psychoJS.experiment.addData("instructions.started_Unix", time.time());
    psychoJS.window.getMovieFrame();
    
    psychoJS.experiment.addData('instruction.started', globalClock.getTime());
    instructionMaxDuration = null
    instructionStartWinParams = {
        'color': psychoJS.window.color,
        'colorSpace': psychoJS.window.colorSpace,
        'backgroundImage': psychoJS.window.backgroundImage,
        'backgroundFit': psychoJS.window.backgroundFit,
    };
    psychoJS.window.color = [(- 1.0), (- 1.0), (- 1.0)];
    psychoJS.window.colorSpace = 'rgb';
    psychoJS.window.backgroundImage = '';
    psychoJS.window.backgroundFit = 'none';
    // keep track of which components have finished
    instructionComponents = [];
    instructionComponents.push(taskInstructions_2);
    instructionComponents.push(ready_2);
    
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction' ---
    // get current time
    t = instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *taskInstructions_2* updates
    if (t >= 0.0 && taskInstructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      taskInstructions_2.tStart = t;  // (not accounting for frame time here)
      taskInstructions_2.frameNStart = frameN;  // exact frame index
      
      taskInstructions_2.setAutoDraw(true);
    }
    
    
    // if taskInstructions_2 is active this frame...
    if (taskInstructions_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *ready_2* updates
    if (t >= 0 && ready_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready_2.tStart = t;  // (not accounting for frame time here)
      ready_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ready_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ready_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ready_2.clearEvents(); });
    }
    
    // if ready_2 is active this frame...
    if (ready_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = ready_2.getKeys({keyList: 'space', waitRelease: false});
      _ready_2_allKeys = _ready_2_allKeys.concat(theseKeys);
      if (_ready_2_allKeys.length > 0) {
        ready_2.keys = _ready_2_allKeys[_ready_2_allKeys.length - 1].name;  // just the last key pressed
        ready_2.rt = _ready_2_allKeys[_ready_2_allKeys.length - 1].rt;
        ready_2.duration = _ready_2_allKeys[_ready_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction' ---
    for (const thisComponent of instructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instruction.stopped', globalClock.getTime());
    psychoJS.window.color = instructionStartWinParams['color'];
    psychoJS.window.colorSpace = instructionStartWinParams['colorSpace'];
    psychoJS.window.backgroundImage = instructionStartWinParams['backgroundImage'];
    psychoJS.window.backgroundFit = instructionStartWinParams['backgroundFit'];
    ready_2.stop();
    // Run 'End Routine' code from saveInstructTime_2
    import * as time from 'time';
    psychoJS.experiment.addData("instructions.stopped_Unix", time.time());
    
    // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function eyelinkStartRecording_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'eyelinkStartRecording_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    eyelinkStartRecording_2Clock.reset();
    routineTimer.reset();
    eyelinkStartRecording_2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from elStartRecord_2
    haveSentImageOnsetMessage = 0;
    el_tracker = pylink.getEYELINK();
    el_tracker.setOfflineMode();
    el_tracker.sendCommand("clear_screen 0");
    im = Image.open(((script_path + "/") + trialImage));
    im = im.resize([scn_width, scn_height]);
    img_pixels = im.load();
    pixels = function () {
        var _pj_a = [], _pj_b = util.range(scn_height);
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var j = _pj_b[_pj_c];
            _pj_a.push(function () {
        var _pj_e = [], _pj_f = util.range(scn_width);
        for (var _pj_g = 0, _pj_h = _pj_f.length; (_pj_g < _pj_h); _pj_g += 1) {
            var i = _pj_f[_pj_g];
            _pj_e.push(img_pixels[[i, j]]);
        }
        return _pj_e;
    }
    .call(this));
        }
        return _pj_a;
    }
    .call(this);
    el_tracker.bitmapBackdrop(scn_width, scn_height, pixels, 0, 0, scn_width, scn_height, 0, 0, pylink.BX_MAXCONTRAST);
    left = (Number.parseInt((scn_width / 2.0)) - 60);
    top = (Number.parseInt((scn_height / 2.0)) - 60);
    right = (Number.parseInt((scn_width / 2.0)) + 60);
    bottom = (Number.parseInt((scn_height / 2.0)) + 60);
    draw_cmd = `draw_filled_box ${left} ${top} ${right} ${bottom}`;
    el_tracker.sendCommand(draw_cmd);
    el_tracker.sendMessage(`TRIALID ${trial_index}`);
    status_msg = `TRIAL number ${trial_index}`;
    el_tracker.sendCommand(`record_status_message '${status_msg}`);
    while ((! dummy_mode)) {
        if (((! el_tracker.isConnected()) || el_tracker.breakPressed())) {
            terminate_task();
        }
        try {
            error = el_tracker.doDriftCorrect(Number.parseInt((scn_width / 2.0)), Number.parseInt((scn_height / 2.0)), 1, 1);
            if ((error !== pylink.ESC_KEY)) {
                break;
            }
        } catch(e) {
        }
    }
    el_tracker.setOfflineMode();
    try {
        el_tracker.startRecording(1, 1, 1, 1);
    } catch(error) {
        if ((error instanceof RuntimeError)) {
            console.log("ERROR:", error);
            abort_trial();
        } else {
            throw error;
        }
    }
    pylink.pumpDelay(100);
    
    // Run 'Begin Routine' code from saveRecordStartTime_2
    import * as time from 'time';
    psychoJS.experiment.addData("el_recording.started_Unix", time.time());
    
    psychoJS.experiment.addData('eyelinkStartRecording_2.started', globalClock.getTime());
    eyelinkStartRecording_2MaxDuration = null
    // keep track of which components have finished
    eyelinkStartRecording_2Components = [];
    
    for (const thisComponent of eyelinkStartRecording_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function eyelinkStartRecording_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'eyelinkStartRecording_2' ---
    // get current time
    t = eyelinkStartRecording_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of eyelinkStartRecording_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function eyelinkStartRecording_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'eyelinkStartRecording_2' ---
    for (const thisComponent of eyelinkStartRecording_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('eyelinkStartRecording_2.stopped', globalClock.getTime());
    // Run 'End Routine' code from saveRecordStartTime_2
    import * as time from 'time';
    psychoJS.experiment.addData("el_recording.stopped_Unix", time.time());
    
    // the Routine "eyelinkStartRecording_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function ScenarioLoopLoopBegin(ScenarioLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ScenarioLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'scenarios.xlsx',
      seed: undefined, name: 'ScenarioLoop'
    });
    psychoJS.experiment.addLoop(ScenarioLoop); // add the loop to the experiment
    currentLoop = ScenarioLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisScenarioLoop of ScenarioLoop) {
      snapshot = ScenarioLoop.getSnapshot();
      ScenarioLoopLoopScheduler.add(importConditions(snapshot));
      ScenarioLoopLoopScheduler.add(TaskRoutineRoutineBegin(snapshot));
      ScenarioLoopLoopScheduler.add(TaskRoutineRoutineEachFrame());
      ScenarioLoopLoopScheduler.add(TaskRoutineRoutineEnd(snapshot));
      ScenarioLoopLoopScheduler.add(PromptRoutineRoutineBegin(snapshot));
      ScenarioLoopLoopScheduler.add(PromptRoutineRoutineEachFrame());
      ScenarioLoopLoopScheduler.add(PromptRoutineRoutineEnd(snapshot));
      ScenarioLoopLoopScheduler.add(AIRoutineRoutineBegin(snapshot));
      ScenarioLoopLoopScheduler.add(AIRoutineRoutineEachFrame());
      ScenarioLoopLoopScheduler.add(AIRoutineRoutineEnd(snapshot));
      ScenarioLoopLoopScheduler.add(RatingRoutineRoutineBegin(snapshot));
      ScenarioLoopLoopScheduler.add(RatingRoutineRoutineEachFrame());
      ScenarioLoopLoopScheduler.add(RatingRoutineRoutineEnd(snapshot));
      ScenarioLoopLoopScheduler.add(PauseRoutineRoutineBegin(snapshot));
      ScenarioLoopLoopScheduler.add(PauseRoutineRoutineEachFrame());
      ScenarioLoopLoopScheduler.add(PauseRoutineRoutineEnd(snapshot));
      ScenarioLoopLoopScheduler.add(ScenarioLoopLoopEndIteration(ScenarioLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function ScenarioLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(ScenarioLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function ScenarioLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function TaskRoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TaskRoutine' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TaskRoutineClock.reset();
    routineTimer.reset();
    TaskRoutineMaxDurationReached = false;
    // update component parameters for each repeat
    ready_3.keys = undefined;
    ready_3.rt = undefined;
    _ready_3_allKeys = [];
    // Run 'Begin Routine' code from saveTaskTime
    import * as time from 'time';
    import * as psychopy.visual from 'psychopy/visual';
    psychoJS.experiment.addData("task.started_Unix", time.time());
    psychoJS.window.getMovieFrame();
    
    psychoJS.experiment.addData('TaskRoutine.started', globalClock.getTime());
    TaskRoutineMaxDuration = null
    // keep track of which components have finished
    TaskRoutineComponents = [];
    TaskRoutineComponents.push(Task);
    TaskRoutineComponents.push(ready_3);
    
    for (const thisComponent of TaskRoutineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function TaskRoutineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TaskRoutine' ---
    // get current time
    t = TaskRoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Task* updates
    if (t >= 0.0 && Task.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Task.tStart = t;  // (not accounting for frame time here)
      Task.frameNStart = frameN;  // exact frame index
      
      Task.setAutoDraw(true);
    }
    
    
    // if Task is active this frame...
    if (Task.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *ready_3* updates
    if (t >= 0 && ready_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready_3.tStart = t;  // (not accounting for frame time here)
      ready_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ready_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ready_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ready_3.clearEvents(); });
    }
    
    // if ready_3 is active this frame...
    if (ready_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = ready_3.getKeys({keyList: 'space', waitRelease: false});
      _ready_3_allKeys = _ready_3_allKeys.concat(theseKeys);
      if (_ready_3_allKeys.length > 0) {
        ready_3.keys = _ready_3_allKeys[_ready_3_allKeys.length - 1].name;  // just the last key pressed
        ready_3.rt = _ready_3_allKeys[_ready_3_allKeys.length - 1].rt;
        ready_3.duration = _ready_3_allKeys[_ready_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TaskRoutineComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function TaskRoutineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TaskRoutine' ---
    for (const thisComponent of TaskRoutineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('TaskRoutine.stopped', globalClock.getTime());
    ready_3.stop();
    // Run 'End Routine' code from saveTaskTime
    import * as time from 'time';
    psychoJS.experiment.addData("task.stopped_Unix", time.time());
    
    // the Routine "TaskRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function PromptRoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PromptRoutine' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    PromptRoutineClock.reset();
    routineTimer.reset();
    PromptRoutineMaxDurationReached = false;
    // update component parameters for each repeat
    ParticipantResponse.setText('');
    ParticipantResponse.refresh();
    PromptText.setText(scenario);
    // Run 'Begin Routine' code from savePromptTime
    import * as time from 'time';
    psychoJS.experiment.addData("prompt.started_Unix", time.time());
    
    psychoJS.experiment.addData('PromptRoutine.started', globalClock.getTime());
    PromptRoutineMaxDuration = null
    // keep track of which components have finished
    PromptRoutineComponents = [];
    PromptRoutineComponents.push(ParticipantResponse);
    PromptRoutineComponents.push(PromptText);
    
    for (const thisComponent of PromptRoutineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function PromptRoutineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PromptRoutine' ---
    // get current time
    t = PromptRoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ParticipantResponse* updates
    if (t >= 0.0 && ParticipantResponse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ParticipantResponse.tStart = t;  // (not accounting for frame time here)
      ParticipantResponse.frameNStart = frameN;  // exact frame index
      
      ParticipantResponse.setAutoDraw(true);
    }
    
    
    // if ParticipantResponse is active this frame...
    if (ParticipantResponse.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *PromptText* updates
    if (t >= 0.0 && PromptText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PromptText.tStart = t;  // (not accounting for frame time here)
      PromptText.frameNStart = frameN;  // exact frame index
      
      PromptText.setAutoDraw(true);
    }
    
    
    // if PromptText is active this frame...
    if (PromptText.status === PsychoJS.Status.STARTED) {
    }
    
    // Run 'Each Frame' code from prompt_code
    import {event} from 'psychopy';
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys();
    if ((ParticipantResponse.text && _pj.in_es6("return", keys))) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PromptRoutineComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PromptRoutineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PromptRoutine' ---
    for (const thisComponent of PromptRoutineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('PromptRoutine.stopped', globalClock.getTime());
    psychoJS.experiment.addData('ParticipantResponse.text',ParticipantResponse.text)
    // Run 'End Routine' code from prompt_code
    /* Syntax Error: Fix Python code */
    // Run 'End Routine' code from savePromptTime
    import * as time from 'time';
    psychoJS.experiment.addData("prompt.stopped_Unix", time.time());
    
    // the Routine "PromptRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function AIRoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AIRoutine' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    AIRoutineClock.reset();
    routineTimer.reset();
    AIRoutineMaxDurationReached = false;
    // update component parameters for each repeat
    AI_Response.setText('');
    // Run 'Begin Routine' code from ai_response_code
    import {parallel} from 'psychopy';
    import {core, event} from 'psychopy';
    import * as time from 'time';
    import * as random from 'random';
    alignment = Alignment.toLowerCase().strip();
    alignments = expInfo["alignments"];
    ai_text = alignments[alignment]["text"];
    AI_Response.setText(ai_text);
    console.log("LLM Alignment:", alignment);
    console.log("LLM Response:", ai_text);
    psychoJS.experiment.addData("AI_shown_alignment", alignment);
    psychoJS.experiment.addData("AI_shown_text", ai_text);
    
    // Run 'Begin Routine' code from saveBeginAIResponseTime
    import * as time from 'time';
    psychoJS.experiment.addData("ai_response.started_Unix", time.time());
    
    psychoJS.experiment.addData('AIRoutine.started', globalClock.getTime());
    AIRoutineMaxDuration = null
    // keep track of which components have finished
    AIRoutineComponents = [];
    AIRoutineComponents.push(AI_Response);
    AIRoutineComponents.push(text);
    
    for (const thisComponent of AIRoutineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function AIRoutineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AIRoutine' ---
    // get current time
    t = AIRoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *AI_Response* updates
    if (t >= 0.0 && AI_Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AI_Response.tStart = t;  // (not accounting for frame time here)
      AI_Response.frameNStart = frameN;  // exact frame index
      
      AI_Response.setAutoDraw(true);
    }
    
    
    // if AI_Response is active this frame...
    if (AI_Response.status === PsychoJS.Status.STARTED) {
    }
    
    // Run 'Each Frame' code from ai_response_code
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys();
    if (_pj.in_es6("space", keys)) {
        continueRoutine = false;
        psychoJS.eventManager.clearEvents();
    }
    
    
    // *text* updates
    if (t >= 5 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // if text is active this frame...
    if (text.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AIRoutineComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function AIRoutineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AIRoutine' ---
    for (const thisComponent of AIRoutineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('AIRoutine.stopped', globalClock.getTime());
    // Run 'End Routine' code from saveBeginAIResponseTime
    import * as time from 'time';
    psychoJS.experiment.addData("ai_response.stopped_Unix", time.time());
    
    // the Routine "AIRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function RatingRoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RatingRoutine' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    RatingRoutineClock.reset();
    routineTimer.reset();
    RatingRoutineMaxDurationReached = false;
    // update component parameters for each repeat
    slider.reset()
    // Run 'Begin Routine' code from slider_code
    import {event} from 'psychopy';
    psychoJS.window.mouseVisible = true;
    slider.reset();
    
    // setup some python lists for storing info about the mouse
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from saveRatingData
    import * as time from 'time';
    psychoJS.experiment.addData("rating.started_Unix", time.time());
    
    psychoJS.experiment.addData('RatingRoutine.started', globalClock.getTime());
    RatingRoutineMaxDuration = null
    // keep track of which components have finished
    RatingRoutineComponents = [];
    RatingRoutineComponents.push(slider);
    RatingRoutineComponents.push(rating_text);
    RatingRoutineComponents.push(mouse);
    
    for (const thisComponent of RatingRoutineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function RatingRoutineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RatingRoutine' ---
    // get current time
    t = RatingRoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }
    
    
    // if slider is active this frame...
    if (slider.status === PsychoJS.Status.STARTED) {
    }
    
    // Run 'Each Frame' code from slider_code
    if ((slider.getRating() !== null)) {
        continueRoutine = false;
    }
    
    
    // *rating_text* updates
    if (t >= 0.0 && rating_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rating_text.tStart = t;  // (not accounting for frame time here)
      rating_text.frameNStart = frameN;  // exact frame index
      
      rating_text.setAutoDraw(true);
    }
    
    
    // if rating_text is active this frame...
    if (rating_text.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RatingRoutineComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function RatingRoutineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RatingRoutine' ---
    for (const thisComponent of RatingRoutineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RatingRoutine.stopped', globalClock.getTime());
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    // Run 'End Routine' code from slider_code
    psychoJS.window.mouseVisible = false;
    rating = slider.getRating();
    
    // store data for psychoJS.experiment (ExperimentHandler)
    // Run 'End Routine' code from saveRatingData
    import * as time from 'time';
    psychoJS.experiment.addData("rating.stopped_Unix", time.time());
    rating = slider.getRating();
    rt = slider.getRT();
    psychoJS.experiment.addData("slider.rating", rating);
    psychoJS.experiment.addData("slider.rt", rt);
    
    // the Routine "RatingRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function PauseRoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PauseRoutine' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    PauseRoutineClock.reset();
    routineTimer.reset();
    PauseRoutineMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from savePauseTime
    import * as time from 'time';
    psychoJS.experiment.addData("task.started_Unix", time.time());
    console.log("Pause?");
    if ((((ScenarioLoop.thisN + 1) % 5) !== 0)) {
        continueRoutine = false;
    }
    
    psychoJS.experiment.addData('PauseRoutine.started', globalClock.getTime());
    PauseRoutineMaxDuration = null
    // keep track of which components have finished
    PauseRoutineComponents = [];
    PauseRoutineComponents.push(Pause);
    
    for (const thisComponent of PauseRoutineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function PauseRoutineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PauseRoutine' ---
    // get current time
    t = PauseRoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pause* updates
    if (t >= 0.0 && Pause.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause.tStart = t;  // (not accounting for frame time here)
      Pause.frameNStart = frameN;  // exact frame index
      
      Pause.setAutoDraw(true);
    }
    
    
    // if Pause is active this frame...
    if (Pause.status === PsychoJS.Status.STARTED) {
    }
    
    // Run 'Each Frame' code from savePauseTime
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys();
    if (_pj.in_es6("space", keys)) {
        continueRoutine = false;
        psychoJS.eventManager.clearEvents();
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PauseRoutineComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PauseRoutineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PauseRoutine' ---
    for (const thisComponent of PauseRoutineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('PauseRoutine.stopped', globalClock.getTime());
    // Run 'End Routine' code from savePauseTime
    import * as time from 'time';
    psychoJS.experiment.addData("task.stopped_Unix", time.time());
    
    // the Routine "PauseRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function eyelinkStopRecording_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'eyelinkStopRecording_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    eyelinkStopRecording_2Clock.reset();
    routineTimer.reset();
    eyelinkStopRecording_2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from saveStopRecordTime_2
    import * as time from 'time';
    psychoJS.experiment.addData("el_recordingStop.started_Unix", time.time());
    
    psychoJS.experiment.addData('eyelinkStopRecording_2.started', globalClock.getTime());
    eyelinkStopRecording_2MaxDuration = null
    // keep track of which components have finished
    eyelinkStopRecording_2Components = [];
    
    for (const thisComponent of eyelinkStopRecording_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function eyelinkStopRecording_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'eyelinkStopRecording_2' ---
    // get current time
    t = eyelinkStopRecording_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of eyelinkStopRecording_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function eyelinkStopRecording_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'eyelinkStopRecording_2' ---
    for (const thisComponent of eyelinkStopRecording_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('eyelinkStopRecording_2.stopped', globalClock.getTime());
    // Run 'End Routine' code from elStopRecord_2
    clear_screen(psychoJS.window);
    el_tracker.sendMessage("blank_screen");
    el_tracker.sendMessage("!V CLEAR 128 128 128");
    offsetValue = Number.parseInt(Math.round(((core.getTime() - fixation.tStartRefresh) * 1000)));
    el_tracker.sendMessage(`${offsetValue}`);
    el_tracker.sendMessage(`${offsetValue}`);
    el_tracker.sendMessage(`${offsetValue} !V DRAWLINE 255 255 255 ${((scn_width / 2) - 50)} ${(scn_height / 2)} ${((scn_width / 2) + 50)} ${(scn_height / 2)}`);
    el_tracker.sendMessage(`${offsetValue} !V DRAWLINE 255 255 255 ${(scn_width / 2)} ${((scn_height / 2) - 50)} ${(scn_width / 2)} ${((scn_height / 2) + 50)}`);
    offsetValue = Number.parseInt(Math.round(((core.getTime() - image.tStartRefresh) * 1000)));
    el_tracker.sendMessage(`${offsetValue}`);
    el_tracker.sendMessage(`${offsetValue}`);
    el_tracker.sendMessage(`${offsetValue} !V IMGLOAD CENTER ../../${trialImage} ${(scn_width / 2)} ${(scn_height / 2)}`);
    if ((! (resp.rt instanceof list))) {
        offsetValue = Number.parseInt(Math.round(((core.getTime() - (image.tStartRefresh + resp.rt)) * 1000)));
        el_tracker.sendMessage(`${offsetValue}`);
    }
    pylink.pumpDelay(100);
    el_tracker.stopRecording();
    el_tracker.sendMessage(`!V TRIAL_VAR condition ${condition}`);
    el_tracker.sendMessage(`!V TRIAL_VAR identifier ${identifier}`);
    el_tracker.sendMessage(`!V TRIAL_VAR image ${trialImage}`);
    el_tracker.sendMessage(`!V TRIAL_VAR condition ${condition}`);
    el_tracker.sendMessage(`!V TRIAL_VAR corrAns ${corrAns}`);
    pylink.pumpDelay(1);
    el_tracker.sendMessage(`!V TRIAL_VAR accuracy ${resp.corr}`);
    el_tracker.sendMessage(`!V TRIAL_VAR keyPressed ${resp.keys}`);
    console.log(resp.rt.toString());
    if ((resp.rt instanceof list)) {
        el_tracker.sendMessage("!V TRIAL_VAR RT -1");
    } else {
        el_tracker.sendMessage(`!V TRIAL_VAR RT ${Number.parseInt(Math.round((resp.rt * 1000)))}`);
    }
    el_tracker.sendMessage(`TRIAL_RESULT ${0}`);
    trial_index = (trial_index + 1);
    
    // Run 'End Routine' code from saveStopRecordTime_2
    import * as time from 'time';
    psychoJS.experiment.addData("el_recordingStop.stopped_Unix", time.time());
    
    // the Routine "eyelinkStopRecording_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function thanksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'thanks' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    thanksClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    thanksMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from end_code
    import * as time from 'time';
    psychoJS.experiment.addData("experimentStop.started_Unix", time.time());
    
    psychoJS.experiment.addData('thanks.started', globalClock.getTime());
    thanksMaxDuration = null
    // keep track of which components have finished
    thanksComponents = [];
    thanksComponents.push(endScreen);
    
    for (const thisComponent of thanksComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function thanksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'thanks' ---
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endScreen* updates
    if (t >= 0.0 && endScreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endScreen.tStart = t;  // (not accounting for frame time here)
      endScreen.frameNStart = frameN;  // exact frame index
      
      endScreen.setAutoDraw(true);
    }
    
    
    // if endScreen is active this frame...
    if (endScreen.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (endScreen.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      endScreen.tStop = t;  // not accounting for scr refresh
      endScreen.frameNStop = frameN;  // exact frame index
      // update status
      endScreen.status = PsychoJS.Status.FINISHED;
      endScreen.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of thanksComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function thanksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'thanks' ---
    for (const thisComponent of thanksComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('thanks.stopped', globalClock.getTime());
    // Run 'End Routine' code from end_code
    import * as time from 'time';
    psychoJS.experiment.addData("experimentStop.stopped_Unix", time.time());
    
    if (routineForceEnded) {
        routineTimer.reset();} else if (thanksMaxDurationReached) {
        thanksClock.add(thanksMaxDuration);
    } else {
        thanksClock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
