// Import the necessary classes from the Premiere Pro scripting API
// var app = new PremierePro();
var project = app.project;
var seq;
var outputFilePath =  "C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\premiere-script\output-file.mp4";
var filesFolderPath = "~/Documents/history-queefs/history-queefs/premiere-script/input-vids";
var insertionBin = project.getInsertionBin();

// Get the video files in the folder
var filesFolder = new Folder(filesFolderPath);
var files = filesFolder.getFiles("*.mp4");
var filePaths = [];
for (var i = 0; i < files.length; i++) {
    filePaths.push(files[i].fullName);
}

// Create a new sequence with the settings of the first video file
var importSuccess = project.importFiles(filePaths, false, insertionBin, false);

var firstSeq = project.createNewSequenceFromClips("Sequence 1", [firstVideo[0]], null);
seq = firstSeq;

// Add the rest of the videos to the sequence
for (var i = 1; i < files.length; i++) {
    var video = project.importFiles([files[i]]);
    seq.insertClip(video[0], seq.getOutPoint());
}

// Export the sequence as an MP4 file
var exportSettings = app.encoder.createExportOptions(outputFilePath, 1080, 1920, app.encoder.ENCODE_QUALITY_HIGH);
exportSettings.setPresetFormat("MP4");
app.encoder.exportSequence(seq, outputFilePath, exportSettings);