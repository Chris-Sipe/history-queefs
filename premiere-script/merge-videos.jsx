// variable setup
var project = app.project;
var outputFilePath = "C:\\Users\\chris\\OneDrive\\Documents\\history-queefs\\history-queefs\\premiere-script\\output-vid.mp4";
var exportSettingsFilePath = "C:\\Users\\chris\\OneDrive\\Documents\\history-queefs\\history-queefs\\premiere-script\\history-queefs-preset.epr";
var filesFolderPath = "~/Documents/history-queefs/history-queefs/premiere-script/input-vids";
var seq;

// import video files into project
var filesFolder = new Folder(filesFolderPath);
var files = filesFolder.getFiles("*.mp4");
var filePaths = [];
for (var i = 0; i < files.length; i++) {
    var filePath = addExtraBackslash(files[i].fsName);
    filePaths.push(filePath);
}
var importSuccess = project.importFiles(filePaths);

// insert clips into sequence
var availableClipsCollection = project.rootItem.children;
var availableClipsArray = [];
for (var i = 0; i < availableClipsCollection.length; i++) {
    availableClipsArray.push(availableClipsCollection[i])
}
project.createNewSequenceFromClips("sequence 1", availableClipsArray, null);

// get sequence
if (project.sequences.length >= 1) {
    seq = project.sequences[0];
} else {
    alert("No sequence found in the project.");
    exit();
}

// set vertical
var seqSettings = seq.getSettings();
seqSettings.videoFrameWidth = 1080;
seqSettings.videoFrameHeight = 1920;
seq.setSettings(seqSettings);

// Export the sequence as an MP4 file
seq.exportAsMediaDirect(outputFilePath, exportSettingsFilePath, 0);

function addExtraBackslash(str) {
    return str.replace(/\\/g, "\\\\");
}